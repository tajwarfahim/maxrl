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

from collections import defaultdict
from typing import List, Optional, Dict, Any
from math_verify import verify

import torch

from verl import DataProto
from verl.utils.reward_score import default_compute_score
from verl.workers.reward_manager import register
from verl.utils.reward_score.math_verify import (
    extract_solution,
)


def most_frequent_equivalent_answer(answers: list[str]) -> str | None:
    """
    Given a list of answer strings, return the most frequent answer
    up to mathematical equivalence using math-verify.

    Returns None if the list is empty.
    """
    if not answers:
        return None

    groups: list[list[str]] = []

    for ans in answers:
        placed = False
        for group in groups:
            # Compare against representative of the group
            if verify(ans, group[0]):
                group.append(ans)
                placed = True
                break

        if not placed:
            groups.append([ans])

    # Select the group with maximum frequency
    largest_group = max(groups, key=len)

    # Return a representative (first element)
    return largest_group[0]


@register("naive")
class NaiveRewardManager:
    """The reward manager."""
    def __init__(
        self,
        tokenizer,
        num_examine: int,
        compute_score=None,
        reward_fn_key: str = "data_source",
    ) -> None:
        """
        Args:
            tokenizer: tokenizer for decoding tokens.
            num_examine: how many samples to print for debugging.
            compute_score: reward scoring function.
            reward_fn_key: non-tensor key containing data_source.
            accuracy_intervals: list of accuracy intervals.
        """
        self.tokenizer = tokenizer
        self.num_examine = num_examine
        self.compute_score = compute_score or default_compute_score
        self.reward_fn_key = reward_fn_key

        accuracy_intervals = [(0.0, 0.0)]

        low = 0
        n = 10
        while n >= 0:
            high = 2.0 ** (-n)
            accuracy_intervals.append((low, high))

            low = high
            n = n - 1

        accuracy_intervals.append((1.0, 1.0))

        self.accuracy_intervals = accuracy_intervals

    def _extract_answer(self, text: str) -> Optional[str]:
        # Uses your existing extraction util; normalize lightly
        ans = extract_solution(text)

        if ans is None:
            return None
        
        ans = str(ans).strip()

        return ans if ans else None
    
    def _normalize_answer(self, ans: str) -> str:
        # minimal normalization; adjust if needed (lowercasing can be risky for some tasks)
        return ans.strip()

    # -------------------------------------------------------------------------
    # ✓ Extract accuracy from the score object
    # -------------------------------------------------------------------------
    def _extract_accuracy(self, score: Any) -> Optional[float]:
        if isinstance(score, dict):
            if "accuracy" in score:
                return float(score["accuracy"])
            if "score" in score:
                return float(score["score"])
            return None
        if isinstance(score, (int, float)):
            return float(score)
        return None

    # -------------------------------------------------------------------------
    # ✓ Compute fractions for accuracy intervals
    # -------------------------------------------------------------------------
    def _compute_accuracy_interval_fractions(
        self, accuracies: List[float]
    ) -> Dict[str, float]:

        if not accuracies:
            result = {}
            for i, (low, high) in enumerate(self.accuracy_intervals):
                if (
                    i == 0 
                    or i == len(self.accuracy_intervals) - 1
                ):
                    label = f"[{low}, {high}]"

                elif i == len(self.accuracy_intervals) - 2:
                    label = f"({low}, {high})"

                else:
                    label = f"({low}, {high}]"

                result[label] = 0.0
            return result

        counts = [0 for _ in self.accuracy_intervals]
        n = len(accuracies)

        for acc in accuracies:
            for idx, (low, high) in enumerate(self.accuracy_intervals):
                in_interval = False

                if idx == 0:
                    in_interval = (acc == 0.0)


                elif idx == len(self.accuracy_intervals) - 1:
                    in_interval = (acc == 1.0)

                # bigger interval
                else:
                    is_second_to_last = (idx == len(self.accuracy_intervals) - 2)

                    greater_than_lower_bound = (acc > low)
                    less_than_higher_bound = (acc < high)
                    less_than_or_equal_to_higher_bound = (acc <= high)

                    if is_second_to_last:
                        in_interval = (
                            greater_than_lower_bound
                            and less_than_higher_bound
                        )

                    else:
                        in_interval = (
                            greater_than_lower_bound
                            and less_than_or_equal_to_higher_bound
                        )

                if in_interval:
                    counts[idx] += 1
                    break

        result = {}
        for i, (low, high) in enumerate(self.accuracy_intervals):
            if (
                i == 0 
                or i == len(self.accuracy_intervals) - 1
            ):
                label = f"[{low}, {high}]"

            elif i == len(self.accuracy_intervals) - 2:
                label = f"({low}, {high})"

            else:
                label = f"({low}, {high}]"

            result[label] = counts[i] / n

        return result

    # -------------------------------------------------------------------------
    # ✓ Main __call__
    # -------------------------------------------------------------------------
    def __call__(self, data: DataProto, return_dict: bool = False):

        # shortcut: RM score fully provided
        if "rm_scores" in data.batch.keys():
            if return_dict:
                return {"reward_tensor": data.batch["rm_scores"]}
            return data.batch["rm_scores"]

        reward_tensor = torch.zeros_like(data.batch["responses"], dtype=torch.float32)
        reward_extra_info: Dict[str, list] = defaultdict(list)

        already_print_data_sources = {}

        # ---------------------------------------------------------
        # Track accuracies per prompt, grouped by data_source
        # prompt_to_accuracies[data_source][prompt_key] = list of accuracies
        # ---------------------------------------------------------
        prompt_to_accuracies = defaultdict(lambda: defaultdict(list))

        # prompt_to_answers[data_source][prompt_key] = list of extracted answers (strings)
        prompt_to_answers = defaultdict(lambda: defaultdict(list))

        # prompt_to_gt_answer[data_source][prompt_key] = extracted ground-truth answer
        prompt_to_gt_answer = defaultdict(dict)

        for i in range(len(data)):
            data_item = data[i]

            prompt_ids = data_item.batch["prompts"]
            prompt_len = prompt_ids.shape[-1]
            attn_mask = data_item.batch["attention_mask"]

            valid_prompt_len = attn_mask[:prompt_len].sum()
            valid_prompt_ids = prompt_ids[-valid_prompt_len:]

            response_ids = data_item.batch["responses"]
            valid_resp_len = attn_mask[prompt_len:].sum()
            valid_resp_ids = response_ids[:valid_resp_len]

            prompt_str = self.tokenizer.decode(valid_prompt_ids, skip_special_tokens=True)
            response_str = self.tokenizer.decode(valid_resp_ids, skip_special_tokens=True)

            ground_truth = data_item.non_tensor_batch["reward_model"]["ground_truth"]
            data_source = data_item.non_tensor_batch[self.reward_fn_key]
            extra_info = data_item.non_tensor_batch.get("extra_info")

            score = self.compute_score(
                data_source=data_source,
                solution_str=response_str,
                ground_truth=ground_truth,
                extra_info=extra_info,
            )

            # reward
            if isinstance(score, dict):
                reward = score["score"]
                for k, v in score.items():
                    reward_extra_info[k].append(v)
            else:
                reward = score

            reward_tensor[i, valid_resp_len - 1] = reward

            # accuracy per response
            acc = self._extract_accuracy(score)
            if acc is not None:
                prompt_key = data_item.non_tensor_batch.get("prompt_id", prompt_str)
                prompt_to_accuracies[data_source][prompt_key].append(float(acc))

            # printing examples
            if data_source not in already_print_data_sources:
                already_print_data_sources[data_source] = 0

            if already_print_data_sources[data_source] < self.num_examine:
                already_print_data_sources[data_source] += 1
                print("[prompt]", prompt_str)
                print("[response]", response_str)
                print("[ground_truth]", ground_truth)
                if isinstance(score, dict):
                    for k, v in score.items():
                        print(f"[{k}]", v)
                else:
                    print("[score]", score)

            prompt_key = data_item.non_tensor_batch.get("prompt_id", prompt_str)

            # Extract prediction answer
            pred_ans = self._extract_answer(response_str)
            if pred_ans is not None:
                prompt_to_answers[data_source][prompt_key].append(self._normalize_answer(pred_ans))

            # Extract & store GT answer once per prompt
            if prompt_key not in prompt_to_gt_answer[data_source]:
                if ground_truth is not None:
                    prompt_to_gt_answer[data_source][prompt_key] = self._normalize_answer(ground_truth)

                else:
                    raise ValueError("No GT answer!")

        # ---------------------------------------------------------
        # ✓ Compute per-prompt accuracies (mean over responses)
        # ---------------------------------------------------------
        # global list (all prompts across data sources)
        all_prompt_accuracies = []

        # group results: { "data_source/[low,high)" : frac }
        per_ds_interval_fractions = {}

        for ds, prompts in prompt_to_accuracies.items():
            per_prompt_accs = []

            for prompt_key, accs in prompts.items():
                if accs:
                    per_prompt_accs.append(sum(accs) / len(accs))
                    all_prompt_accuracies.append(sum(accs) / len(accs))

            # compute fractions for this data_source
            frac_dict = self._compute_accuracy_interval_fractions(per_prompt_accs)

            # flatten keys as "data_source/interval"
            for interval_label, frac in frac_dict.items():
                key = f"{ds}/{interval_label}"
                per_ds_interval_fractions[key] = frac

        # global interval fractions (all prompts)
        global_interval_fractions = self._compute_accuracy_interval_fractions(
            all_prompt_accuracies
        )

        # Calculate majority voting metrics
        per_ds_majority_vote_accuracy = {}
        global_mv_correct = 0
        global_mv_total = 0

        for ds, prompts in prompt_to_answers.items():
            ds_correct = 0
            ds_total = 0

            for prompt_key, ans_list in prompts.items():
                gt = prompt_to_gt_answer[ds].get(prompt_key)
                if not gt or not ans_list:
                    raise ValueError("Ground truth not found for this prompt!")

                # mode (most frequent extracted answer)
                most_frequent_answer = most_frequent_equivalent_answer(
                    answers=ans_list,
                )

                ds_total += 1
                global_mv_total += 1

                if verify(most_frequent_answer, gt):
                    ds_correct += 1
                    global_mv_correct += 1

            per_ds_majority_vote_accuracy[ds] = (ds_correct / ds_total) if ds_total else 0.0

        global_majority_vote_accuracy = (global_mv_correct / global_mv_total) if global_mv_total else 0.0

        if return_dict:
            return {
                "reward_tensor": reward_tensor,
                "reward_extra_info": reward_extra_info,
                "accuracy_interval_fractions_per_prompt_global": (
                    global_interval_fractions
                ),
                "accuracy_interval_fractions_per_prompt_per_datasource": (
                    per_ds_interval_fractions
                ),
                "majority_vote_accuracy_global": global_majority_vote_accuracy,
                "majority_vote_accuracy_per_datasource": per_ds_majority_vote_accuracy,
            }

        return reward_tensor