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
Rollout with huggingface models.
TODO: refactor this class. Currently, it will hang when using FSDP HybridShard. We should actually create a single
GPU model. Then, get full state_dict and bind the state_dict to the single GPU model. Then, use the single GPU model
to perform generation.
"""

import contextlib
import logging

import torch
import torch.distributed
from tensordict import TensorDict
from torch import nn
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from transformers import GenerationConfig
from tqdm import tqdm

logger = logging.getLogger(__name__)

from verl import DataProto
from verl.utils.device import get_device_name, get_torch_device
from verl.utils.torch_functional import get_response_mask

from .base import BaseRollout

__all__ = ["HFRollout"]


class HFRollout(BaseRollout):
    def __init__(self, module: nn.Module, config):
        super().__init__()
        self.config = config
        self.module = module

    def generate_sequences(self, prompts: DataProto) -> DataProto:
        batch_size = prompts.batch.batch_size[0]  # 当前卡处理的batch数（单卡）
        is_validate = prompts.meta_info.get("validate", False)
        
        # micro_batch_size永远表示sample level
        # 在validation阶段：val_kwargs.n已经提前展平，所以batch_size已经是sample level
        # 在train阶段：batch_size是prompt level，需要除以rollout.n得到prompt batch size
        micro_batch_size_sample_level = self.config.get("micro_batch_size", batch_size)
        
        if is_validate:
            # validation阶段：batch_size已经是sample level（val_kwargs.n已展平）
            # num_return_sequences=1，所以micro_batch_size直接使用
            effective_batch_size = batch_size
            effective_micro_batch_size = micro_batch_size_sample_level
        else:
            # train阶段：batch_size是prompt level，需要转换为prompt batch size
            # 因为每个prompt会生成rollout.n个samples，所以prompt batch size = sample batch size / rollout.n
            rollout_n = self.config.get("n", 1)
            effective_batch_size = batch_size  # prompt level
            effective_micro_batch_size = max(micro_batch_size_sample_level // rollout_n, 1)  # prompt level
        
        num_chunks = max(effective_batch_size // effective_micro_batch_size, 1)  # 当前卡需要分多少轮
        batch_prompts = prompts.chunk(chunks=num_chunks)
        
        # 获取分布式信息
        if torch.distributed.is_initialized():
            rank = torch.distributed.get_rank()
            world_size = torch.distributed.get_world_size()
        else:
            rank = 0
            world_size = 1
        
        # 添加tqdm进度条，显示总batch数、总轮数、当前轮数
        # 注意：micro_batch_size永远表示sample level
        # 在数据并行模式下，每张卡会收到总batch的一部分（通过DP_COMPUTE_PROTO分发）
        # 然后每张卡内部再按照effective_micro_batch_size分chunks处理
        output = []
        if world_size > 1:
            # 多卡情况：显示当前GPU的信息
            if is_validate:
                desc = f"HFRollout[GPU {rank}/{world_size-1}] (val): {effective_batch_size} samples on this GPU, {num_chunks} rounds"
            else:
                desc = f"HFRollout[GPU {rank}/{world_size-1}] (train): {effective_batch_size} prompts on this GPU, {num_chunks} rounds"
        else:
            # 单卡情况
            if is_validate:
                desc = f"HFRollout (val): {effective_batch_size} samples in {num_chunks} rounds"
            else:
                desc = f"HFRollout (train): {effective_batch_size} prompts in {num_chunks} rounds"
        
        # 只在rank 0显示进度条，避免多行输出混乱
        # 注意：每张GPU都会独立处理自己的数据分片，并按照effective_micro_batch_size分chunks
        with tqdm(total=num_chunks, desc=desc, unit="round", disable=(rank != 0)) as pbar:
            for round_idx, p in enumerate(batch_prompts, 1):
                postfix_dict = {
                    "round": f"{round_idx}/{num_chunks}",
                    "batches_per_gpu": effective_batch_size,
                    "micro_batch_size": effective_micro_batch_size,
                    "micro_batch_size_sample_level": micro_batch_size_sample_level,
                }
                if not is_validate:
                    postfix_dict["rollout_n"] = self.config.get("n", 1)
                if world_size > 1:
                    postfix_dict["world_size"] = world_size
                pbar.set_postfix(postfix_dict)
                output.append(self._generate_minibatch(p))
                pbar.update(1)
        
        output = DataProto.concat(output)
        return output

    @torch.no_grad()
    def _generate_minibatch(self, prompts: DataProto) -> DataProto:
        # make sampling args can be overridden by inputs
        do_sample = prompts.meta_info.get("do_sample", self.config.do_sample)
        is_validate = prompts.meta_info.get("validate", False)

        temperature = prompts.meta_info.get("temperature", self.config.temperature)
        response_length = prompts.meta_info.get("response_length", self.config.response_length)
        top_p = prompts.meta_info.get("top_p", self.config.get("top_p", 1.0))
        top_k = max(0, prompts.meta_info.get("top_k", self.config.get("top_k", 0)))  # to be compatible with vllm

        if not do_sample:
            # do_sample==False -> greedy decoding
            kwargs = {
                "do_sample": False,
                "num_beams": 1,
            }
        elif is_validate:
            # do validate and do sample -> use val_kwargs
            kwargs = {
                "do_sample": True,
                "num_beams": 1,
                "top_k": max(0, self.config.val_kwargs.top_k),  # to be compatible with vllm
                "top_p": self.config.val_kwargs.top_p,
                "temperature": self.config.val_kwargs.temperature,
                "num_return_sequences": 1,  # if validate, already repeat in ray_trainer
            }
        else:
            # do_sample -> use rollout config
            kwargs = {
                "do_sample": True,
                "num_beams": 1,
                "top_p": top_p,
                "top_k": top_k,
                "temperature": temperature,
                "num_return_sequences": self.config.n,
            }

        # make config according to generate mode
        generation_config = GenerationConfig(**kwargs)

        idx = prompts.batch["input_ids"]  # (bs, prompt_length)
        prompt_length = idx.size(1)
        attention_mask = prompts.batch["attention_mask"]  # left-padded attention_mask
        position_ids = prompts.batch["position_ids"]

        # used to construct attention_mask
        eos_token_id = prompts.meta_info["eos_token_id"]
        pad_token_id = prompts.meta_info["pad_token_id"]

        self.module.eval()
        param_ctx = contextlib.nullcontext()

        is_fsdp = isinstance(self.module, FSDP)
        print(f"[HFRollout] Module is FSDP: {is_fsdp}", flush=True)
        
        if is_fsdp:
            # NOTE: recurse=True is required to summon all submodule params for correct generation
            # The original recurse=False caused incorrect outputs because submodule params were not summoned
            print("[HFRollout] Creating summon_full_params context with recurse=True", flush=True)
            param_ctx = FSDP.summon_full_params(self.module, writeback=False, recurse=True)
        
        from verl.utils.torch_dtypes import PrecisionType
        torch_dtype = PrecisionType.to_dtype(self.config.get("dtype", "bfloat16"))
        
        with param_ctx, torch.autocast(device_type=get_device_name(), dtype=torch_dtype):
            # Log parameter stats after entering summon context
            total_params = sum(p.numel() for p in self.module.parameters())
            non_zero_params = sum((p != 0).sum().item() for p in self.module.parameters())
            first_param = next(self.module.parameters())
            print(f"[HFRollout] Inside param context - total_params: {total_params:,}, "
                  f"non_zero_params: {non_zero_params:,}, "
                  f"first_param shape: {first_param.shape}, "
                  f"first_param mean: {first_param.mean().item():.6f}, "
                  f"first_param std: {first_param.std().item():.6f}", flush=True)
            
            print(f"[HFRollout] Starting generate with eos_token_id={eos_token_id}, "
                  f"pad_token_id={pad_token_id}, max_new_tokens={response_length}, "
                  f"do_sample={do_sample}, temperature={temperature}", flush=True)
            
            # NOTE: Do NOT pass position_ids - HuggingFace generate computes them automatically
            # Passing explicit position_ids can cause issues with generation
            output = self.module.generate(
                input_ids=idx,
                attention_mask=attention_mask,
                # position_ids=position_ids,  # Removed: causes generation issues
                do_sample=do_sample,
                max_new_tokens=response_length,
                eos_token_id=eos_token_id,
                pad_token_id=pad_token_id,
                generation_config=generation_config,
                output_scores=False,  # this is potentially very large
                return_dict_in_generate=True,
                use_cache=True,
            )

        # TODO: filter out the seq with no answers like ds-chat
        seq = output.sequences
        generated_batch_size = seq.size(0)  # bs * num_return_sequences
        
        # Log generation results
        logger.info(f"[HFRollout] Generation complete - output shape: {seq.shape}, "
                   f"generated_batch_size: {generated_batch_size}")

        # huggingface generate will stop generating when all the batch reaches [EOS].
        # We have to pad to response_length
        sequence_length = prompt_length + self.config.response_length
        delta_length = sequence_length - seq.shape[1]

        if delta_length > 0:
            delta_tokens = torch.ones(size=(generated_batch_size, delta_length), device=seq.device, dtype=seq.dtype)
            delta_tokens = pad_token_id * delta_tokens
            seq = torch.cat((seq, delta_tokens), dim=1)
        assert seq.shape[1] == sequence_length

        # make necessary reputations if num_return_sequences > 1
        num_return_sequences = kwargs.get("num_return_sequences", 1)
        if num_return_sequences > 1:
            position_ids = position_ids.repeat_interleave(num_return_sequences, dim=0)
            attention_mask = attention_mask.repeat_interleave(num_return_sequences, dim=0)

        prompt = seq[:, :prompt_length]  # (generated_batch_size, prompt_length)
        response = seq[:, prompt_length:]  # (generated_batch_size, response_length)

        response_length = response.size(1)
        delta_position_id = torch.arange(1, response_length + 1, device=position_ids.device)
        delta_position_id = delta_position_id.unsqueeze(0).repeat(generated_batch_size, 1)

        response_position_ids = position_ids[:, -1:] + delta_position_id
        position_ids = torch.cat([position_ids, response_position_ids], dim=-1)

        response_attention_mask = get_response_mask(response_id=response, eos_token=eos_token_id, dtype=attention_mask.dtype)
        attention_mask = torch.cat((attention_mask, response_attention_mask), dim=-1)

        batch = TensorDict(
            {
                "prompts": prompt,
                "responses": response,
                "input_ids": seq,
                "attention_mask": attention_mask,
                "position_ids": position_ids,
            },
            batch_size=generated_batch_size,
        )

        # empty cache before compute old_log_prob
        get_torch_device().empty_cache()

        self.module.train()
        return DataProto(batch=batch)
