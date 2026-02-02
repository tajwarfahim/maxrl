import os
import uuid
from pprint import pprint
from typing import Type

import numpy as np
import ray
import torch
from tqdm import tqdm

from verl import DataProto
from verl.protocol import pad_dataproto_to_divisor, unpad_dataproto
from verl.single_controller.base import Worker
from verl.trainer.ppo.core_algos import AdvantageEstimator, agg_loss
from verl.trainer.ppo.metric_utils import (
    compute_data_metrics,
    compute_throughout_metrics,
    compute_timing_metrics,
)
from verl.trainer.ppo.reward import compute_reward, compute_reward_async
from verl.utils.debug import marked_timer
from verl.utils.metric import (
    reduce_metrics,
)
from verl.trainer.ppo.ray_trainer import (
    RayPPOTrainer, 
    apply_kl_penalty,
    compute_advantage,
)
from verl.paprika.utils.json_utils import write_json
from verl.paprika.utils.paprika_metrics import calculate_paprika_metrics

WorkerType = Type[Worker]


class PaprikaTrainer(RayPPOTrainer):
    def _validate(self):
        validation_sampling_params = {
            "n": 1,
            "temperature": self.config.actor_rollout_ref.rollout.val_kwargs.temperature,
            "top_p": self.config.actor_rollout_ref.rollout.val_kwargs.top_p,
            "top_k": self.config.actor_rollout_ref.rollout.val_kwargs.top_k,
            "max_tokens": self.config.data.max_response_length,
            "min_p": self.config.actor_rollout_ref.rollout.val_kwargs.min_p,
        }

        # TODO: handle multiple validation batch logic
        assert len(self.val_dataloader) == 1, (
            "Validation dataloader having more than one batches"
            "is not currently supported!"
        )

        for test_data in self.val_dataloader:
            test_batch = DataProto.from_single_dict(test_data)

            # add unique identifiers
            test_batch.non_tensor_batch["uid"] = np.array(
                [str(uuid.uuid4()) for _ in range(len(test_batch.batch))], 
                dtype=object,
            )

            # repeat test batch
            test_batch = test_batch.repeat(
                repeat_times=self.config.actor_rollout_ref.rollout.val_kwargs.n, 
                interleave=True,
            )
            non_tensor_batch_keys_to_pop = ["paprika_task_scenario"]
            batch_keys_to_pop = ["input_ids", "attention_mask", "position_ids"]

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
                "sampling_params": validation_sampling_params,
                "env_mode": "test",
            }

            test_gen_batch_padded, pad_size = pad_dataproto_to_divisor(
                data=test_gen_batch, 
                size_divisor=self.actor_rollout_wg.world_size,
            )

            if not self.async_rollout_mode:
                test_output_gen_batch_padded = self.actor_rollout_wg.generate_sequences(test_gen_batch_padded)

            else:
                raise ValueError(f"Async rollout mode not supported for multi-turn setup")

            # unpad
            test_output_gen_batch = unpad_dataproto(test_output_gen_batch_padded, pad_size=pad_size)

            test_batch = test_batch.union(test_output_gen_batch)

            metrics_dict, task_trajectories = calculate_paprika_metrics(
                data=test_batch,
                num_trajectories_per_task=self.config.actor_rollout_ref.rollout.val_kwargs.n,
                metric_type="val-core",
            )

        # save validation rollouts
        if self.config.trainer.validation_data_dir is not None:
            save_path = os.path.join(
                self.config.trainer.validation_data_dir,
                f"validation_trajectories_steps_{self.global_steps}.json"
            )

            write_json(
                data={
                    "records": task_trajectories,
                },
                fname=save_path,
            )

        # return val metrics
        return metrics_dict
    
    def fit(self):
        """
        The training loop of PPO.
        The driver process only need to call the compute functions of the worker group through RPC
        to construct the PPO dataflow.
        The light-weight advantage computation is done on the driver process.
        """
        from omegaconf import OmegaConf

        from verl.utils.tracking import Tracking

        logger = Tracking(
            project_name=self.config.trainer.project_name,
            experiment_name=self.config.trainer.experiment_name,
            default_backend=self.config.trainer.logger,
            config=OmegaConf.to_container(self.config, resolve=True),
        )

        self.global_steps = 0

        # load checkpoint before doing anything
        self._load_checkpoint()

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

        training_sampling_params = {
            "n": 1,
            "temperature": self.config.actor_rollout_ref.rollout.temperature,
            "top_p": self.config.actor_rollout_ref.rollout.top_p,
            "top_k": self.config.actor_rollout_ref.rollout.top_k,
            "max_tokens": self.config.data.max_response_length,
        }

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

                # add unique identifiers
                batch.non_tensor_batch["uid"] = np.array(
                    [str(uuid.uuid4()) for _ in range(len(batch.batch))], 
                    dtype=object,
                )

                # copy batch to generate multiple trajectories per problem
                batch = batch.repeat(
                    repeat_times=self.config.actor_rollout_ref.rollout.n, 
                    interleave=True,
                )

                # pop those keys for generation
                batch_keys_to_pop = ["input_ids", "attention_mask", "position_ids"]
                non_tensor_batch_keys_to_pop = ["raw_prompt_ids", "paprika_task_scenario", "uid"]
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

                gen_batch.meta_info["sampling_params"] = training_sampling_params
                gen_batch.meta_info["env_mode"] = "train"

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

                    if self.config.algorithm.adv_estimator == AdvantageEstimator.REMAX:
                        raise ValueError("REMAX advantage estimator not supported yet.")

                    batch = batch.union(gen_batch_output)

                    # calculate training rollout metrics
                    train_trajectories_metrics, task_trajectories = calculate_paprika_metrics(
                        data=batch,
                        num_trajectories_per_task=self.config.actor_rollout_ref.rollout.n,
                        metric_type="train",
                    )

                    # save rollouts if needed
                    if self.config.trainer.rollout_data_dir is not None:
                        save_path = os.path.join(
                            self.config.trainer.rollout_data_dir,
                            f"training_trajectories_steps_{self.global_steps}.json"
                        )

                        write_json(
                            data={
                                "records": task_trajectories,
                            },
                            fname=save_path,
                        )

                    for train_metric_key in train_trajectories_metrics:
                        metrics[train_metric_key] = train_trajectories_metrics[train_metric_key]

                    # Balance the number of valid tokens across DP ranks.
                    # NOTE: This usually changes the order of data in the `batch`,
                    # which won't affect the advantage calculation (since it's based on uid),
                    # but might affect the loss calculation (due to the change of mini-batching).
                    # TODO: Decouple the DP balancing and mini-batching.
                    if self.config.trainer.balance_batch:
                        self._balance_batch(batch, metrics=metrics)

                    # compute global_valid tokens
                    batch.meta_info["global_token_num"] = torch.sum(batch.batch["attention_mask"], dim=-1).tolist()

                    eos_token_rate = None
                    eos_token_loss_rate = None

                    with marked_timer("reward", timing_raw, color="yellow"):
                        # compute reward model score
                        if self.use_rm:
                            reward_tensor = self.rm_wg.compute_rm_score(batch)
                            batch = batch.union(reward_tensor)

                        if self.config.reward_model.launch_reward_fn_async:
                            future_reward = compute_reward_async.remote(batch, self.config, self.tokenizer)
                        else:
                            reward_tensor, reward_extra_infos_dict = compute_reward(batch, self.reward_fn)
                            eos_token_rate = reward_extra_infos_dict.pop("eos_token_rate", None)
                            eos_token_loss_rate = reward_extra_infos_dict.pop("eos_token_loss_rate", None)

                    # recompute old_log_probs
                    with marked_timer("old_log_prob", timing_raw, color="blue"):
                        # create new batch
                        select_keys_to_copy = [
                            "prompts", 
                            "responses", 
                            "response_mask", 
                            "input_ids", 
                            "attention_mask", 
                            "position_ids",
                            "loss_mask",
                        ]

                        key_to_tensor_name = {
                            key: key for key in select_keys_to_copy
                        }

                        if self.config.trainer.old_log_prob_calculation_system_prompt == "system_prompts_as_is":
                            key_to_tensor_name = {
                                key: f"{key}_with_system_prompts_as_is"
                                for key in key_to_tensor_name
                            }

                        elif self.config.trainer.old_log_prob_calculation_system_prompt == "custom_system_prompt":
                            key_to_tensor_name = {
                                key: f"{key}_with_custom_system_prompt"
                                for key in key_to_tensor_name
                            }

                        elif self.config.trainer.old_log_prob_calculation_system_prompt != "default_system_prompt":
                            raise ValueError(
                                f"Given old log prob calculation system prompt "
                                f"{self.config.trainer.old_log_prob_calculation_system_prompt} is not supported."
                            )

                        tensors_for_old_log_prob_calculation = {
                            key: batch.batch[key_to_tensor_name[key]]
                            for key in key_to_tensor_name
                        }

                        batch_for_calculating_old_log_probs = DataProto.from_dict(
                            tensors=tensors_for_old_log_prob_calculation,
                            meta_info=batch.meta_info,
                        )

                        # Calculate old_log_probs
                        old_log_prob = self.actor_rollout_wg.compute_log_prob(
                            batch_for_calculating_old_log_probs
                        )

                        # Merge batch
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
                            select_keys_to_copy = [
                                "prompts", 
                                "responses", 
                                "response_mask", 
                                "input_ids", 
                                "attention_mask", 
                                "position_ids",
                                "loss_mask",
                            ]

                            key_to_tensor_name = {
                                key: key for key in select_keys_to_copy
                            }

                            if self.config.trainer.ref_log_prob_calculation_system_prompt == "system_prompts_as_is":
                                key_to_tensor_name = {
                                    key: f"{key}_with_system_prompts_as_is"
                                    for key in key_to_tensor_name
                                }

                            elif self.config.trainer.ref_log_prob_calculation_system_prompt == "custom_system_prompt":
                                key_to_tensor_name = {
                                    key: f"{key}_with_custom_system_prompt"
                                    for key in key_to_tensor_name
                                }

                            elif self.config.trainer.ref_log_prob_calculation_system_prompt != "default_system_prompt":
                                raise ValueError(
                                    f"Given ref log prob calculation system prompt "
                                    f"{self.config.trainer.ref_log_prob_calculation_system_prompt} is not supported."
                                )
                            
                            tensors_for_calculating_ref_log_probs = {
                                key: batch.batch[key_to_tensor_name[key]]
                                for key in key_to_tensor_name
                            }

                            batch_for_calculating_ref_log_probs = DataProto.from_dict(
                                tensors=tensors_for_calculating_ref_log_probs,
                                meta_info=batch.meta_info,
                            )

                            if not self.ref_in_actor:
                                ref_log_prob = self.ref_policy_wg.compute_ref_log_prob(
                                    batch_for_calculating_ref_log_probs
                                )
                            else:
                                ref_log_prob = self.actor_rollout_wg.compute_ref_log_prob(
                                    batch_for_calculating_ref_log_probs
                                )
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

                        if reward_extra_infos_dict:
                            # Only add items that are lists/arrays with matching batch size
                            # (filter out scalar metrics like majority_vote_accuracy_global)
                            batch_size = len(batch)
                            batch.non_tensor_batch.update({
                                k: np.array(v) 
                                for k, v in reward_extra_infos_dict.items() 
                                if isinstance(v, (list, np.ndarray)) and len(v) == batch_size
                            })

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

                    batch.meta_info["multi_turn"] = True
                    batch.meta_info["loss_type"] = self.config.trainer.get("loss_type", "grpo")

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
                            actor_output = self.actor_rollout_wg.update_actor(batch)
                        actor_output_metrics = reduce_metrics(actor_output.meta_info["metrics"])
                        metrics.update(actor_output_metrics)

                    # validate
                    eval_on_last_step = getattr(self.config.trainer, 'eval_on_last_step', True)
                    should_eval_last = is_last_step and eval_on_last_step
                    if self.val_reward_fn is not None and self.config.trainer.test_freq > 0 and (should_eval_last or self.global_steps % self.config.trainer.test_freq == 0):
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

                if eos_token_rate is not None:
                    metrics.update(
                        {
                            "eos_token_info/eos_token_rate": eos_token_rate,
                        }
                    )

                if eos_token_loss_rate is not None:
                    metrics.update(
                        {
                            "eos_token_info/eos_token_loss_rate": eos_token_loss_rate,
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