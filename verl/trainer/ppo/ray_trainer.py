# Copyright 2024 Bytedance Ltd. and/or its affiliates
# Copyright 2023-2024 SGLang Team
# Copyright 2025 ModelBest Inc. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
FSDP PPO Trainer with Ray-based single controller.
This trainer supports model-agonistic model initialization with huggingface
"""

import json
import os
import uuid
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum
from pprint import pprint
from typing import Optional, Type

import numpy as np
import ray
import torch
from omegaconf import OmegaConf, open_dict
from torch.utils.data import Dataset, Sampler
from torchdata.stateful_dataloader import StatefulDataLoader
from tqdm import tqdm

from verl import DataProto
from verl.protocol import pad_dataproto_to_divisor, unpad_dataproto
from verl.single_controller.base import Worker
from verl.single_controller.ray import RayClassWithInitArgs, RayResourcePool, RayWorkerGroup
from verl.single_controller.ray.base import create_colocated_worker_cls
from verl.trainer.ppo import core_algos
from verl.trainer.ppo.core_algos import AdvantageEstimator, agg_loss
from verl.trainer.ppo.metric_utils import (
    compute_data_metrics,
    compute_throughout_metrics,
    compute_timing_metrics,
    process_validation_metrics,
)
from verl.trainer.ppo.reward import compute_reward, compute_reward_async
from verl.utils.checkpoint.checkpoint_manager import BaseCheckpointManager, find_latest_ckpt_path
from verl.utils.debug import marked_timer
from verl.utils.metric import (
    reduce_metrics,
)
from verl.utils.seqlen_balancing import get_seqlen_balanced_partitions, log_seqlen_unbalance
from verl.utils.torch_functional import masked_mean
from verl.utils.tracking import ValidationGenerationsLogger

WorkerType = Type[Worker]


class Role(Enum):
    """
    To create more roles dynamically, you can subclass Role and add new members
    """

    Actor = 0
    Rollout = 1
    ActorRollout = 2
    Critic = 3
    RefPolicy = 4
    RewardModel = 5
    ActorRolloutRef = 6


@dataclass
class ResourcePoolManager:
    """
    Define a resource pool specification. Resource pool will be initialized first.
    """

    resource_pool_spec: dict[str, list[int]]
    mapping: dict[Role, str]
    resource_pool_dict: dict[str, RayResourcePool] = field(default_factory=dict)

    def create_resource_pool(self):
        for resource_pool_name, process_on_nodes in self.resource_pool_spec.items():
            # max_colocate_count means the number of WorkerGroups (i.e. processes) in each RayResourcePool
            # For FSDP backend, we recommend using max_colocate_count=1 that merge all WorkerGroups into one.
            # For Megatron backend, we recommend using max_colocate_count>1
            # that can utilize different WorkerGroup for differnt models
            resource_pool = RayResourcePool(process_on_nodes=process_on_nodes, use_gpu=True, max_colocate_count=1, name_prefix=resource_pool_name)
            self.resource_pool_dict[resource_pool_name] = resource_pool

        self._check_resource_available()

    def get_resource_pool(self, role: Role) -> RayResourcePool:
        """Get the resource pool of the worker_cls"""
        return self.resource_pool_dict[self.mapping[role]]

    def get_n_gpus(self) -> int:
        """Get the number of gpus in this cluster."""
        return sum([n_gpus for process_on_nodes in self.resource_pool_spec.values() for n_gpus in process_on_nodes])

    def _check_resource_available(self):
        """Check if the resource pool can be satisfied in this ray cluster."""
        node_available_resources = ray.state.available_resources_per_node()
        node_available_gpus = {node: node_info.get("GPU", 0) if "GPU" in node_info else node_info.get("NPU", 0) for node, node_info in node_available_resources.items()}

        # check total required gpus can be satisfied
        total_available_gpus = sum(node_available_gpus.values())
        total_required_gpus = sum([n_gpus for process_on_nodes in self.resource_pool_spec.values() for n_gpus in process_on_nodes])
        if total_available_gpus < total_required_gpus:
            raise ValueError(f"Total available GPUs {total_available_gpus} is less than total desired GPUs {total_required_gpus}")

        # check each resource pool can be satisfied, O(#resource_pools * #nodes)
        for resource_pool_name, process_on_nodes in self.resource_pool_spec.items():
            num_gpus, num_nodes = process_on_nodes[0], len(process_on_nodes)
            for node, available_gpus in node_available_gpus.items():
                if available_gpus >= num_gpus:
                    node_available_gpus[node] -= num_gpus
                    num_nodes -= 1
                    if num_nodes == 0:
                        break
            if num_nodes > 0:
                raise ValueError(f"Resource pool {resource_pool_name}: {num_gpus}*{num_nodes}" + "cannot be satisfied in this ray cluster")


def apply_kl_penalty(data: DataProto, kl_ctrl: core_algos.AdaptiveKLController, kl_penalty="kl", multi_turn=False):
    """Apply KL penalty to the token-level rewards.

    This function computes the KL divergence between the reference policy and current policy,
    then applies a penalty to the token-level rewards based on this divergence.

    Args:
        data (DataProto): The data containing batched model outputs and inputs.
        kl_ctrl (core_algos.AdaptiveKLController): Controller for adaptive KL penalty.
        kl_penalty (str, optional): Type of KL penalty to apply. Defaults to "kl".
        multi_turn (bool, optional): Whether the data is from a multi-turn conversation. Defaults to False.

    Returns:
        tuple: A tuple containing:
            - The updated data with token-level rewards adjusted by KL penalty
            - A dictionary of metrics related to the KL penalty
    """
    responses = data.batch["responses"]
    response_length = responses.size(1)
    token_level_scores = data.batch["token_level_scores"]
    batch_size = data.batch.batch_size[0]

    if multi_turn:
        loss_mask = data.batch["loss_mask"]
        response_mask = loss_mask[:, -response_length:]
    else:
        attention_mask = data.batch["attention_mask"]
        response_mask = attention_mask[:, -response_length:]

    # compute kl between ref_policy and current policy
    # When apply_kl_penalty, algorithm.use_kl_in_reward=True, so the reference model has been enabled.
    kld = core_algos.kl_penalty(data.batch["old_log_probs"], data.batch["ref_log_prob"], kl_penalty=kl_penalty)  # (batch_size, response_length)
    kld = kld * response_mask
    beta = kl_ctrl.value

    token_level_rewards = token_level_scores - beta * kld

    current_kl = masked_mean(kld, mask=response_mask, axis=-1)  # average over sequence
    current_kl = torch.mean(current_kl, dim=0).item()

    # according to https://github.com/huggingface/trl/blob/951ca1841f29114b969b57b26c7d3e80a39f75a0/trl/trainer/ppo_trainer.py#L837
    kl_ctrl.update(current_kl=current_kl, n_steps=batch_size)
    data.batch["token_level_rewards"] = token_level_rewards

    metrics = {"actor/reward_kl_penalty": current_kl, "actor/reward_kl_penalty_coeff": beta}

    return data, metrics


def compute_response_mask(data: DataProto):
    """Compute the attention mask for the response part of the sequence.

    This function extracts the portion of the attention mask that corresponds to the model's response,
    which is used for masking computations that should only apply to response tokens.

    Args:
        data (DataProto): The data containing batched model outputs and inputs.

    Returns:
        torch.Tensor: The attention mask for the response tokens.
    """
    responses = data.batch["responses"]
    response_length = responses.size(1)
    attention_mask = data.batch["attention_mask"]
    return attention_mask[:, -response_length:]


def compute_advantage(
    data: DataProto, 
    adv_estimator, 
    gamma=1.0, 
    lam=1.0, 
    num_repeat=1, 
    multi_turn=False, 
    norm_adv_by_std_in_grpo=True, 
    no_advantage_weighting_on_off_policy_data=False,
    config=None,
):
    """Compute advantage estimates for policy optimization.

    This function computes advantage estimates using various estimators like GAE, GRPO, REINFORCE++, etc.
    The advantage estimates are used to guide policy optimization in RL algorithms.

    Args:
        data (DataProto): The data containing batched model outputs and inputs.
        adv_estimator: The advantage estimator to use (e.g., GAE, GRPO, REINFORCE++).
        gamma (float, optional): Discount factor for future rewards. Defaults to 1.0.
        lam (float, optional): Lambda parameter for GAE. Defaults to 1.0.
        num_repeat (int, optional): Number of times to repeat the computation. Defaults to 1.
        multi_turn (bool, optional): Whether the data is from a multi-turn conversation. Defaults to False.
        norm_adv_by_std_in_grpo (bool, optional): Whether to normalize advantages by standard deviation in GRPO. Defaults to True.
        config (dict, optional): Configuration dictionary for algorithm settings. Defaults to None.

    Returns:
        DataProto: The updated data with computed advantages and returns.
    """
    # Back-compatible with trainers that do not compute response mask in fit
    if "response_mask" not in data.batch.keys():
        data.batch["response_mask"] = compute_response_mask(data)

    # prepare response group
    if adv_estimator == AdvantageEstimator.GAE:
        # Compute advantages and returns using Generalized Advantage Estimation (GAE)
        advantages, returns = core_algos.compute_gae_advantage_return(
            token_level_rewards=data.batch["token_level_rewards"],
            values=data.batch["values"],
            response_mask=data.batch["response_mask"],
            gamma=gamma,
            lam=lam,
        )
        data.batch["advantages"] = advantages
        data.batch["returns"] = returns
        if config.get("use_pf_ppo", False):
            data = core_algos.compute_pf_ppo_reweight_data(
                data,
                config.get("pf_ppo_reweight_method", "pow"),
                config.get("pf_ppo_weight_pow", 2.0),
            )

    elif adv_estimator in [AdvantageEstimator.GRPO, AdvantageEstimator.ONESIDEDGRPO]:
        # Initialize the mask for GRPO calculation
        grpo_calculation_mask = data.batch["response_mask"]
        if multi_turn:
            # If multi-turn, replace the mask with the relevant part of loss_mask
            # Get length from the initial response mask
            response_length = grpo_calculation_mask.size(1)
            # This mask is the one intended for GRPO
            grpo_calculation_mask = data.batch["loss_mask"][:, -response_length:]
        # Call compute_grpo_outcome_advantage with parameters matching its definition
        advantages, returns = core_algos.compute_grpo_outcome_advantage(
            token_level_rewards=data.batch["token_level_rewards"],
            response_mask=grpo_calculation_mask,
            index=data.non_tensor_batch["uid"],
            norm_adv_by_std_in_grpo=norm_adv_by_std_in_grpo,
        )
        data.batch["advantages"] = advantages
        data.batch["returns"] = returns
        
    elif adv_estimator == AdvantageEstimator.MAXRL:
        # Initialize the mask for GRPO calculation
        grpo_calculation_mask = data.batch["response_mask"]
        if multi_turn:
            # If multi-turn, replace the mask with the relevant part of loss_mask
            # Get length from the initial response mask
            response_length = grpo_calculation_mask.size(1)
            # This mask is the one intended for GRPO
            grpo_calculation_mask = data.batch["loss_mask"][:, -response_length:]
        # Call compute_grpo_outcome_advantage with parameters matching its definition
        advantages, returns = core_algos.compute_maxrl_outcome_advantage(
            token_level_rewards=data.batch["token_level_rewards"],
            response_mask=grpo_calculation_mask,
            index=data.non_tensor_batch["uid"],
            norm_adv_by_std_in_grpo=norm_adv_by_std_in_grpo,
        )
        data.batch["advantages"] = advantages
        data.batch["returns"] = returns

    elif adv_estimator == AdvantageEstimator.GRPO_WITH_FILTERED_SFT:
        # Initialize the mask for SFT calculation
        sft_calculation_mask = data.batch["response_mask"]

        if multi_turn:
            # If multi-turn, replace the mask with the relevant part of loss_mask
            # Get length from the initial response mask
            response_length = sft_calculation_mask.size(1)
            # This mask is the one intended for GRPO
            sft_calculation_mask = data.batch["loss_mask"][:, -response_length:]

        # Call compute_grpo_outcome_advantage with parameters matching its definition
        advantages, returns, off_policy_mask = core_algos.compute_grpo_with_filtered_sft_outcome_advantage(
            token_level_rewards=data.batch["token_level_rewards"],
            response_mask=sft_calculation_mask,
            data_policy_labels=data.non_tensor_batch["data_policy_labels"],
            index=data.non_tensor_batch["uid"],
            norm_adv_by_std_in_grpo=norm_adv_by_std_in_grpo,
            no_advantage_weighting_on_off_policy_data=no_advantage_weighting_on_off_policy_data,
        )
        data.batch["advantages"] = advantages
        data.batch["returns"] = returns
        data.batch["off_policy_mask"] = off_policy_mask
        
    elif adv_estimator == AdvantageEstimator.SELF_PAPER:
        # Initialize the mask for SELF_PAPER calculation
        calculation_mask = data.batch["response_mask"]
        if multi_turn:
            response_length = calculation_mask.size(1)
            calculation_mask = data.batch["loss_mask"][:, -response_length:]
        
        # Get reward_baselines if available
        reward_baselines = data.batch.get("reward_baselines", None)
        
        # Call compute_self_paper_outcome_advantage with both GRPO params and reward_baselines
        advantages, returns = core_algos.compute_self_paper_outcome_advantage(
            token_level_rewards=data.batch["token_level_rewards"],
            response_mask=calculation_mask,
            index=data.non_tensor_batch["uid"],
            norm_adv_by_std_in_grpo=norm_adv_by_std_in_grpo,
            reward_baselines=reward_baselines,
            config=config,
        )
        data.batch["advantages"] = advantages
        data.batch["returns"] = returns
    
    elif adv_estimator == AdvantageEstimator.DSGRPO:
        # DSGRPO (Differential Smoothing GRPO) handler
        # Initialize the mask for calculation
        calculation_mask = data.batch["response_mask"]
        if multi_turn:
            response_length = calculation_mask.size(1)
            calculation_mask = data.batch["loss_mask"][:, -response_length:]
        
        # Get old_log_probs for differential smoothing
        old_log_probs = data.batch.get("old_log_probs", None)
        
        # Call compute_dsgrpo_outcome_advantage
        advantages, returns = core_algos.compute_dsgrpo_outcome_advantage(
            token_level_rewards=data.batch["token_level_rewards"],
            response_mask=calculation_mask,
            index=data.non_tensor_batch["uid"],
            norm_adv_by_std_in_grpo=norm_adv_by_std_in_grpo,
            config=config,
            old_log_probs=old_log_probs,
        )
        data.batch["advantages"] = advantages
        data.batch["returns"] = returns
        
    else:
        # handle all other adv estimator type other than GAE, GRPO and SFT
        adv_estimator_fn = core_algos.get_adv_estimator_fn(adv_estimator)
        adv_kwargs = {
            "token_level_rewards": data.batch["token_level_rewards"],
            "response_mask": data.batch["response_mask"],
            "config": config,
        }
        if "uid" in data.non_tensor_batch:  # optional
            adv_kwargs["index"] = data.non_tensor_batch["uid"]
        reward_baselines = data.batch.get("reward_baselines", None)  # optional, compatible with all tensordict versions
        if reward_baselines is not None:
            adv_kwargs["reward_baselines"] = reward_baselines

        # calculate advantage estimator
        advantages, returns = adv_estimator_fn(**adv_kwargs)
        data.batch["advantages"] = advantages
        data.batch["returns"] = returns

    return data


class RayPPOTrainer:
    """
    Note that this trainer runs on the driver process on a single CPU/GPU node.
    """

    # TODO: support each role have individual ray_worker_group_cls,
    # i.e., support different backend of different role
    def __init__(
        self,
        config,
        tokenizer,
        role_worker_mapping: dict[Role, WorkerType],
        resource_pool_manager: ResourcePoolManager,
        ray_worker_group_cls: RayWorkerGroup = RayWorkerGroup,
        processor=None,
        reward_fn=None,
        val_reward_fn=None,
        train_dataset: Optional[Dataset] = None,
        val_dataset: Optional[Dataset] = None,
        collate_fn=None,
        train_sampler: Optional[Sampler] = None,
        device_name="cuda",
    ):
        """Initialize distributed PPO trainer with Ray backend."""

        self.tokenizer = tokenizer
        self.processor = processor
        self.config = config
        self.reward_fn = reward_fn
        self.val_reward_fn = val_reward_fn

        self.hybrid_engine = config.actor_rollout_ref.hybrid_engine
        assert self.hybrid_engine, "Currently, only support hybrid engine"

        if self.hybrid_engine:
            assert Role.ActorRollout in role_worker_mapping, f"{role_worker_mapping.keys()=}"

        self.role_worker_mapping = role_worker_mapping
        self.resource_pool_manager = resource_pool_manager
        self.use_reference_policy = Role.RefPolicy in role_worker_mapping
        self.use_rm = Role.RewardModel in role_worker_mapping
        self.ray_worker_group_cls = ray_worker_group_cls
        self.device_name = device_name
        self.validation_generations_logger = ValidationGenerationsLogger()

        # if ref_in_actor is True, the reference policy will be actor without lora applied
        self.ref_in_actor = config.actor_rollout_ref.model.get("lora_rank", 0) > 0

        # define in-reward KL control
        # kl loss control currently not suppoorted
        if config.algorithm.use_kl_in_reward:
            self.kl_ctrl_in_reward = core_algos.get_kl_controller(config.algorithm.kl_ctrl)

        if self.config.algorithm.adv_estimator == AdvantageEstimator.GAE:
            self.use_critic = True

        elif self.config.algorithm.adv_estimator in [
            AdvantageEstimator.GRPO,
            AdvantageEstimator.DSGRPO,
            AdvantageEstimator.GRPO_PASSK,
            AdvantageEstimator.REINFORCE_PLUS_PLUS,
            AdvantageEstimator.REMAX,
            AdvantageEstimator.RLOO,
            AdvantageEstimator.OPO,
            AdvantageEstimator.REINFORCE_PLUS_PLUS_BASELINE,
            AdvantageEstimator.GRPO_WITH_FILTERED_SFT,
            AdvantageEstimator.MAXRL,
            AdvantageEstimator.PKPO,
            AdvantageEstimator.MACLAURIN,
            AdvantageEstimator.CROSS_FITTED_MACLAURIN,
            AdvantageEstimator.MACLAURIN_BASELINE,
            AdvantageEstimator.VR_COND,
            AdvantageEstimator.SELF_PAPER,
            AdvantageEstimator.MISC,
            AdvantageEstimator.OVERSAMPLE_SUBSET_VR_WEIGHTS,
            AdvantageEstimator.CLIPPED_P_NORMALIZATION,
            AdvantageEstimator.ONESIDEDGRPO
        ]:
            self.use_critic = False

        else:
            raise NotImplementedError

        self._validate_config()
        self._create_dataloader(train_dataset, val_dataset, collate_fn, train_sampler)

        self.wandb_id = None

    def _validate_config(self):
        config = self.config
        # number of GPUs total
        n_gpus = config.trainer.n_gpus_per_node * config.trainer.nnodes
        if config.actor_rollout_ref.actor.strategy == "megatron":
            model_parallel_size = config.actor_rollout_ref.actor.megatron.tensor_model_parallel_size * config.actor_rollout_ref.actor.megatron.pipeline_model_parallel_size
            assert n_gpus % (model_parallel_size * config.actor_rollout_ref.actor.megatron.context_parallel_size) == 0, f"n_gpus ({n_gpus}) must be divisible by model_parallel_size ({model_parallel_size}) times context_parallel_size ({config.actor_rollout_ref.actor.megatron.context_parallel_size})"
            megatron_dp = n_gpus // (model_parallel_size * config.actor_rollout_ref.actor.megatron.context_parallel_size)
            minimal_bsz = megatron_dp * config.actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu
        else:
            minimal_bsz = n_gpus

        # 1. Check total batch size for data correctness
        real_train_batch_size = config.data.train_batch_size * config.actor_rollout_ref.rollout.n
        assert real_train_batch_size % minimal_bsz == 0, f"real_train_batch_size ({real_train_batch_size}) must be divisible by minimal possible batch size ({minimal_bsz})"

        # A helper function to check "micro_batch_size" vs "micro_batch_size_per_gpu"
        # We throw an error if the user sets both. The new convention is "..._micro_batch_size_per_gpu".
        def check_mutually_exclusive(mbs, mbs_per_gpu, name: str):
            settings = {
                "actor_rollout_ref.actor": "micro_batch_size",
                "critic": "micro_batch_size",
                "reward_model": "micro_batch_size",
                "actor_rollout_ref.ref": "log_prob_micro_batch_size",
                "actor_rollout_ref.rollout": "log_prob_micro_batch_size",
            }

            if name in settings:
                param = settings[name]
                param_per_gpu = f"{param}_per_gpu"

                if mbs is None and mbs_per_gpu is None:
                    raise ValueError(f"[{name}] Please set at least one of '{name}.{param}' or '{name}.{param_per_gpu}'.")

                if mbs is not None and mbs_per_gpu is not None:
                    raise ValueError(f"[{name}] You have set both '{name}.{param}' AND '{name}.{param_per_gpu}'. Please remove '{name}.{param}' because only '*_{param_per_gpu}'" + "is supported (the former is deprecated).")

        if not config.actor_rollout_ref.actor.use_dynamic_bsz:
            # actor: ppo_micro_batch_size vs. ppo_micro_batch_size_per_gpu
            check_mutually_exclusive(
                config.actor_rollout_ref.actor.ppo_micro_batch_size,
                config.actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu,
                "actor_rollout_ref.actor",
            )

            if self.use_reference_policy:
                # reference: log_prob_micro_batch_size vs. log_prob_micro_batch_size_per_gpu
                check_mutually_exclusive(
                    config.actor_rollout_ref.ref.log_prob_micro_batch_size,
                    config.actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu,
                    "actor_rollout_ref.ref",
                )

            #  The rollout section also has log_prob_micro_batch_size vs. log_prob_micro_batch_size_per_gpu
            check_mutually_exclusive(
                config.actor_rollout_ref.rollout.log_prob_micro_batch_size,
                config.actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu,
                "actor_rollout_ref.rollout",
            )

        if self.use_critic and not config.critic.use_dynamic_bsz:
            # Check for critic micro-batch size conflicts
            check_mutually_exclusive(config.critic.ppo_micro_batch_size, config.critic.ppo_micro_batch_size_per_gpu, "critic")

        # Check for reward model micro-batch size conflicts
        if config.reward_model.enable and not config.reward_model.use_dynamic_bsz:
            check_mutually_exclusive(config.reward_model.micro_batch_size, config.reward_model.micro_batch_size_per_gpu, "reward_model")

        # Actor
        # check if train_batch_size is larger than ppo_mini_batch_size
        # if NOT dynamic_bsz, we must ensure:
        #    ppo_mini_batch_size is divisible by ppo_micro_batch_size
        #    ppo_micro_batch_size * sequence_parallel_size >= n_gpus
        if not config.actor_rollout_ref.actor.use_dynamic_bsz:
            assert config.data.train_batch_size >= config.actor_rollout_ref.actor.ppo_mini_batch_size
            sp_size = config.actor_rollout_ref.actor.get("ulysses_sequence_parallel_size", 1)
            if config.actor_rollout_ref.actor.ppo_micro_batch_size is not None:
                assert config.actor_rollout_ref.actor.ppo_mini_batch_size % config.actor_rollout_ref.actor.ppo_micro_batch_size == 0
                assert config.actor_rollout_ref.actor.ppo_micro_batch_size * sp_size >= n_gpus

        assert config.actor_rollout_ref.actor.loss_agg_mode in [
            "token-mean",
            "seq-mean-token-sum",
            "seq-mean-token-mean",
            "seq-mean-token-sum-norm",
        ], f"Invalid loss_agg_mode: {config.actor_rollout_ref.actor.loss_agg_mode}"

        if config.algorithm.use_kl_in_reward and config.actor_rollout_ref.actor.use_kl_loss:
            print("NOTICE: You have both enabled in-reward kl and kl loss.")

        # critic
        if self.use_critic and not config.critic.use_dynamic_bsz:
            assert config.data.train_batch_size >= config.critic.ppo_mini_batch_size
            sp_size = config.critic.get("ulysses_sequence_parallel_size", 1)
            if config.critic.ppo_micro_batch_size is not None:
                assert config.critic.ppo_mini_batch_size % config.critic.ppo_micro_batch_size == 0
                assert config.critic.ppo_micro_batch_size * sp_size >= n_gpus

        # Check if use_remove_padding is enabled when using sequence parallelism for fsdp
        if config.actor_rollout_ref.actor.strategy == "fsdp" and (config.actor_rollout_ref.actor.get("ulysses_sequence_parallel_size", 1) > 1 or config.actor_rollout_ref.ref.get("ulysses_sequence_parallel_size", 1) > 1):
            assert config.actor_rollout_ref.model.use_remove_padding, "When using sequence parallelism for actor/ref policy, you must enable `use_remove_padding`."

        if self.use_critic and config.critic.strategy == "fsdp":
            if config.critic.get("ulysses_sequence_parallel_size", 1) > 1:
                assert config.critic.model.use_remove_padding, "When using sequence parallelism for critic, you must enable `use_remove_padding`."

        if config.data.get("val_batch_size", None) is not None:
            print("WARNING: val_batch_size is deprecated." + " Validation datasets are sent to inference engines as a whole batch," + " which will schedule the memory themselves.")

        # check eval config
        if config.actor_rollout_ref.rollout.val_kwargs.do_sample:
            assert config.actor_rollout_ref.rollout.temperature > 0, "validation gen temperature should be greater than 0 when enabling do_sample"

        # check multi_turn with tool config
        if config.actor_rollout_ref.rollout.multi_turn.enable:
            assert config.actor_rollout_ref.rollout.multi_turn.tool_config_path is not None, "tool_config_path must be set when enabling multi_turn with tool, due to no role-playing support"
            assert config.algorithm.adv_estimator in [AdvantageEstimator.GRPO], "only GRPO is tested for multi-turn with tool"

        print("[validate_config] All configuration checks passed successfully!")

    def _create_dataloader(self, train_dataset, val_dataset, collate_fn, train_sampler):
        """
        Creates the train and validation dataloaders.
        """
        # TODO: we have to make sure the batch size is divisible by the dp size
        from verl.trainer.main_ppo import create_rl_dataset, create_rl_sampler

        if train_dataset is None:
            train_dataset = create_rl_dataset(self.config.data.train_files, self.config.data, self.tokenizer, self.processor)
        if val_dataset is None:
            val_dataset = create_rl_dataset(self.config.data.val_files, self.config.data, self.tokenizer, self.processor)
        self.train_dataset, self.val_dataset = train_dataset, val_dataset

        if train_sampler is None:
            train_sampler = create_rl_sampler(self.config.data, self.train_dataset)
        if collate_fn is None:
            from verl.utils.dataset.rl_dataset import collate_fn as default_collate_fn

            collate_fn = default_collate_fn

        self.train_dataloader = StatefulDataLoader(
            dataset=self.train_dataset,
            batch_size=self.config.data.get("gen_batch_size", self.config.data.train_batch_size),
            num_workers=self.config.data.get("dataloader_num_workers", 8),
            drop_last=True,
            collate_fn=collate_fn,
            sampler=train_sampler,
        )

        val_batch_size = self.config.data.val_batch_size  # Prefer config value if set
        if val_batch_size is None:
            val_batch_size = len(self.val_dataset)

        self.val_dataloader = StatefulDataLoader(
            dataset=self.val_dataset,
            batch_size=val_batch_size,
            num_workers=self.config.data.get("dataloader_num_workers", 8),
            shuffle=self.config.data.get("validation_shuffle", True),
            drop_last=False,
            collate_fn=collate_fn,
        )

        assert len(self.train_dataloader) >= 1, "Train dataloader is empty!"
        assert len(self.val_dataloader) >= 1, "Validation dataloader is empty!"

        print(f"Size of train dataloader: {len(self.train_dataloader)}, Size of val dataloader: {len(self.val_dataloader)}")

        total_training_steps = len(self.train_dataloader) * self.config.trainer.total_epochs

        if self.config.trainer.total_training_steps is not None:
            total_training_steps = self.config.trainer.total_training_steps

        self.total_training_steps = total_training_steps
        print(f"Total training steps: {self.total_training_steps}")

        try:
            OmegaConf.set_struct(self.config, True)
            with open_dict(self.config):
                if OmegaConf.select(self.config, "actor_rollout_ref.actor.optim"):
                    self.config.actor_rollout_ref.actor.optim.total_training_steps = total_training_steps
                if OmegaConf.select(self.config, "critic.optim"):
                    self.config.critic.optim.total_training_steps = total_training_steps
        except Exception as e:
            print(f"Warning: Could not set total_training_steps in config. Structure missing? Error: {e}")

    def _dump_generations(self, inputs, outputs, scores, reward_extra_infos_dict, dump_path):
        """Dump rollout/validation samples as JSONL."""
        os.makedirs(dump_path, exist_ok=True)
        filename = os.path.join(dump_path, f"{self.global_steps}.jsonl")

        n = len(inputs)
        base_data = {
            "input": inputs,
            "output": outputs,
            "score": scores,
            "step": [self.global_steps] * n,
        }

        for k, v in reward_extra_infos_dict.items():
            if len(v) == n:
                base_data[k] = v

        lines = []
        for i in range(n):
            entry = {k: v[i] for k, v in base_data.items()}
            lines.append(json.dumps(entry, ensure_ascii=False))

        with open(filename, "w") as f:
            f.write("\n".join(lines) + "\n")

        print(f"Dumped generations to {filename}")

    def _maybe_log_val_generations(self, inputs, outputs, scores):
        """Log a table of validation samples to the configured logger (wandb or swanlab)"""

        generations_to_log = self.config.trainer.log_val_generations

        if generations_to_log == 0:
            return

        # Create tuples of (input, output, score) and sort by input text
        samples = list(zip(inputs, outputs, scores))
        samples.sort(key=lambda x: x[0])  # Sort by input text

        # Use fixed random seed for deterministic shuffling
        rng = np.random.RandomState(42)
        rng.shuffle(samples)

        # Take first N samples after shuffling
        samples = samples[:generations_to_log]

        # Log to each configured logger
        self.validation_generations_logger.log(self.config.trainer.logger, samples, self.global_steps)

    def _validate(self):
        data_source_lst = []
        reward_extra_infos_dict: dict[str, list] = defaultdict(list)

        # Lists to collect samples for the table
        sample_inputs = []
        sample_outputs = []
        sample_scores = []

        # Interval binning accumulators
        global_interval_counts = defaultdict(float)
        global_interval_total = 0

        per_ds_interval_counts = defaultdict(lambda: defaultdict(float))
        per_ds_interval_totals = defaultdict(int)

        global_interval_fractions = None
        per_ds_interval_fractions = None

        # Majority voting aggregation variables
        global_mv_correct = 0.0
        global_mv_total = 0
        per_ds_mv_correct = defaultdict(float)
        per_ds_mv_total = defaultdict(int)

        for test_data in self.val_dataloader:
            test_batch_original = DataProto.from_single_dict(test_data)

            # we only do validation on rule-based rm
            if self.config.reward_model.enable and test_batch_original[0].non_tensor_batch["reward_model"]["style"] == "model":
                return {}

            # Check if batched generation is configured
            val_n = self.config.actor_rollout_ref.rollout.val_kwargs.n
            val_gen_batch_size = self.config.actor_rollout_ref.rollout.val_kwargs.get("gen_batch_size", None)
            
            if val_gen_batch_size and val_gen_batch_size > 0 and val_n > val_gen_batch_size:
                # Batched generation with INCREMENTAL reward computation to save memory
                # Each round: generate, compute rewards, keep only essential info, free memory
                # NOTE: Majority voting and interval fractions are computed at the END using
                # accumulated per-item data (extracted_answer, accuracy, prompt_key, data_source)
                total_rounds = (val_n + val_gen_batch_size - 1) // val_gen_batch_size
                num_prompts = len(test_batch_original)
                print(f"[Validation] Split into {total_rounds} rounds ({num_prompts} prompts × {val_n} rollouts, {val_gen_batch_size} rollouts per round)")
                print(f"[Validation] Using incremental reward computation to save memory")
                print(f"[Validation] Majority voting will be computed at the END using all accumulated data")
                
                # We'll process rewards incrementally instead of accumulating all batches
                round_processed = False
                
                # Accumulators for per-item data (for final majority voting / interval fraction computation)
                all_extracted_answers = []
                all_accuracies = []
                all_prompt_keys = []
                all_data_sources_for_mv = []
                
                for current_round in range(total_rounds):
                    # Calculate how many rollouts for this round
                    round_start = current_round * val_gen_batch_size
                    round_end = min((current_round + 1) * val_gen_batch_size, val_n)
                    round_n = round_end - round_start
                    
                    print(f"[Validation] Generation start round {current_round + 1}/{total_rounds} ({num_prompts} prompts × {round_n} rollouts)")
                    
                    # Make a copy and repeat for this round
                    round_batch = deepcopy(test_batch_original)
                    round_batch = round_batch.repeat(repeat_times=round_n, interleave=True)
                    
                    # Save input_ids before any modifications
                    round_input_ids = round_batch.batch["input_ids"].clone()
                    
                    # Make another copy for generation (pop will modify the object)
                    round_batch_for_gen = deepcopy(round_batch)
                    
                    # Prepare generation batch (pop from the copy, not the original)
                    batch_keys_to_pop = ["input_ids", "attention_mask", "position_ids"]
                    non_tensor_batch_keys_to_pop = ["raw_prompt_ids"]
                    if "multi_modal_data" in round_batch_for_gen.non_tensor_batch:
                        non_tensor_batch_keys_to_pop.append("multi_modal_data")
                    if "raw_prompt" in round_batch_for_gen.non_tensor_batch:
                        non_tensor_batch_keys_to_pop.append("raw_prompt")
                    if "tools_kwargs" in round_batch_for_gen.non_tensor_batch:
                        non_tensor_batch_keys_to_pop.append("tools_kwargs")
                    round_gen_batch = round_batch_for_gen.pop(
                        batch_keys=batch_keys_to_pop,
                        non_tensor_batch_keys=non_tensor_batch_keys_to_pop,
                    )
                    
                    round_gen_batch.meta_info = {
                        "eos_token_id": self.tokenizer.eos_token_id,
                        "pad_token_id": self.tokenizer.pad_token_id,
                        "recompute_log_prob": False,
                        "do_sample": self.config.actor_rollout_ref.rollout.val_kwargs.do_sample,
                        "validate": True,
                    }
                    
                    # Pad to be divisible by dp_size
                    round_gen_batch_padded, round_pad_size = pad_dataproto_to_divisor(round_gen_batch, self.actor_rollout_wg.world_size)
                    
                    if not self.async_rollout_mode:
                        round_output_padded = self.actor_rollout_wg.generate_sequences(round_gen_batch_padded)
                    else:
                        self.async_rollout_manager.wake_up()
                        round_output_padded = self.async_rollout_manager.generate_sequences(round_gen_batch_padded)
                        self.async_rollout_manager.sleep()
                    
                    # Unpad
                    round_output = unpad_dataproto(round_output_padded, pad_size=round_pad_size)
                    print(f"[Validation] Generation end round {current_round + 1}/{total_rounds}")
                    
                    # Free generation batch memory
                    del round_gen_batch, round_gen_batch_padded, round_output_padded, round_batch_for_gen
                    
                    # === INCREMENTAL REWARD COMPUTATION ===
                    # Process this round's rewards immediately instead of accumulating
                    
                    # Decode input texts for this round
                    round_input_texts = [self.tokenizer.decode(ids, skip_special_tokens=True) for ids in round_input_ids]
                    sample_inputs.extend(round_input_texts)
                    del round_input_ids  # Free memory
                    
                    # Decode output texts for this round
                    round_output_ids = round_output.batch["responses"]
                    round_output_texts = [self.tokenizer.decode(ids, skip_special_tokens=True) for ids in round_output_ids]
                    sample_outputs.extend(round_output_texts)
                    
                    # Pop conflicting keys from round_batch before union
                    keys_to_pop_for_union = ["input_ids", "attention_mask", "position_ids"]
                    for key in keys_to_pop_for_union:
                        if key in round_batch.batch.keys():
                            round_batch.batch.pop(key)
                    
                    # Union batch with generation output
                    round_batch = round_batch.union(round_output)
                    del round_output  # Free memory
                    
                    # Compute rewards for this round
                    round_batch.meta_info["validate"] = True  # Enable majority voting calculation
                    result = self.val_reward_fn(round_batch, return_dict=True)
                    reward_tensor = result["reward_tensor"]
                    scores = reward_tensor.sum(-1).cpu().tolist()
                    sample_scores.extend(scores)
                    
                    # Collect reward extra info (including per-item extracted_answer, accuracy, prompt_key, data_source)
                    reward_extra_infos_dict["reward"].extend(scores)
                    if "reward_extra_info" in result:
                        for key, lst in result["reward_extra_info"].items():
                            reward_extra_infos_dict[key].extend(lst)
                            # Accumulate per-item data for final majority voting computation
                            if key == "extracted_answer":
                                all_extracted_answers.extend(lst)
                            elif key == "accuracy":
                                all_accuracies.extend(lst)
                            elif key == "prompt_key":
                                all_prompt_keys.extend(lst)
                            elif key == "data_source":
                                all_data_sources_for_mv.extend(lst)
                    
                    # Collect data sources
                    batch_data_sources = round_batch.non_tensor_batch.get(
                        "data_source", np.array(["unknown"] * reward_tensor.shape[0])
                    )
                    data_source_lst.append(batch_data_sources)
                    
                    # NOTE: We IGNORE the per-round majority voting and interval fraction results
                    # because they are computed on partial data (only this round's samples per prompt)
                    # We will compute these metrics at the END using all accumulated data
                    
                    # Free round batch memory - we've extracted everything we need
                    del round_batch, result, reward_tensor
                    import gc
                    gc.collect()
                    
                    print(f"[Validation] Round {current_round + 1}/{total_rounds} rewards computed, memory freed")
                
                # === FINAL MAJORITY VOTING AND INTERVAL FRACTION COMPUTATION ===
                # Now compute these metrics using ALL accumulated per-item data
                print(f"[Validation] Computing majority voting and interval fractions using all {len(all_extracted_answers)} samples...")
                
                if all_extracted_answers and all_accuracies and all_prompt_keys and all_data_sources_for_mv:
                    from verl.workers.reward_manager.multi_thread_naive import most_frequent_answer_with_score
                    
                    # Group by (data_source, prompt_key)
                    prompt_to_answers = defaultdict(lambda: defaultdict(list))
                    prompt_to_accuracies = defaultdict(lambda: defaultdict(list))
                    
                    for i in range(len(all_extracted_answers)):
                        ds = all_data_sources_for_mv[i]
                        pk = all_prompt_keys[i]
                        ans = all_extracted_answers[i]
                        acc = all_accuracies[i]
                        prompt_to_answers[ds][pk].append((ans, acc))
                        prompt_to_accuracies[ds][pk].append(acc)
                    
                    # Compute majority voting (accumulate, don't reset, in case of multiple validation batches)
                    # Note: global_mv_correct, global_mv_total, per_ds_mv_correct, per_ds_mv_total
                    # are already initialized at the start of _validate(), so we just add to them
                    
                    # Track math500_level for aggregation
                    math500_level_suffixes = {f"math500_level{i}" for i in range(1, 6)}
                    math500_all_mv_correct = 0
                    math500_all_mv_total = 0
                    
                    for ds, prompts in prompt_to_answers.items():
                        is_math500_level = any(ds.endswith(suffix) for suffix in math500_level_suffixes)
                        
                        for pk, ans_score_list in prompts.items():
                            if not ans_score_list:
                                continue
                            majority_ans, is_correct = most_frequent_answer_with_score(ans_score_list)
                            
                            global_mv_total += 1
                            per_ds_mv_total[ds] += 1
                            if is_correct:
                                global_mv_correct += 1
                                per_ds_mv_correct[ds] += 1
                            
                            if is_math500_level:
                                math500_all_mv_total += 1
                                if is_correct:
                                    math500_all_mv_correct += 1
                    
                    # Log majority voting results
                    if global_mv_total > 0:
                        global_mv_acc = global_mv_correct / global_mv_total
                        print(f"[Validation] Global majority voting: {global_mv_correct}/{global_mv_total} = {global_mv_acc:.4f}")
                        
                        for ds in sorted(per_ds_mv_total.keys()):
                            ds_acc = per_ds_mv_correct[ds] / per_ds_mv_total[ds] if per_ds_mv_total[ds] > 0 else 0
                            print(f"[Validation] {ds} majority voting: {per_ds_mv_correct[ds]}/{per_ds_mv_total[ds]} = {ds_acc:.4f}")
                        
                        if math500_all_mv_total > 0:
                            math500_all_acc = math500_all_mv_correct / math500_all_mv_total
                            print(f"[Validation] math500_all majority voting: {math500_all_mv_correct}/{math500_all_mv_total} = {math500_all_acc:.4f}")
                    
                    # Compute interval fractions (both global and per-datasource)
                    accuracy_intervals = [(0.0, 0.0)]
                    low = 0.0
                    n_pow = 10
                    while n_pow >= 0:
                        high = 2.0 ** (-n_pow)
                        accuracy_intervals.append((low, high))
                        low = high
                        n_pow -= 1
                    accuracy_intervals.append((1.0, 1.0))
                    
                    def get_interval_label(idx, lo, hi, total_intervals):
                        if idx == 0 or idx == total_intervals - 1:
                            return f"[{lo}, {hi}]"
                        elif idx == total_intervals - 2:
                            return f"({lo}, {hi})"
                        else:
                            return f"({lo}, {hi}]"
                    
                    def compute_interval_fractions(accuracies_list):
                        if not accuracies_list:
                            return {}
                        counts = [0 for _ in accuracy_intervals]
                        for acc in accuracies_list:
                            for idx, (lo, hi) in enumerate(accuracy_intervals):
                                in_interval = False
                                if idx == 0:
                                    in_interval = (acc == 0.0)
                                elif idx == len(accuracy_intervals) - 1:
                                    in_interval = (acc == 1.0)
                                else:
                                    is_second_to_last = (idx == len(accuracy_intervals) - 2)
                                    if is_second_to_last:
                                        in_interval = (acc > lo and acc < hi)
                                    else:
                                        in_interval = (acc > lo and acc <= hi)
                                if in_interval:
                                    counts[idx] += 1
                                    break
                        n = len(accuracies_list)
                        fractions = {}
                        for i, (lo, hi) in enumerate(accuracy_intervals):
                            label = get_interval_label(i, lo, hi, len(accuracy_intervals))
                            fractions[label] = counts[i] / n
                        return fractions
                    
                    # Compute per-datasource and global interval fractions
                    all_prompt_accuracies = []
                    per_ds_prompt_accuracies = defaultdict(list)
                    
                    for ds, prompts in prompt_to_accuracies.items():
                        for pk, accs in prompts.items():
                            if accs:
                                mean_acc = sum(accs) / len(accs)
                                all_prompt_accuracies.append(mean_acc)
                                per_ds_prompt_accuracies[ds].append(mean_acc)
                    
                    if all_prompt_accuracies:
                        # Global interval fractions
                        global_fracs = compute_interval_fractions(all_prompt_accuracies)
                        for label, frac in global_fracs.items():
                            global_interval_counts[label] = frac
                        global_interval_total = 1  # Normalized fractions
                        
                        # Per-datasource interval fractions
                        for ds, ds_accuracies in per_ds_prompt_accuracies.items():
                            ds_fracs = compute_interval_fractions(ds_accuracies)
                            for interval_label, frac in ds_fracs.items():
                                per_ds_interval_counts[ds][f"{ds}/{interval_label}"] = frac
                            per_ds_interval_totals[ds] = 1  # Normalized fractions
                        
                        # Aggregate math500_level1-5 into math500_all
                        math500_all_accuracies = []
                        for ds in per_ds_prompt_accuracies.keys():
                            if any(ds.endswith(f"math500_level{i}") for i in range(1, 6)):
                                math500_all_accuracies.extend(per_ds_prompt_accuracies[ds])
                        
                        if math500_all_accuracies:
                            math500_all_fracs = compute_interval_fractions(math500_all_accuracies)
                            for interval_label, frac in math500_all_fracs.items():
                                per_ds_interval_counts["math500_all"][f"math500_all/{interval_label}"] = frac
                            per_ds_interval_totals["math500_all"] = 1
                            math500_mean_acc = sum(math500_all_accuracies) / len(math500_all_accuracies)
                            print(f"[Validation] math500_all interval fractions computed, mean_accuracy={math500_mean_acc:.4f}, num_prompts={len(math500_all_accuracies)}")
                else:
                    print(f"[Validation] Warning: Missing per-item data for majority voting computation")
                
                # Mark that we've already processed rewards incrementally
                round_processed = True
                print(f"[Validation] All {total_rounds} rounds complete with incremental processing, {len(sample_scores)} total samples")
            else:
                # Original behavior: repeat and generate all at once
                round_processed = False  # Will use the standard reward computation below
                test_batch = test_batch_original.repeat(repeat_times=val_n, interleave=True)
                
                # Save input_ids before pop (since pop removes it from test_batch)
                input_ids = test_batch.batch["input_ids"].clone()
                
                batch_keys_to_pop = ["input_ids", "attention_mask", "position_ids"]
                non_tensor_batch_keys_to_pop = ["raw_prompt_ids"]
                if "multi_modal_data" in test_batch.non_tensor_batch:
                    non_tensor_batch_keys_to_pop.append("multi_modal_data")
                if "raw_prompt" in test_batch.non_tensor_batch:
                    non_tensor_batch_keys_to_pop.append("raw_prompt")
                if "tools_kwargs" in test_batch.non_tensor_batch:
                    non_tensor_batch_keys_to_pop.append("tools_kwargs")
                test_gen_batch = test_batch.pop(
                    batch_keys=batch_keys_to_pop,
                    non_tensor_batch_keys=non_tensor_batch_keys_to_pop,
                )

                test_gen_batch.meta_info = {
                    "eos_token_id": self.tokenizer.eos_token_id,
                    "pad_token_id": self.tokenizer.pad_token_id,
                    "recompute_log_prob": False,
                    "do_sample": self.config.actor_rollout_ref.rollout.val_kwargs.do_sample,
                    "validate": True,
                }
                print(f"test_gen_batch meta info: {test_gen_batch.meta_info}")

                # pad to be divisible by dp_size
                test_gen_batch_padded, pad_size = pad_dataproto_to_divisor(test_gen_batch, self.actor_rollout_wg.world_size)
                if not self.async_rollout_mode:
                    test_output_gen_batch_padded = self.actor_rollout_wg.generate_sequences(test_gen_batch_padded)
                else:
                    self.async_rollout_manager.wake_up()
                    test_output_gen_batch_padded = self.async_rollout_manager.generate_sequences(test_gen_batch_padded)
                    self.async_rollout_manager.sleep()

                # unpad
                test_output_gen_batch = unpad_dataproto(test_output_gen_batch_padded, pad_size=pad_size)
            
            # Skip the rest if rewards were already computed incrementally
            if round_processed:
                print("validation generation end (rewards already computed incrementally)")
                continue
                
            print("validation generation end")
            # TODO: Can we keep special tokens except for padding tokens?
            input_texts = [self.tokenizer.decode(ids, skip_special_tokens=True) for ids in input_ids]
            sample_inputs.extend(input_texts)

            # Store generated outputs
            output_ids = test_output_gen_batch.batch["responses"]
            output_texts = [self.tokenizer.decode(ids, skip_special_tokens=True) for ids in output_ids]
            sample_outputs.extend(output_texts)

            test_batch = test_batch.union(test_output_gen_batch)

            # evaluate using reward_function
            test_batch.meta_info["validate"] = True  # Enable majority voting calculation
            result = self.val_reward_fn(test_batch, return_dict=True)
            reward_tensor = result["reward_tensor"]
            scores = reward_tensor.sum(-1).cpu().tolist()
            sample_scores.extend(scores)

            reward_extra_infos_dict["reward"].extend(scores)
            print(f"len reward_extra_infos_dict['reward']: {len(reward_extra_infos_dict['reward'])}")
            if "reward_extra_info" in result:
                for key, lst in result["reward_extra_info"].items():
                    reward_extra_infos_dict[key].extend(lst)
                    print(f"len reward_extra_infos_dict['{key}']: {len(reward_extra_infos_dict[key])}")

            batch_data_sources = test_batch.non_tensor_batch.get(
                "data_source", np.array(["unknown"] * reward_tensor.shape[0])
            )
            data_source_lst.append(batch_data_sources)

            unique_ds, ds_counts = np.unique(batch_data_sources, return_counts=True)
            batch_ds_counts = dict(zip(unique_ds.tolist(), ds_counts.tolist()))

            if "accuracy_interval_fractions_per_prompt_global" in result:
                batch_fracs = result["accuracy_interval_fractions_per_prompt_global"]
                batch_size = reward_tensor.shape[0]

                for k, v in batch_fracs.items():
                    global_interval_counts[k] += float(v) * batch_size

                global_interval_total += batch_size

            if "accuracy_interval_fractions_per_prompt_per_datasource" in result:
                batch_fracs = result["accuracy_interval_fractions_per_prompt_per_datasource"]

                # Track which datasources we've already counted for this batch
                ds_counted_this_batch = set()

                for interval_label, v in batch_fracs.items():
                    ds = interval_label.split("/")[0]
                    ds_batch_size = int(batch_ds_counts.get(ds, 0))

                    per_ds_interval_counts[ds][interval_label] += float(v) * ds_batch_size

                    # Only add to totals once per datasource per batch
                    if ds not in ds_counted_this_batch:
                        per_ds_interval_totals[ds] += ds_batch_size
                        ds_counted_this_batch.add(ds)

            # Aggregate majority voting metrics if available
            if "majority_vote_accuracy_global" in result:
                batch_mv_acc = float(result["majority_vote_accuracy_global"])
                batch_mv_n = int(result.get("majority_vote_num_prompts_global", 0))
                # fallback to batch size if counts are missing
                if batch_mv_n <= 0:
                    batch_mv_n = int(reward_tensor.shape[0])
                    
                global_mv_correct += batch_mv_acc * batch_mv_n
                global_mv_total += batch_mv_n

            if "majority_vote_accuracy_per_datasource" in result:
                batch_ds_mv_acc = result["majority_vote_accuracy_per_datasource"]
                batch_ds_mv_n = result.get("majority_vote_num_prompts_per_datasource", {})

                for ds, acc in batch_ds_mv_acc.items():
                    n = int(batch_ds_mv_n.get(ds, 0))
                    if n <= 0:
                        # fallback: examples-based weight (not ideal, but keeps it minimal)
                        n = int(batch_ds_counts.get(ds, 0))

                    per_ds_mv_correct[ds] += float(acc) * n
                    per_ds_mv_total[ds] += n

        self._maybe_log_val_generations(inputs=sample_inputs, outputs=sample_outputs, scores=sample_scores)

        # dump generations
        val_data_dir = self.config.trainer.get("validation_data_dir", None)
        if val_data_dir:
            self._dump_generations(
                inputs=sample_inputs,
                outputs=sample_outputs,
                scores=sample_scores,
                reward_extra_infos_dict=reward_extra_infos_dict,
                dump_path=val_data_dir,
            )

        if global_interval_total > 0:
            global_interval_fractions = {
                k: c / global_interval_total for k, c in global_interval_counts.items()
            }

        # finalize aggregated per-datasource fractions
        if per_ds_interval_totals:
            per_ds_interval_fractions = {}
            for ds, counts in per_ds_interval_counts.items():
                denom = per_ds_interval_totals[ds]
                if denom == 0:
                    continue
                for interval_label, c in counts.items():
                    per_ds_interval_fractions[interval_label] = c / denom

        for key_info, lst in reward_extra_infos_dict.items():
            assert len(lst) == 0 or len(lst) == len(sample_scores), f"{key_info}: {len(lst)=}, {len(sample_scores)=}"

        data_sources = np.concatenate(data_source_lst, axis=0)

        unique_ds, ds_counts = np.unique(data_sources, return_counts=True)
        num_examples_per_ds = dict(zip(unique_ds.tolist(), ds_counts.tolist()))

        data_src2var2metric2val = process_validation_metrics(data_sources, sample_inputs, reward_extra_infos_dict)

        # =================================================================
        # Special patch: Aggregate math500_level1-5 into math500_all
        # =================================================================
        # Match data sources that end with math500_level1-5 (handles both "math500_level1" and "guanning-ai/math500_level1")
        math500_level_suffixes = {f"math500_level{i}" for i in range(1, 6)}
        found_levels = {ds for ds in set(data_sources) if any(ds.endswith(suffix) for suffix in math500_level_suffixes)}
        if found_levels:
            mask = np.isin(data_sources, list(found_levels))
            math500_all_result = process_validation_metrics(
                np.array(["math500_all"] * mask.sum()),
                [sample_inputs[i] for i in np.where(mask)[0]],
                {k: [v[i] for i in np.where(mask)[0]] for k, v in reward_extra_infos_dict.items() if v},
            )
            data_src2var2metric2val.update(math500_all_result)
            print(f"[Validation] math500_all: {mask.sum()} samples from {len(found_levels)} levels")
            print(f"[Validation] math500_all metrics: {list(math500_all_result.get('math500_all', {}).keys())}")
        metric_dict = {}
        for data_source, var2metric2val in data_src2var2metric2val.items():
            core_var = "acc" if "acc" in var2metric2val else "reward"
            for var_name, metric2val in var2metric2val.items():
                n_max = max([int(name.split("@")[-1].split("/")[0]) for name in metric2val.keys()])

                for metric_name, metric_val in metric2val.items():
                    if var_name == core_var and (f"@{n_max}" in metric_name):
                        if metric_name.startswith("mean"): 
                            metric_sec = "mean_accuracies"
                        
                        elif metric_name.startswith("best") and "std" not in metric_name:
                            metric_sec = f"pass@{n_max}_accuracies"

                        else:
                            metric_sec = "val-core"
                            
                    else:
                        metric_sec = "val-aux"

                    pfx = f"{metric_sec}/{data_source}/{var_name}/{metric_name}"
                    metric_dict[pfx] = metric_val

        if global_interval_fractions is not None:
            assert isinstance(global_interval_fractions, dict)
            for interval_label, fraction in global_interval_fractions.items():
                metric_dict[
                    f"validation_all_datasets_binning/fraction_of_prompts_in_{interval_label}"
                ] = fraction

        if per_ds_interval_fractions is not None:
            assert isinstance(per_ds_interval_fractions, dict)

            for interval_label, fraction in per_ds_interval_fractions.items():
                ds = interval_label.split("/")[0]
                interval_value = interval_label.split("/")[-1]

                metric_name = f"validation_binning_for_dataset_{ds}/fraction_of_prompts_in_{interval_value}"
                metric_dict[metric_name] = fraction

            # Aggregate math500_level1-5 binning into math500_all
            if found_levels:
                math500_binning_counts = defaultdict(float)
                math500_binning_total = 0
                
                for lvl in found_levels:
                    ds_batch_size = per_ds_interval_totals.get(lvl, 0)
                    math500_binning_total += ds_batch_size  # Only add once per level
                    
                    for interval_label, fraction in per_ds_interval_fractions.items():
                        if interval_label.startswith(f"{lvl}/"):
                            interval_value = interval_label.split("/")[-1]
                            math500_binning_counts[interval_value] += fraction * ds_batch_size
                
                if math500_binning_total > 0:
                    for interval_value, count in math500_binning_counts.items():
                        fraction = count / math500_binning_total
                        metric_dict[
                            f"validation_binning_for_dataset_math500_all/fraction_of_prompts_in_{interval_value}"
                        ] = fraction

        for ds, n in num_examples_per_ds.items():
            metric_dict[f"validation_num_examples/{ds}"] = int(n)

        metric_dict["validation_num_examples/all"] = int(len(data_sources))

        # -------- majority vote accuracy final metrics --------
        if global_mv_total > 0:
            metric_dict[
                f"validation_majority_vote_accuracy/global/majority@{self.config.actor_rollout_ref.rollout.val_kwargs.n}"
            ] = global_mv_correct / global_mv_total

        for ds, tot in per_ds_mv_total.items():
            if tot > 0:
                metric_dict[
                    f"validation_majority_vote_accuracy/{ds}/majority@{self.config.actor_rollout_ref.rollout.val_kwargs.n}"
                ] = per_ds_mv_correct[ds] / tot

        return metric_dict

    def init_workers(self):
        """Initialize distributed training workers using Ray backend.

        Creates:
        1. Ray resource pools from configuration
        2. Worker groups for each role (actor, critic, etc.)
        """
        self.resource_pool_manager.create_resource_pool()

        self.resource_pool_to_cls = {pool: {} for pool in self.resource_pool_manager.resource_pool_dict.values()}

        # create actor and rollout
        if self.hybrid_engine:
            resource_pool = self.resource_pool_manager.get_resource_pool(Role.ActorRollout)
            actor_rollout_cls = RayClassWithInitArgs(
                cls=self.role_worker_mapping[Role.ActorRollout],
                config=self.config.actor_rollout_ref,
                role="actor_rollout",
            )
            self.resource_pool_to_cls[resource_pool]["actor_rollout"] = actor_rollout_cls
        else:
            raise NotImplementedError

        # create critic
        if self.use_critic:
            resource_pool = self.resource_pool_manager.get_resource_pool(Role.Critic)
            critic_cls = RayClassWithInitArgs(cls=self.role_worker_mapping[Role.Critic], config=self.config.critic)
            self.resource_pool_to_cls[resource_pool]["critic"] = critic_cls

        # create reference policy if needed
        if self.use_reference_policy:
            resource_pool = self.resource_pool_manager.get_resource_pool(Role.RefPolicy)
            ref_policy_cls = RayClassWithInitArgs(self.role_worker_mapping[Role.RefPolicy], config=self.config.actor_rollout_ref, role="ref")
            self.resource_pool_to_cls[resource_pool]["ref"] = ref_policy_cls

        # create a reward model if reward_fn is None
        if self.use_rm:
            # we create a RM here
            resource_pool = self.resource_pool_manager.get_resource_pool(Role.RewardModel)
            rm_cls = RayClassWithInitArgs(self.role_worker_mapping[Role.RewardModel], config=self.config.reward_model)
            self.resource_pool_to_cls[resource_pool]["rm"] = rm_cls

        # initialize WorkerGroup
        # NOTE: if you want to use a different resource pool for each role, which can support different parallel size,
        # you should not use `create_colocated_worker_cls`.
        # Instead, directly pass different resource pool to different worker groups.
        # See https://github.com/volcengine/verl/blob/master/examples/ray/tutorial.ipynb for more information.
        all_wg = {}
        wg_kwargs = {}  # Setting up kwargs for RayWorkerGroup
        if OmegaConf.select(self.config.trainer, "ray_wait_register_center_timeout") is not None:
            wg_kwargs["ray_wait_register_center_timeout"] = self.config.trainer.ray_wait_register_center_timeout
        if OmegaConf.select(self.config.trainer, "profile_steps") is not None:
            wg_kwargs["profile_steps"] = OmegaConf.select(self.config.trainer, "profile_steps")
            assert OmegaConf.select(self.config.trainer, "worker_nsight_options") is not None, "worker_nsight_options must be set when profile_steps is set"
            wg_kwargs["worker_nsight_options"] = OmegaConf.to_container(OmegaConf.select(self.config.trainer, "worker_nsight_options"))

        for resource_pool, class_dict in self.resource_pool_to_cls.items():
            worker_dict_cls = create_colocated_worker_cls(class_dict=class_dict)
            wg_dict = self.ray_worker_group_cls(resource_pool=resource_pool, ray_cls_with_init=worker_dict_cls, device_name=self.device_name, **wg_kwargs)
            spawn_wg = wg_dict.spawn(prefix_set=class_dict.keys())
            all_wg.update(spawn_wg)

        if self.use_critic:
            self.critic_wg = all_wg["critic"]
            self.critic_wg.init_model()

        if self.use_reference_policy and not self.ref_in_actor:
            self.ref_policy_wg = all_wg["ref"]
            self.ref_policy_wg.init_model()

        if self.use_rm:
            self.rm_wg = all_wg["rm"]
            self.rm_wg.init_model()

        # we should create rollout at the end so that vllm can have a better estimation of kv cache memory
        self.actor_rollout_wg = all_wg["actor_rollout"]
        self.actor_rollout_wg.init_model()

        # create async rollout manager and request scheduler
        self.async_rollout_mode = False
        if self.config.actor_rollout_ref.rollout.mode == "async":
            from verl.workers.rollout.async_server import AsyncLLMServerManager

            self.async_rollout_mode = True
            self.async_rollout_manager = AsyncLLMServerManager(
                config=self.config,
                worker_group=self.actor_rollout_wg,
            )

    def _save_checkpoint_helper(
        self,
        default_local_dir,
        actor_remote_path,
        critic_remote_path,
        max_actor_ckpt_to_keep,
        max_critic_ckpt_to_keep,
    ) -> None:
        # path: given_path + `/global_step_{global_steps}` + `/actor`
        local_global_step_folder = os.path.join(default_local_dir, f"global_step_{self.global_steps}")
        print(f"local_global_step_folder: {local_global_step_folder}")
        
        actor_local_path = os.path.join(local_global_step_folder, "actor")

        self.actor_rollout_wg.save_checkpoint(actor_local_path, actor_remote_path, self.global_steps, max_ckpt_to_keep=max_actor_ckpt_to_keep)

        if self.use_critic:
            critic_local_path = os.path.join(local_global_step_folder, "critic")
            self.critic_wg.save_checkpoint(critic_local_path, critic_remote_path, self.global_steps, max_ckpt_to_keep=max_critic_ckpt_to_keep)

        # save dataloader
        BaseCheckpointManager.local_mkdir(local_global_step_folder)
        dataloader_local_path = os.path.join(local_global_step_folder, "data.pt")
        dataloader_state_dict = self.train_dataloader.state_dict()
        torch.save(dataloader_state_dict, dataloader_local_path)

        # latest checkpointed iteration tracker (for atomic usage)
        local_latest_checkpointed_iteration = os.path.join(
            default_local_dir, 
            "latest_checkpointed_iteration.txt",
        )
        with open(local_latest_checkpointed_iteration, "w") as f:
            f.write(str(self.global_steps))

        # wandb id
        wandb_id_save_path = os.path.join(
            default_local_dir,
            "wandb_id.txt",
        )

        with open(wandb_id_save_path, "w") as f:
            f.write(str(self.wandb_id))

    def _save_checkpoint(self):
        actor_remote_path = (
            None 
            if self.config.trainer.default_hdfs_dir is None 
            else os.path.join(self.config.trainer.default_hdfs_dir, f"global_step_{self.global_steps}", "actor")
        )

        if self.use_critic:
            critic_remote_path = (
                None 
                if self.config.trainer.default_hdfs_dir is None 
                else os.path.join(self.config.trainer.default_hdfs_dir, f"global_step_{self.global_steps}", "critic")
            )

        else:
            critic_remote_path = None

        remove_previous_ckpt_in_save = self.config.trainer.get("remove_previous_ckpt_in_save", False)
        if remove_previous_ckpt_in_save:
            print("Warning: remove_previous_ckpt_in_save is deprecated," + " set max_actor_ckpt_to_keep=1 and max_critic_ckpt_to_keep=1 instead")

        max_actor_ckpt_to_keep = self.config.trainer.get("max_actor_ckpt_to_keep", None) if not remove_previous_ckpt_in_save else 1
        max_critic_ckpt_to_keep = self.config.trainer.get("max_critic_ckpt_to_keep", None) if not remove_previous_ckpt_in_save else 1

        self._save_checkpoint_helper(
            default_local_dir=self.config.trainer.default_local_dir,
            actor_remote_path=actor_remote_path,
            critic_remote_path=critic_remote_path,
            max_actor_ckpt_to_keep=max_actor_ckpt_to_keep,
            max_critic_ckpt_to_keep=max_critic_ckpt_to_keep,
        )

    def _load_dataloader(
        self,
        dataloader_local_path: str,
    ):
        if os.path.exists(dataloader_local_path):
            dataloader_state_dict = torch.load(dataloader_local_path, weights_only=False)
            self.train_dataloader.load_state_dict(dataloader_state_dict)
        else:
            print(f"Warning: No dataloader state found at {dataloader_local_path}, will start from scratch")

    def _load_checkpoint(self):
        if self.config.trainer.resume_mode == "disable":
            return 0

        # load from hdfs
        if self.config.trainer.default_hdfs_dir is not None:
            raise NotImplementedError("load from hdfs is not implemented yet")
        else:
            checkpoint_folder = self.config.trainer.default_local_dir  # TODO: check path
            if not os.path.isabs(checkpoint_folder):
                working_dir = os.getcwd()
                checkpoint_folder = os.path.join(working_dir, checkpoint_folder)
            global_step_folder = find_latest_ckpt_path(checkpoint_folder)  # None if no latest

        # find global_step_folder
        if self.config.trainer.resume_mode == "auto":
            if global_step_folder is None:
                print("Training from scratch")

                dataloader_local_path = self.config.resume_training_parameters.dataloader_local_path

                if isinstance(dataloader_local_path, str):
                    if not os.path.exists(dataloader_local_path):
                        raise ValueError(
                            f"data loader local path, {dataloader_local_path}, "
                            f"is provided, but it is not valid!"
                        )
                    
                    else:
                        self._load_dataloader(
                            dataloader_local_path=dataloader_local_path,
                        )

                return 0
            
        else:
            if self.config.trainer.resume_mode == "resume_path":
                assert isinstance(self.config.trainer.resume_from_path, str), "resume ckpt must be str type"
                assert "global_step_" in self.config.trainer.resume_from_path, "resume ckpt must specify the global_steps"
                global_step_folder = self.config.trainer.resume_from_path

                if not os.path.isabs(global_step_folder):
                    working_dir = os.getcwd()
                    global_step_folder = os.path.join(working_dir, global_step_folder)

        print(f"Load from checkpoint folder: {global_step_folder}")
        # set global step
        self.global_steps = int(global_step_folder.split("global_step_")[-1])

        print(f"Setting global step to {self.global_steps}")
        print(f"Resuming from {global_step_folder}")

        actor_path = os.path.join(global_step_folder, "actor")
        critic_path = os.path.join(global_step_folder, "critic")
        # load actor
        self.actor_rollout_wg.load_checkpoint(actor_path, del_local_after_load=self.config.trainer.del_local_ckpt_after_load)
        # load critic
        if self.use_critic:
            self.critic_wg.load_checkpoint(critic_path, del_local_after_load=self.config.trainer.del_local_ckpt_after_load)

        # load dataloader,
        # TODO: from remote not implemented yet
        dataloader_local_path = os.path.join(global_step_folder, "data.pt")
        self._load_dataloader(dataloader_local_path=dataloader_local_path)

        # Load wandb id
        wandb_id_save_path = os.path.join(
            checkpoint_folder,
            "wandb_id.txt",
        )

        if os.path.exists(wandb_id_save_path):
            print("Previous WANDB id is provided!")
            with open(wandb_id_save_path, "r") as f:
                self.wandb_id = f.read().strip()

            print("WANDB Run ID loaded: ", self.wandb_id)

        else:
            print("No WANDB run ID is provided.")
            self.wandb_id = None

    def _balance_batch(self, batch: DataProto, metrics, logging_prefix="global_seqlen"):
        """Reorder the data on single controller such that each dp rank gets similar total tokens"""
        attention_mask = batch.batch["attention_mask"]
        batch_size = attention_mask.shape[0]
        global_seqlen_lst = batch.batch["attention_mask"].view(batch_size, -1).sum(-1).tolist()  # (train_batch_size,)
        world_size = self.actor_rollout_wg.world_size
        global_partition_lst = get_seqlen_balanced_partitions(global_seqlen_lst, k_partitions=world_size, equal_size=True)
        # reorder based on index. The data will be automatically equally partitioned by dispatch function
        global_idx = torch.tensor([j for partition in global_partition_lst for j in partition])
        batch.reorder(global_idx)
        global_balance_stats = log_seqlen_unbalance(seqlen_list=global_seqlen_lst, partitions=global_partition_lst, prefix=logging_prefix)
        metrics.update(global_balance_stats)

    def fit(self):
        """
        The training loop of PPO.
        The driver process only need to call the compute functions of the worker group through RPC
        to construct the PPO dataflow.
        The light-weight advantage computation is done on the driver process.
        """
        from omegaconf import OmegaConf

        from verl.utils.tracking import Tracking

        # load checkpoint before doing anything
        self.global_steps = 0
        self._load_checkpoint()

        # see if there is a custom global steps from which we want to restart training
        if isinstance(self.config.resume_training_parameters.resume_global_steps, int):
            self.global_steps = self.config.resume_training_parameters.resume_global_steps

        if isinstance(self.config.resume_training_parameters.wandb_id_to_resume, str):
            self.wandb_id = self.config.resume_training_parameters.wandb_id_to_resume

        # NOTE: for now, we just force wandb logging in a new run
        self.wandb_id = None

        # Setup logging
        logger = Tracking(
            project_name=self.config.trainer.project_name,
            experiment_name=self.config.trainer.experiment_name,
            default_backend=self.config.trainer.logger,
            previous_run_id=self.wandb_id,
            config=OmegaConf.to_container(self.config, resolve=True),
        )

        if self.wandb_id is None:
            self.wandb_id = logger.wandb_id
            print("Wandb new run initialized since we are training from scratch.")
            print("Wandb ID: ", self.wandb_id)

        # perform validation before training
        # currently, we only support validation using the reward_function.
        if self.val_reward_fn is not None and self.config.trainer.get("val_before_train", True):
            val_metrics = self._validate()
            assert val_metrics, f"{val_metrics=}"
            pprint(f"Initial validation metrics: {val_metrics}")
            logger.log(data=val_metrics, step=self.global_steps)
            if self.config.trainer.get("val_only", False):
                return

        # add tqdm
        progress_bar = tqdm(total=self.total_training_steps, initial=self.global_steps, desc="Training Progress")

        # we start from step 1
        self.global_steps += 1
        last_val_metrics = None

        for epoch in range(self.config.trainer.total_epochs):
            for batch_dict in self.train_dataloader:
                do_profile = self.global_steps in self.config.trainer.profile_steps if self.config.trainer.profile_steps is not None else False
                if do_profile:
                    self.actor_rollout_wg.start_profile()
                    if self.use_reference_policy:
                        self.ref_policy_wg.start_profile()
                    if self.use_critic:
                        self.critic_wg.start_profile()
                    if self.use_rm:
                        self.rm_wg.start_profile()

                metrics = {}
                timing_raw = {}
                batch: DataProto = DataProto.from_single_dict(batch_dict)

                # pop those keys for generation
                batch_keys_to_pop = ["input_ids", "attention_mask", "position_ids"]
                non_tensor_batch_keys_to_pop = ["raw_prompt_ids"]
                if "multi_modal_data" in batch.non_tensor_batch:
                    non_tensor_batch_keys_to_pop.append("multi_modal_data")
                if "raw_prompt" in batch.non_tensor_batch:
                    non_tensor_batch_keys_to_pop.append("raw_prompt")
                if "tools_kwargs" in batch.non_tensor_batch:
                    non_tensor_batch_keys_to_pop.append("tools_kwargs")
                gen_batch = batch.pop(
                    batch_keys=batch_keys_to_pop,
                    non_tensor_batch_keys=non_tensor_batch_keys_to_pop,
                )

                is_last_step = self.global_steps >= self.total_training_steps

                with marked_timer("step", timing_raw):
                    # generate a batch
                    with marked_timer("gen", timing_raw, color="red"):
                        if not self.async_rollout_mode:
                            gen_batch_output = self.actor_rollout_wg.generate_sequences(gen_batch)
                        else:
                            self.async_rollout_manager.wake_up()
                            gen_batch_output = self.async_rollout_manager.generate_sequences(gen_batch)
                            self.async_rollout_manager.sleep()
                        timing_raw.update(gen_batch_output.meta_info["timing"])
                        gen_batch_output.meta_info.pop("timing", None)

                    if self.config.algorithm.adv_estimator in (AdvantageEstimator.REMAX, AdvantageEstimator.SELF_PAPER):
                        with marked_timer("gen_max", timing_raw, color="purple"):
                            gen_baseline_batch = deepcopy(gen_batch)
                            gen_baseline_batch.meta_info["do_sample"] = False
                            gen_baseline_output = self.actor_rollout_wg.generate_sequences(gen_baseline_batch)

                            batch = batch.union(gen_baseline_output)
                            reward_baseline_tensor = self.reward_fn(batch)
                            reward_baseline_tensor = reward_baseline_tensor.sum(dim=-1)

                            batch.pop(batch_keys=list(gen_baseline_output.batch.keys()))

                            batch.batch["reward_baselines"] = reward_baseline_tensor

                            del gen_baseline_batch, gen_baseline_output

                    batch.non_tensor_batch["uid"] = np.array([str(uuid.uuid4()) for _ in range(len(batch.batch))], dtype=object)
                    # repeat to align with repeated responses in rollout
                    batch = batch.repeat(repeat_times=self.config.actor_rollout_ref.rollout.n, interleave=True)
                    batch = batch.union(gen_batch_output)

                    batch.batch["response_mask"] = compute_response_mask(batch)
                    # Balance the number of valid tokens across DP ranks.
                    # NOTE: This usually changes the order of data in the `batch`,
                    # which won't affect the advantage calculation (since it's based on uid),
                    # but might affect the loss calculation (due to the change of mini-batching).
                    # TODO: Decouple the DP balancing and mini-batching.
                    if self.config.trainer.balance_batch:
                        self._balance_batch(batch, metrics=metrics)

                    # compute global_valid tokens
                    batch.meta_info["global_token_num"] = torch.sum(batch.batch["attention_mask"], dim=-1).tolist()

                    with marked_timer("reward", timing_raw, color="yellow"):
                        # compute reward model score
                        if self.use_rm:
                            reward_tensor = self.rm_wg.compute_rm_score(batch)
                            batch = batch.union(reward_tensor)

                        if self.config.reward_model.launch_reward_fn_async:
                            future_reward = compute_reward_async.remote(batch, self.config, self.tokenizer)
                        else:
                            reward_tensor, reward_extra_infos_dict = compute_reward(batch, self.reward_fn)

                    # recompute old_log_probs
                    with marked_timer("old_log_prob", timing_raw, color="blue"):
                        old_log_prob = self.actor_rollout_wg.compute_log_prob(batch)
                        entropys = old_log_prob.batch["entropys"]
                        response_masks = batch.batch["response_mask"]
                        loss_agg_mode = self.config.actor_rollout_ref.actor.loss_agg_mode
                        entropy_agg = agg_loss(loss_mat=entropys, loss_mask=response_masks, loss_agg_mode=loss_agg_mode)
                        old_log_prob_metrics = {"actor/entropy": entropy_agg.detach().item()}
                        metrics.update(old_log_prob_metrics)
                        old_log_prob.batch.pop("entropys")
                        batch = batch.union(old_log_prob)

                        if "rollout_log_probs" in batch.batch.keys():
                            # TODO: we may want to add diff of probs too.
                            rollout_old_log_probs = batch.batch["rollout_log_probs"]
                            actor_old_log_probs = batch.batch["old_log_probs"]
                            attention_mask = batch.batch["attention_mask"]
                            responses = batch.batch["responses"]
                            response_length = responses.size(1)
                            response_mask = attention_mask[:, -response_length:]

                            rollout_probs = torch.exp(rollout_old_log_probs)
                            actor_probs = torch.exp(actor_old_log_probs)
                            rollout_probs_diff = torch.abs(rollout_probs - actor_probs)
                            rollout_probs_diff = torch.masked_select(rollout_probs_diff, response_mask.bool())
                            rollout_probs_diff_max = torch.max(rollout_probs_diff)
                            rollout_probs_diff_mean = torch.mean(rollout_probs_diff)
                            rollout_probs_diff_std = torch.std(rollout_probs_diff)
                            metrics.update(
                                {
                                    "training/rollout_probs_diff_max": rollout_probs_diff_max.detach().item(),
                                    "training/rollout_probs_diff_mean": rollout_probs_diff_mean.detach().item(),
                                    "training/rollout_probs_diff_std": rollout_probs_diff_std.detach().item(),
                                }
                            )

                    if self.use_reference_policy:
                        # compute reference log_prob
                        with marked_timer("ref", timing_raw, color="olive"):
                            if not self.ref_in_actor:
                                ref_log_prob = self.ref_policy_wg.compute_ref_log_prob(batch)
                            else:
                                ref_log_prob = self.actor_rollout_wg.compute_ref_log_prob(batch)
                            batch = batch.union(ref_log_prob)

                    # compute values
                    if self.use_critic:
                        with marked_timer("values", timing_raw, color="cyan"):
                            values = self.critic_wg.compute_values(batch)
                            batch = batch.union(values)

                    with marked_timer("adv", timing_raw, color="brown"):
                        # we combine with rule-based rm
                        reward_extra_infos_dict: dict[str, list]
                        if self.config.reward_model.launch_reward_fn_async:
                            reward_tensor, reward_extra_infos_dict = ray.get(future_reward)
                        batch.batch["token_level_scores"] = reward_tensor

                        accuracy_interval_fractions_per_prompt_global = None
                        accuracy_interval_fractions_per_prompt_per_datasource = None

                        if reward_extra_infos_dict:
                            accuracy_interval_fractions_per_prompt_global = reward_extra_infos_dict.pop(
                                "accuracy_interval_fractions_per_prompt_global",
                                None,
                            )

                            accuracy_interval_fractions_per_prompt_per_datasource = reward_extra_infos_dict.pop(
                                "accuracy_interval_fractions_per_prompt_per_datasource",
                                None,
                            )

                            # only log during validation
                            reward_extra_infos_dict.pop(
                                "majority_vote_accuracy_global",
                                None,
                            )

                            # only log during validation
                            reward_extra_infos_dict.pop(
                                "majority_vote_accuracy_per_datasource",
                                None,
                            )

                            batch.non_tensor_batch.update({k: np.array(v) for k, v in reward_extra_infos_dict.items()})

                        # Log training data accuracy bins if available
                        train_data_accuracy_bins = {}
                        if isinstance(accuracy_interval_fractions_per_prompt_global, dict):
                            for interval_label, fraction in accuracy_interval_fractions_per_prompt_global.items():
                                train_data_accuracy_bins[
                                    f"train_all_datasets_binning/fraction_of_prompts_in_{interval_label}"
                                ] = fraction

                        if isinstance(accuracy_interval_fractions_per_prompt_per_datasource, dict):
                            for interval_label, fraction in accuracy_interval_fractions_per_prompt_per_datasource.items():
                                ds = interval_label.split("/")[0]
                                interval_value = interval_label.split("/")[-1]

                                binning_metric_name = f"train_binning_for_dataset_{ds}/fraction_of_prompts_in_{interval_value}"
                                train_data_accuracy_bins[binning_metric_name] = fraction

                        metrics.update(train_data_accuracy_bins)

                        # compute rewards. apply_kl_penalty if available
                        if self.config.algorithm.use_kl_in_reward:
                            batch, kl_metrics = apply_kl_penalty(batch, kl_ctrl=self.kl_ctrl_in_reward, kl_penalty=self.config.algorithm.kl_penalty)
                            metrics.update(kl_metrics)
                        else:
                            batch.batch["token_level_rewards"] = batch.batch["token_level_scores"]

                        # compute advantages, executed on the driver process

                        norm_adv_by_std_in_grpo = self.config.algorithm.get("norm_adv_by_std_in_grpo", True)  # GRPO adv normalization factor

                        batch = compute_advantage(
                            batch,
                            adv_estimator=self.config.algorithm.adv_estimator,
                            gamma=self.config.algorithm.gamma,
                            lam=self.config.algorithm.lam,
                            num_repeat=self.config.actor_rollout_ref.rollout.n,
                            norm_adv_by_std_in_grpo=norm_adv_by_std_in_grpo,
                            multi_turn=self.config.actor_rollout_ref.rollout.multi_turn.enable,
                            config=self.config.algorithm,
                        )

                    # update critic
                    if self.use_critic:
                        with marked_timer("update_critic", timing_raw, color="pink"):
                            critic_output = self.critic_wg.update_critic(batch)
                        critic_output_metrics = reduce_metrics(critic_output.meta_info["metrics"])
                        metrics.update(critic_output_metrics)

                    # implement critic warmup
                    if self.config.trainer.critic_warmup <= self.global_steps:
                        # update actor
                        with marked_timer("update_actor", timing_raw, color="red"):
                            batch.meta_info["multi_turn"] = self.config.actor_rollout_ref.rollout.multi_turn.enable
                            actor_output = self.actor_rollout_wg.update_actor(batch)
                        actor_output_metrics = reduce_metrics(actor_output.meta_info["metrics"])
                        metrics.update(actor_output_metrics)
                        
                        # Calculate RPC coordination overhead
                        update_actor_total_ms = timing_raw.get("update_actor", 0) * 1000
                        # Sum up all worker-side timing components
                        worker_timing_keys = [k for k in actor_output_metrics.keys() if k.startswith("timing_distributed_ms/")]
                        worker_total_ms = sum(actor_output_metrics.get(k, 0) for k in worker_timing_keys)
                        rpc_overhead_ms = update_actor_total_ms - worker_total_ms
                        metrics["timing_distributed_ms/rpc_coordination"] = rpc_overhead_ms

                        # Compute gradient statistics from optimizer state (if enabled)
                        if self.config.trainer.get("log_gradient_statistics", False):
                            with marked_timer("gradient_estimator", timing_raw, color="orange"):
                                step_data = DataProto(meta_info={"step": self.global_steps})
                                gradient_estimator_output = self.actor_rollout_wg.compute_gradient_estimator(step_data)
                                gradient_estimator_metrics = reduce_metrics(gradient_estimator_output.meta_info.get("gradient_estimator", {}))
                                prefixed_metrics = {f"gradient/{k}": v for k, v in gradient_estimator_metrics.items()}
                                metrics.update(prefixed_metrics)

                        # diagnostics checkpoint saving based on actor grad norm
                        if (
                            self.config.diagnostics.grad_norm_threshold_for_saving_checkpoint is not None
                            and isinstance(self.config.diagnostics.checkpoint_dir, str)
                        ):
                            grad_norm_threshold = self.config.diagnostics.grad_norm_threshold_for_saving_checkpoint
                            curr_grad_norm = metrics["actor/grad_norm"]

                            if curr_grad_norm > grad_norm_threshold:
                                print("Gradient Norm Threshold: ", grad_norm_threshold)
                                print("Current gradient norm: ", curr_grad_norm)
                                print("Saving a checkpoint for debugging purposes....")

                                self._save_checkpoint_helper(
                                    default_local_dir=self.config.diagnostics.checkpoint_dir,
                                    actor_remote_path=None,
                                    critic_remote_path=None,
                                    max_actor_ckpt_to_keep=None,
                                    max_critic_ckpt_to_keep=None,
                                )

                    # Log rollout generations if enabled
                    rollout_data_dir = self.config.trainer.get("rollout_data_dir", None)
                    if rollout_data_dir:
                        with marked_timer("dump_rollout_generations", timing_raw, color="green"):
                            print(batch.batch.keys())
                            inputs = self.tokenizer.batch_decode(batch.batch["prompts"], skip_special_tokens=True)
                            outputs = self.tokenizer.batch_decode(batch.batch["responses"], skip_special_tokens=True)
                            scores = batch.batch["token_level_scores"].sum(-1).cpu().tolist()
                            self._dump_generations(
                                inputs=inputs,
                                outputs=outputs,
                                scores=scores,
                                reward_extra_infos_dict=reward_extra_infos_dict,
                                dump_path=rollout_data_dir,
                            )

                    # validate
                    validate_on_last_step = (
                        is_last_step
                        and self.config.trainer.get("val_on_last_step", True)
                    )

                    if (
                        self.val_reward_fn is not None 
                        and self.config.trainer.test_freq > 0 
                        and (
                            validate_on_last_step
                            or self.global_steps % self.config.trainer.test_freq == 0
                        )
                    ):
                        with marked_timer("testing", timing_raw, color="green"):
                            val_metrics: dict = self._validate()
                            if is_last_step:
                                last_val_metrics = val_metrics
                        metrics.update(val_metrics)

                    if self.config.trainer.save_freq > 0 and (is_last_step or self.global_steps % self.config.trainer.save_freq == 0):
                        with marked_timer("save_checkpoint", timing_raw, color="green"):
                            self._save_checkpoint()

                # training metrics
                metrics.update(
                    {
                        "training/global_step": self.global_steps,
                        "training/epoch": epoch,
                    }
                )
                # collect metrics
                metrics.update(compute_data_metrics(batch=batch, use_critic=self.use_critic))
                metrics.update(compute_timing_metrics(batch=batch, timing_raw=timing_raw))
                # TODO: implement actual tflpo and theoretical tflpo
                n_gpus = self.resource_pool_manager.get_n_gpus()
                metrics.update(compute_throughout_metrics(batch=batch, timing_raw=timing_raw, n_gpus=n_gpus))

                # TODO: make a canonical logger that supports various backend
                logger.log(data=metrics, step=self.global_steps)

                progress_bar.update(1)
                self.global_steps += 1

                if do_profile:
                    self.actor_rollout_wg.stop_profile()
                    if self.use_reference_policy:
                        self.ref_policy_wg.stop_profile()
                    if self.use_critic:
                        self.critic_wg.stop_profile()
                    if self.use_rm:
                        self.rm_wg.stop_profile()

                if is_last_step:
                    pprint(f"Final validation metrics: {last_val_metrics}")
                    progress_bar.close()
                    return
