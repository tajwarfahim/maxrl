# Copyright 2024 PRIME team and/or its affiliates
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

import multiprocessing
import time
from typing import Callable, Optional

import torch
from transformers import PreTrainedTokenizer

from verl import DataProto
from verl.utils.reward_score import default_compute_score
from verl.workers.reward_manager import register


def _compute_single_score(args):
    """Worker function for multiprocessing Pool"""
    evaluation_func, task, completion, reference, extra_info = args
    try:
        result = evaluation_func(task, completion, reference, extra_info)
        if isinstance(result, (int, float, bool)):
            return float(result)
        elif isinstance(result, dict):
            return float(result.get("score", 0.0))
        else:
            return float(result[0]) if result else 0.0
    except Exception as e:
        print(f"[Error] Task failed: {e}")
        return 0.0


@register("prime")
class PrimeRewardManager:
    """
    The Reward Manager used in https://github.com/PRIME-RL/PRIME
    Uses a persistent multiprocessing.Pool for parallel reward computation.
    """

    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        num_examine: int,
        compute_score: Optional[Callable] = None,
        reward_fn_key: str = "data_source",
        num_processes: int = 32,
        chunksize: Optional[int] = None,
    ) -> None:
        self.tokenizer = tokenizer
        self.num_examine = num_examine
        self.compute_score = compute_score or default_compute_score
        self.reward_fn_key = reward_fn_key
        self.num_processes = num_processes
        self.chunksize = chunksize  # If None, will compute dynamically
        
        # Create persistent process pool with spawn context
        print(f"[PrimeReward] Creating persistent Pool with {num_processes} processes (spawn context)...")
        t_start = time.time()
        self._mp_context = multiprocessing.get_context("spawn")
        self._pool = self._mp_context.Pool(processes=num_processes)
        print(f"[PrimeReward] Pool created in {time.time() - t_start:.3f}s (will be reused for all batches)")

    def __del__(self):
        """Clean up the process pool when the manager is destroyed"""
        if hasattr(self, '_pool') and self._pool is not None:
            print("[PrimeReward] Closing process pool...")
            self._pool.close()
            self._pool.join()
            print("[PrimeReward] Pool closed.")

    def _run_reward_scoring(self, completions, references, tasks, extra_info=None):
        """
        Parallel reward scoring using the persistent process pool.
        """
        t_total_start = time.time()
        
        if extra_info is None:
            extra_info = [None] * len(tasks)
        
        # Prepare arguments for each task
        t_prep_start = time.time()
        args_list = [
            (self.compute_score, task, completion, reference, ei)
            for task, completion, reference, ei in zip(tasks, completions, references, extra_info)
        ]
        t_prep = time.time() - t_prep_start
        
        try:
            t_map_start = time.time()
            # Use chunksize to reduce IPC overhead: each process gets a batch of tasks at once
            # For lightweight tasks like maze, use larger chunksize to minimize IPC
            if self.chunksize is not None:
                chunksize = self.chunksize
            else:
                # Dynamic: each process gets roughly equal workload
                chunksize = max(1, len(args_list) // self.num_processes)
            scores = self._pool.map(_compute_single_score, args_list, chunksize=chunksize)
            t_map = time.time() - t_map_start
            
            t_total = time.time() - t_total_start
            print(f"[PrimeReward] {len(scores)} scores in {t_total:.3f}s (prep={t_prep:.3f}s, map={t_map:.3f}s, chunksize={chunksize}), mean={sum(scores)/len(scores):.4f}")
            return scores
        except Exception as e:
            print(f"[PrimeReward] ERROR: {e}, falling back to sequential...")
            t_seq_start = time.time()
            scores = [_compute_single_score(args) for args in args_list]
            print(f"[PrimeReward] Sequential: {time.time() - t_seq_start:.3f}s for {len(scores)} scores")
            return scores

    def verify(self, data):
        """
        verify the batch and save as ``acc`` tensor
        """
        prompt_ids = data.batch["prompts"]
        response_ids = data.batch["responses"]
        sequences_str = self.tokenizer.batch_decode(response_ids, skip_special_tokens=True)
        ground_truth = [data_item.non_tensor_batch["reward_model"]["ground_truth"] for data_item in data]
        data_sources = data.non_tensor_batch[self.reward_fn_key]
        extra_info = data.non_tensor_batch.get("extra_info", None)

        assert len(sequences_str) == len(ground_truth) == len(data_sources)
        
        try:
            scores = self._run_reward_scoring(
                completions=sequences_str,
                references=ground_truth,
                tasks=data_sources,
                extra_info=extra_info,
            )
        except Exception as e:
            print(f"[Error] Unexpected error during scoring: {e}. Setting all as 0.")
            scores = [0.0 for _ in range(len(sequences_str))]
        
        data.batch["acc"] = torch.tensor(scores, dtype=torch.float32, device=prompt_ids.device)
        return scores

    def __call__(self, data: DataProto, return_dict: bool = False):
        """We will expand this function gradually based on the available datasets"""

        if "rm_scores" in data.batch.keys():
            if return_dict:
                return {"reward_tensor": data.batch["rm_scores"]}
            return data.batch["rm_scores"]

        reward_tensor = torch.zeros_like(data.batch["responses"], dtype=torch.float32)
        already_print_data_sources = {}

        prompt_ids = data.batch["prompts"]
        prompt_length = prompt_ids.shape[-1]
        response_ids = data.batch["responses"]
        valid_response_length = data.batch["attention_mask"][:, prompt_length:].sum(dim=-1)
        sequences_str = self.tokenizer.batch_decode(response_ids, skip_special_tokens=True)
        data_sources = data.non_tensor_batch["data_source"]

        scores = self.verify(data)

        for i in range(len(data)):
            data_source = data_sources[i]
            reward_tensor[i, valid_response_length[i].item() - 1] = scores[i]

            if data_source not in already_print_data_sources:
                already_print_data_sources[data_source] = 0

            if already_print_data_sources[data_source] < self.num_examine:
                already_print_data_sources[data_source] += 1
                print(sequences_str[i])

        if return_dict:
            return {"reward_tensor": reward_tensor}
        else:
            return reward_tensor
