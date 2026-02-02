# Copyright 2024 Bytedance Ltd. and/or its affiliates
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
The vllm_rollout that can be applied in different backend
When working with FSDP:
- Use DTensor weight loader (recommended) or HF weight loader
- Utilize state_dict from the FSDP to synchronize the weights among tp ranks in vLLM
When working with Megatron:
- Use Megatron weight loader
- During training, only the current pp stage holds the parameters
- Before inference, broadcast the parameters of the current pp rank
  to all other pp ranks (all pp ranks holds all the parameters)
- Bind the parameters to the inference engine
- Do inference in tp. pp is treated as additional dp
- After inference, all the parameters that doesn't belong to this pp rank is freed.
"""

import logging
import os
from copy import deepcopy
import json
from typing import List, Dict, Tuple, Any

import numpy as np
import torch
import torch.distributed
from omegaconf import DictConfig, OmegaConf
from tensordict import TensorDict
from vllm import LLM, SamplingParams
from vllm.distributed import parallel_state as vllm_ps

from verl import DataProto
from verl.paprika.task_manager import TaskManager
from verl.third_party.vllm import vllm_version
from verl.utils.debug import GPUMemoryLogger
from verl.workers.rollout.base import BaseRollout
from verl.paprika.environments import get_batch_of_environments

logger = logging.getLogger(__file__)
logger.setLevel(os.getenv("VERL_LOGGING_LEVEL", "WARN"))


class vLLMMultiturnRollout(BaseRollout):    
    def get_eos_suffix(self, model_name: str) -> List[int]:
        if model_name == "Qwen/Qwen2.5-3B-Instruct":
            eos_suffix = [198]
        
        elif model_name == "Qwen/Qwen2.5-3B":
            eos_suffix = [198]

        elif model_name == "Qwen/Qwen2.5-7B":
            eos_suffix = [198]

        elif model_name == "meta-llama/Llama-3.2-3B-Instruct":
            eos_suffix = []

        elif model_name == "meta-llama/Meta-Llama-3.1-8B-Instruct":
            eos_suffix = []

        elif model_name == "ftajwar/paprika_Meta-Llama-3.1-8B-Instruct":
            eos_suffix = []

        elif model_name == "Qwen/Qwen3-4B":
            eos_suffix = [198]

        elif model_name == "Qwen/Qwen3-4B-Base":
            eos_suffix = [198]

        elif model_name == "Qwen/Qwen3-1.7B":
            eos_suffix = [198]

        elif model_name == "Qwen/Qwen3-8B":
            eos_suffix = [198]

        elif model_name == "Qwen/Qwen3-14B":
            eos_suffix = [198]
        
        else:
            raise ValueError(
                f"Given model name: {model_name} --- is not supported."
            )
        
        return eos_suffix

    def __init__(self, model_path: str, config: DictConfig, tokenizer, model_hf_config, **kwargs):
        """A vLLM rollout. It requires the module is supported by the vllm.

        Args:
            module: module here follows huggingface APIs
            config: DictConfig
            tokenizer: the task/model tokenizer
            model_hf_config: the huggingface config to initiallize the generating model in vllm
            **kwargs: train_tp, for Megatron Backend to initialize hybrid engine (zero redundancy) process group
        """
        super().__init__()
        self.config = config
        assert not (not config.enforce_eager and config.free_cache_engine), "disable CUDA graph (enforce_eager = False) if free cache engine"

        tensor_parallel_size = self.config.get("tensor_model_parallel_size", 1)
        assert tensor_parallel_size <= torch.distributed.get_world_size(), "tensor parallel size should be less than or equal to the world size"
        max_num_batched_tokens = self.config.get("max_num_batched_tokens", 8192)

        if kwargs.get("train_tp") is not None:
            # deployed with megatron
            import os

            os.environ["CUDA_TIMER_STREAM_KAFKA_ENABLE"] = "0"
            os.environ["MEGATRON_IMPORT_TIMERS"] = "0"
            if vllm_version in (
                "0.5.4",
                "0.6.3",
            ):
                train_tp = kwargs.get("train_tp")
                num_tp_per_train_tp = train_tp // tensor_parallel_size
                vllm_ps.initialize_parallel_state(tensor_model_parallel_size=tensor_parallel_size, num_tp_per_train_tp=num_tp_per_train_tp)
            else:
                vllm_ps.initialize_model_parallel(tensor_model_parallel_size=tensor_parallel_size)

        rope_scaling_config = getattr(model_hf_config, "rope_scaling", None)
        if not rope_scaling_config:
            max_position_embeddings = None
            if hasattr(model_hf_config, "max_position_embeddings"):
                max_position_embeddings = model_hf_config.max_position_embeddings
            elif hasattr(model_hf_config, "llm_config") and hasattr(model_hf_config.llm_config, "max_position_embeddings"):
                max_position_embeddings = model_hf_config.llm_config.max_position_embeddings
            elif hasattr(model_hf_config, "text_config") and hasattr(model_hf_config.text_config, "max_position_embeddings"):
                max_position_embeddings = model_hf_config.text_config.max_position_embeddings
            if max_position_embeddings is None:
                raise ValueError("max_position_embeddings not found in model_hf_config")

            assert max_position_embeddings >= config.prompt_length + config.response_length, "model context length should be greater than total sequence length"

        max_model_len = int(config.max_model_len or config.prompt_length + config.response_length)

        if max_num_batched_tokens < max_model_len and self.config.enable_chunked_prefill:
            raise ValueError(
                "Enable chunked prefill, max_num_batched_tokens is smaller than max_model_len, \
                             please increase max_num_batched_tokens or disable chunked prefill"
            )

        trust_remote_code = kwargs.get("trust_remote_code", False)
        load_format = "dummy" if config.load_format.startswith("dummy") else config.load_format

        lora_kwargs = kwargs.pop("lora_kwargs", {})
        self.lora_kwargs = lora_kwargs
        # copy it to avoid secretly modifying the engine config
        engine_kwargs = {} if "engine_kwargs" not in config or "vllm" not in config.engine_kwargs else OmegaConf.to_container(deepcopy(config.engine_kwargs.vllm))
        # For each vLLM engine parameter,
        # - `None` means not setting it, so we pop it, and leave it to vLLM default value
        #    (which can vary across different vLLM versions);
        # - Otherwise it's the desired value we want to explicitly set.
        engine_kwargs = {key: val for key, val in engine_kwargs.items() if val is not None}
        if config.get("limit_images", None):  # support for multi-image data
            engine_kwargs["limit_mm_per_prompt"] = {"image": config.get("limit_images")}

        print("Loading inference engine")
        self.inference_engine = LLM(
            model=model_path,
            enable_sleep_mode=True,
            tensor_parallel_size=tensor_parallel_size,
            distributed_executor_backend="external_launcher",
            dtype=config.dtype,
            enforce_eager=config.enforce_eager,
            gpu_memory_utilization=config.gpu_memory_utilization,
            disable_custom_all_reduce=True,
            skip_tokenizer_init=False,
            max_model_len=max_model_len,
            load_format=load_format,
            disable_log_stats=config.disable_log_stats,
            max_num_batched_tokens=max_num_batched_tokens,
            enable_chunked_prefill=config.enable_chunked_prefill,
            enable_prefix_caching=True,
            trust_remote_code=trust_remote_code,
            seed=config.get("seed", 0),
            **lora_kwargs,
            **engine_kwargs,
        )
        

        # Offload vllm model to reduce peak memory usage
        self.inference_engine.sleep(level=1)

        kwargs = dict(
            n=1,
            logprobs=0,  # can be set to 0 and let actor to recompute
            max_tokens=config.response_length,
        )

        # # we may detokenize the result all together later
        if vllm_version != "0.3.1":
            kwargs["detokenize"] = False

        # supporting adding any sampling params from the config file
        for k in config.keys():
            if hasattr(SamplingParams(), str(k)):
                kwargs[k] = config.get(k)

        print(f"kwargs: {kwargs}")
        self.sampling_params = SamplingParams(**kwargs)

        self.pad_token_id = tokenizer.pad_token_id
        self.tokenizer = tokenizer

    def prepare_task_manager(
        self,
        prompts: DataProto,
    ) -> TaskManager:
        non_tensor_batch = prompts.non_tensor_batch
        env_mode = prompts.meta_info["env_mode"]

        assert (
            "paprika_task_scenario" in non_tensor_batch
        ), f"The dataset is not in correct format to run Paprika"

        task_scenarios = non_tensor_batch["paprika_task_scenario"]

        task_group_names = [
            task_scenario["task_group_name"] 
            for task_scenario in task_scenarios
        ]

        task_states = [
            {"env": task_scenario["env"], "agent": task_scenario["agent"]}
            for task_scenario in task_scenarios
        ]
        
        env_modes = [
            env_mode for _ in range(len(task_scenarios))
        ]

        environments = get_batch_of_environments(
            task_group_names=task_group_names,
            task_states=task_states,
            env_modes=env_modes,
        )

        task_manager = TaskManager(
            list_of_environments=environments,
        )

        return task_manager
    
    def get_list_of_supported_thinking_models(
        self,
    ) -> List[str]:
        # return [
        #     "Qwen/Qwen3-1.7B",
        #     # "Qwen/Qwen3-4B",
        # ]
        return []
    
    def _process_individual_trajectory(
        self, 
        trajectory: List[Dict[str, str]],
        agent_generated_tokens: List[List[int]],
    ) -> Dict[str, List[int]]:
        # TODO: test with the idea where we do not discard last env step
        # # discard last env step
        # trajectory = trajectory[:-1]

        # First: get the first assistant turn index
        first_assistant_turn_index = None
        for index in range(len(trajectory)):
            if trajectory[index]["role"] == "assistant":
                first_assistant_turn_index = index
                break

        if first_assistant_turn_index is None:
            first_assistant_turn_index = len(trajectory)

        # Next, prepare the prompt_ids
        prompt_subpart_of_trajectory = deepcopy(
            trajectory[0 : first_assistant_turn_index]
        )

        policy_model_name = self.config.get("policy_model_name", None)
        assert policy_model_name is not None

        tokenizer_kwargs = {
            "conversation": prompt_subpart_of_trajectory,
            "add_generation_prompt": True,
            "tokenize": True,
        }

        if policy_model_name in self.get_list_of_supported_thinking_models():
            tokenizer_kwargs["enable_thinking"] = False

        prompt_ids = self.tokenizer.apply_chat_template(
            **tokenizer_kwargs,
        )

        # Now tokenize the whole trajectory, and build the mask along the way
        response_mask = []
        agent_turn = 0

        for index in range(first_assistant_turn_index, len(trajectory)):
            role = trajectory[index]["role"]

            chat_so_far = deepcopy(trajectory[:index])
            with_current = deepcopy(trajectory[:index+1])

            chat_so_far_ids = []
            if len(chat_so_far) > 0:
                tokenizer_kwargs = {
                    "conversation": chat_so_far,
                    "tokenize": True,
                    "add_generation_prompt": (index == first_assistant_turn_index),
                    "padding": False,
                    "truncation": False,
                }

                if policy_model_name in self.get_list_of_supported_thinking_models():
                    tokenizer_kwargs["enable_thinking"] = False

                chat_so_far_ids = self.tokenizer.apply_chat_template(
                    **tokenizer_kwargs,
                )

            else:
                raise ValueError("chat_so_far cannot be empty.")
            
            tokenizer_kwargs = {
                "conversation": with_current,
                "tokenize": True,
                "add_generation_prompt": (
                    index == len(trajectory) - 1
                    and role == "user"
                ),
                "padding": False,
                "truncation": False,
            }

            if policy_model_name in self.get_list_of_supported_thinking_models():
                tokenizer_kwargs["enable_thinking"] = False

            with_current_ids = self.tokenizer.apply_chat_template(
                **tokenizer_kwargs,
            )

            current_turn_token_ids = with_current_ids[len(chat_so_far_ids):]

            # However, the response mask will be different
            if role != "assistant":
                response_mask.extend([0] * len(current_turn_token_ids))
                prompt_ids.extend(current_turn_token_ids)

            else:
                tokenizer_kwargs = {
                    "conversation": chat_so_far,
                    "tokenize": True,
                    "add_generation_prompt": True,
                    "padding": False,
                    "truncation": False,
                }

                if policy_model_name in self.get_list_of_supported_thinking_models():
                    tokenizer_kwargs["enable_thinking"] = False

                chat_so_far_ids_with_generation_prompt = self.tokenizer.apply_chat_template(
                    **tokenizer_kwargs,
                )

                prefix_length = len(chat_so_far_ids_with_generation_prompt)
                new_ids_excluding_generation_prompt = with_current_ids[prefix_length:]
                
                generation_prompt_length = (
                    len(current_turn_token_ids) 
                    - len(new_ids_excluding_generation_prompt)
                )

                # substitute directly model generated part instead of
                # token --> text --> token part
                # since this can cause issues
                current_turn_token_ids = (
                    current_turn_token_ids[:generation_prompt_length]
                    + agent_generated_tokens[agent_turn]
                )
                new_ids_excluding_generation_prompt = agent_generated_tokens[agent_turn]
                agent_turn += 1

                assert new_ids_excluding_generation_prompt.count(self.tokenizer.eos_token_id) == 1
                eos_token_index = new_ids_excluding_generation_prompt.index(self.tokenizer.eos_token_id)

                response_mask_extension = (
                    [0] * generation_prompt_length
                    + [1] * (eos_token_index + 1)
                    + [0] * (len(new_ids_excluding_generation_prompt) - eos_token_index - 1)
                )

                assert len(response_mask_extension) == len(current_turn_token_ids), (
                    "current turns token_ids should have same length as"
                    "response_mask_extension"
                )

                response_mask.extend(response_mask_extension)
                prompt_ids.extend(current_turn_token_ids)

        # Now calculate prompt and response token ids
        response_ids = prompt_ids[-len(response_mask) :]
        prompt_ids = prompt_ids[: len(prompt_ids) - len(response_mask)]

        return {
            "prompt_ids": prompt_ids,
            "response_ids": response_ids,
            "response_mask": response_mask,
        }
    
    def _handle_padding(
        self,
        token_ids: List[List[int]], # shape: (batch size, ...)
        padding_side: str,
        padding_max_length: int,
        pad_token_id: int,
        assert_length_is_upper_bounded: bool,
    ) -> Tuple[torch.LongTensor, torch.LongTensor]:
        if assert_length_is_upper_bounded:
            for ids in token_ids:
                assert len(ids) <= padding_max_length

            truncated_token_ids = [ids for ids in token_ids]

        else:
            truncated_token_ids = [
                ids[:padding_max_length] for ids in token_ids
            ]

        processed_token_ids = []
        attention_masks = []

        for index in range(len(truncated_token_ids)):
            num_pad_tokens = padding_max_length - len(truncated_token_ids[index])

            if padding_side == "left":
                padded_tokens = (
                    [pad_token_id] * num_pad_tokens 
                    + truncated_token_ids[index]
                )
                attention_mask = (
                    [0] * num_pad_tokens 
                    + [1] * len(truncated_token_ids[index])
                )

            elif padding_side == "right":
                padded_tokens = (
                    truncated_token_ids[index] 
                    + [pad_token_id] * num_pad_tokens
                )
                attention_mask = (
                    [1] * len(truncated_token_ids[index]) 
                    + [0] * num_pad_tokens
                )

            else:
                raise ValueError(
                    f"Given padding side {padding_side} is not supported."
                )
            
            processed_token_ids.append(padded_tokens)
            attention_masks.append(attention_mask)

        processed_token_ids_tensor = torch.tensor(
            processed_token_ids,
            dtype=torch.long,
        )
        attention_masks_tensor = torch.tensor(
            attention_masks,
            dtype=torch.long,
        )

        return processed_token_ids_tensor, attention_masks_tensor
    
    def _postprocess_multiturn_trajectories(
        self,
        prompts: DataProto,
        trajectories: List[List[Dict[str, str]]],
        task_success_labels: List[float],
        rewards: List[float],
        agent_generated_tokens: List[List[List[int]]],
    ) -> Dict[str, Any]:
        # First, do per trajectory preliminary processing
        process_keys = ["prompt_ids", "response_ids", "response_mask"]
        all_trajectory_subparts = {
            key: [] for key in process_keys
        }
        for trajectory_index in range(len(trajectories)):
            trajectory_subparts = self._process_individual_trajectory(
                trajectory=trajectories[trajectory_index],
                agent_generated_tokens=agent_generated_tokens[trajectory_index],
            )
            for key in process_keys:
                all_trajectory_subparts[key].append(
                    trajectory_subparts[key]
                )

        # process prompts
        prompt_ids, prompt_attention_mask = self._handle_padding(
            token_ids=all_trajectory_subparts["prompt_ids"],
            padding_side="left",
            padding_max_length=self.config.prompt_length,
            pad_token_id=self.tokenizer.pad_token_id,
            assert_length_is_upper_bounded=True,
        )

        # process responses
        response_ids, response_attention_mask = self._handle_padding(
            token_ids=all_trajectory_subparts["response_ids"],
            padding_side="right",
            padding_max_length=self.config.trajectory_length,
            pad_token_id=self.tokenizer.pad_token_id,
            assert_length_is_upper_bounded=True,
        )

        # process response masks
        response_mask, _ = self._handle_padding(
            token_ids=all_trajectory_subparts["response_mask"],
            padding_side="right",
            padding_max_length=self.config.trajectory_length,
            pad_token_id=0,
            assert_length_is_upper_bounded=True,\
        )

        assert response_ids.shape == response_mask.shape, (
            f"mismatch in response_ids and response_mask shape: "
            f"{response_ids.shape} vs {response_mask.shape}"
        )

        loss_mask = response_mask * response_attention_mask
        input_ids = torch.cat([prompt_ids, response_ids], dim=1)
        attention_mask = torch.cat([prompt_attention_mask, response_attention_mask], dim=1)
        position_ids = (attention_mask.cumsum(dim=1) - 1) * attention_mask

        json_string_trajectories = []
        # convert trajectories to json format, for dumping
        for trajectory_index in range(len(trajectories)):
            record = {
                "task_group_name": prompts[trajectory_index].non_tensor_batch[
                    "paprika_task_scenario"
                ]["task_group_name"],
                "env": prompts[trajectory_index].non_tensor_batch[
                    "paprika_task_scenario"
                ]["env"],
                "agent": prompts[trajectory_index].non_tensor_batch[
                    "paprika_task_scenario"
                ]["agent"],
                "success_label": task_success_labels[trajectory_index],
                "reward": rewards[trajectory_index],
                "trajectory": trajectories[trajectory_index],
            }

            # convert to string
            json_string = json.dumps(record)
            json_string_trajectories.append(json_string)

        return {
            "prompts": prompt_ids,  # [bsz, prompt_length]
            "responses": response_ids,  # [bsz, response_length]
            "response_mask": response_mask,  # [bsz, response_length]
            "input_ids": input_ids,  # [bsz, prompt_length + response_length]
            "attention_mask": attention_mask,  # [bsz, prompt_length + response_length]
            "position_ids": position_ids,  # [bsz, prompt_length + response_length]
            "json_string_trajectories": json_string_trajectories,
            "loss_mask": loss_mask, # [bsz, response_length]
        }
    
    def prepare_inputs_to_vllm_engine_using_chat_template_directly(
        self,
        task_manager: TaskManager,
    ) -> List[List[int]]:
        curr_trajectories = (
            task_manager.get_trajectory_states_for_next_round_of_generations()
        )

        policy_model_name = self.config.get("policy_model_name", None)
        assert policy_model_name is not None

        tokenizer_kwargs = {
            "add_generation_prompt": True,
            "tokenize": False,
            "padding": False,
            "truncation": False,
        }

        if policy_model_name in self.get_list_of_supported_thinking_models():
            tokenizer_kwargs["enable_thinking"] = False

        curr_trajectories_formatted_with_chat_template = [
            self.tokenizer.apply_chat_template(
                conversation=curr_trajectory, 
                **tokenizer_kwargs,
            )
            for curr_trajectory in curr_trajectories
        ]

        curr_trajectories_tokenized = [
            self.tokenizer.encode(
                curr_trajectory,
                add_special_tokens=False,
            )
            for curr_trajectory in curr_trajectories_formatted_with_chat_template
        ]

        return curr_trajectories_tokenized
    
    def prepare_inputs_to_vllm_engine(
        self,
        task_manager: TaskManager,
    ) -> List[List[int]]:
        # Assumption: trajectory looks like:
        # system prompt, user prompt, first turn agent action, env feedback, second turn agent action, ....
        curr_trajectories = (
            task_manager.get_trajectory_states_for_next_round_of_generations()
        )

        curr_agent_generated_tokens = (
            task_manager.get_all_agent_generated_tokens_for_next_round_of_generations()
        )

        assert len(curr_trajectories) == len(curr_agent_generated_tokens)

        vllm_input_tokens = []

        for trajectory_index in range(len(curr_trajectories)):
            processed_trajectory_subparts = self._process_individual_trajectory(
                trajectory=curr_trajectories[trajectory_index],
                agent_generated_tokens=curr_agent_generated_tokens[trajectory_index],
            )

            prompt_ids = processed_trajectory_subparts["prompt_ids"]
            response_ids = processed_trajectory_subparts["response_ids"]

            entire_trajectory_tokenized = prompt_ids + response_ids

            vllm_input_tokens.append(
                entire_trajectory_tokenized
            )

            # import pdb; pdb.set_trace()

        return vllm_input_tokens
            
        
    @GPUMemoryLogger(role="vllm rollout multiturn", logger=logger)
    @torch.no_grad()
    def generate_sequences(self, prompts: DataProto, **kwargs) -> DataProto:
        # rebuild vllm cache engine
        if (
            vllm_version
            in (
                "0.5.4",
                "0.6.3",
            )
            and self.config.free_cache_engine
        ):
            self.inference_engine.init_cache_engine()

        non_tensor_batch = prompts.non_tensor_batch

        # Start a "thread" to keep track of each conversation
        # Prepare all task environments
        all_trajectories_for_training = []
        all_trajectories_with_original_system_prompt = []
        all_trajectories_with_custom_system_prompt = []
        trajectory_level_rewards = []
        task_success_labels = []
        task_num_turns = []


        task_manager = self.prepare_task_manager(
            prompts=prompts,
        )

        policy_model_name = self.config.get("policy_model_name", None)
        assert policy_model_name is not None

        # Generate all multi-turn rollout trajectories
        while task_manager.get_num_valid_tasks() > 0:
            tokenized_inputs_for_vllm_engine = (
                # self.prepare_inputs_to_vllm_engine_using_chat_template_directly(
                #     task_manager=task_manager,
                # )
                self.prepare_inputs_to_vllm_engine(
                    task_manager=task_manager,
                )
            )

            assert len(tokenized_inputs_for_vllm_engine) == task_manager.get_num_valid_tasks()

            all_env_max_tokens_per_turn = (
                task_manager.get_all_env_max_tokens_per_turn_for_next_round_of_generations()
            )

            assert len(all_env_max_tokens_per_turn) == task_manager.get_num_valid_tasks()

            # Per env sampling params is provided by the trainer
            if "per_env_sampling_params" in prompts.non_tensor_batch.keys():
                per_env_sampling_params = prompts.non_tensor_batch["per_env_sampling_params"].tolist()
                current_valid_task_ids = task_manager.get_all_valid_task_ids()
                
                per_env_sampling_params = [
                    per_env_sampling_params[t_id]
                    for t_id in current_valid_task_ids
                ]

            # It is not given, so we need to produce it
            else:
                assert "sampling_params" in prompts.meta_info.keys()
                per_env_sampling_params = [
                    deepcopy(prompts.meta_info["sampling_params"])
                    for _ in range(len(all_env_max_tokens_per_turn))
                ]

            # Modify the per env max tokens, since it can't be centrally defined and depends
            # on each training environment instance
            for env_index in range(len(all_env_max_tokens_per_turn)):
                env_max_tokens_per_turn = all_env_max_tokens_per_turn[env_index]

                if isinstance(env_max_tokens_per_turn, int):
                    assert env_max_tokens_per_turn >= 1
                    assert "max_tokens" in per_env_sampling_params[env_index]

                    per_env_sampling_params[env_index]["max_tokens"] = env_max_tokens_per_turn
                    per_env_sampling_params[env_index] = SamplingParams(
                        **per_env_sampling_params[env_index]
                    )
        
            vllm_inputs = [
                {"prompt_token_ids": raw_prompt_ids} 
                for raw_prompt_ids in tokenized_inputs_for_vllm_engine
            ]

            llm_responses = self.inference_engine.generate(
                prompts=vllm_inputs,
                sampling_params=per_env_sampling_params,
                use_tqdm=False,
            )

            generated_texts = []
            agent_response_tokens = []
            for output in llm_responses:
                for sample_id in range(len(output.outputs)):
                    response_ids = output.outputs[sample_id].token_ids

                    assert len(response_ids) <= prompts.meta_info["sampling_params"]["max_tokens"]
                    response_ids_list = list(response_ids)

                    # Very hacky solution, but best I can think of right now
                    eos_suffix = self.get_eos_suffix(
                        model_name=policy_model_name,
                    )

                    if self.tokenizer.eos_token_id not in response_ids_list:
                        response_ids_list += [self.tokenizer.eos_token_id] + eos_suffix

                    else:
                        assert response_ids_list[-1] == self.tokenizer.eos_token_id
                        assert response_ids_list.count(self.tokenizer.eos_token_id) == 1
                        response_ids_list += eos_suffix

                    agent_response_tokens.append(response_ids_list)

                    generated_text = self.tokenizer.decode(
                        response_ids,
                        skip_special_tokens=True,
                    )
                    generated_texts.append(generated_text)

            task_manager.update_task_trajectories_with_agent_actions(
                agent_responses=generated_texts,
                agent_response_tokens=agent_response_tokens,
            )
        
        # Retrieve all rewards and trajectories

        # 1. system prompt ---> default from each environment
        all_trajectories_for_training.extend(
            task_manager.get_all_trajectories_with_default_system_prompt()
        )

        # 2. system prompt ---> whatever is used for generation
        all_trajectories_with_original_system_prompt.extend(
            task_manager.get_all_trajectories_with_system_prompts_as_is()
        )

        # 3. system prompt ---> custom one from each environment
        all_trajectories_with_custom_system_prompt.extend(
            task_manager.get_all_trajectories_with_custom_system_prompt()
        )

        # rewards and number of turns
        trajectory_level_rewards.extend(
            task_manager.get_all_trajectory_level_rewards()
        )
        task_num_turns.extend(task_manager.get_all_task_num_turns())
        task_success_labels.extend(task_manager.get_all_task_success_labels())

        # Process trajectories
        assert (
            len(all_trajectories_for_training) == len(prompts)
        ), "all task should have a generated trajectory"

        postprocessing_outputs = self._postprocess_multiturn_trajectories(
            prompts=prompts,
            trajectories=all_trajectories_for_training,
            task_success_labels=task_success_labels,
            rewards=trajectory_level_rewards,
            agent_generated_tokens=task_manager.get_all_agent_generated_tokens(),
        )

        post_processing_outputs_original_system_prompt = (
            self._postprocess_multiturn_trajectories(
                prompts=prompts,
                trajectories=all_trajectories_with_original_system_prompt,
                task_success_labels=task_success_labels,
                rewards=trajectory_level_rewards,
                agent_generated_tokens=task_manager.get_all_agent_generated_tokens(),
            )
        )

        post_processing_outputs_custom_system_prompt = (
            self._postprocess_multiturn_trajectories(
                prompts=prompts,
                trajectories=all_trajectories_with_custom_system_prompt,
                task_success_labels=task_success_labels,
                rewards=trajectory_level_rewards,
                agent_generated_tokens=task_manager.get_all_agent_generated_tokens(),
            )
        )

        # Update non-tensor batch
        non_tensor_batch["rewards"] = np.array(trajectory_level_rewards)
        non_tensor_batch["task_success_labels"] = np.array(task_success_labels)
        non_tensor_batch["task_num_turns"] = np.array(task_num_turns)
        non_tensor_batch["records"] = np.array(
            postprocessing_outputs["json_string_trajectories"], 
            dtype=object,
        )

        # Match with prompt/without prompt outputs
        for key in [
            "responses",
            "response_mask",
            "loss_mask"
        ]:
            assert torch.equal(
                postprocessing_outputs[key],
                post_processing_outputs_original_system_prompt[key],
            )

            assert torch.equal(
                postprocessing_outputs[key],
                post_processing_outputs_custom_system_prompt[key],
            )

        # Generate tensor batch
        tensor_batch_kwargs = {}
        for key in [
            "prompts", 
            "responses", 
            "response_mask", 
            "input_ids", 
            "attention_mask", 
            "position_ids",
            "loss_mask",
        ]:
            tensor_batch_kwargs[key] = postprocessing_outputs[key]
            tensor_batch_kwargs[f"{key}_with_system_prompts_as_is"] = (
                post_processing_outputs_original_system_prompt[key]
            )
            tensor_batch_kwargs[f"{key}_with_custom_system_prompt"] = (
                post_processing_outputs_custom_system_prompt[key]
            )
        
        tensor_batch = TensorDict(
            tensor_batch_kwargs,
            batch_size=len(all_trajectories_for_training),
        )

        # free vllm cache engine
        if (
            vllm_version
            in (
                "0.5.4",
                "0.6.3",
            )
            and self.config.free_cache_engine
        ):
            self.inference_engine.free_cache_engine()

        return DataProto(batch=tensor_batch, non_tensor_batch=non_tensor_batch)