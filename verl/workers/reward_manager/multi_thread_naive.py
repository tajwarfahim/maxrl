# Copyright 2024 Bytedance Ltd.
# Licensed under the Apache License, Version 2.0

from __future__ import annotations

from collections import defaultdict
from typing import List, Dict, Any, Tuple, Set, Optional
import time
import signal

import ray
import torch
from math_verify import verify

from verl import DataProto
from verl.workers.reward_manager import register
from verl.utils.reward_score.math_verify import extract_solution

# -----------------------------------------------------------------------------
# math_verify imports
# -----------------------------------------------------------------------------
try:
    from math_verify.errors import TimeoutException
    from math_verify.metric import math_metric
    from math_verify.parser import ExprExtractionConfig, LatexExtractionConfig
except ImportError:
    raise RuntimeError("Please install math-verify: pip install math-verify")


# =============================================================================
# Per-item timeout helpers (actor-local)
# =============================================================================

class _ItemTimeout(Exception):
    pass


def _alarm_handler(signum, frame):
    raise _ItemTimeout


# =============================================================================
# MathVerify scorer (ONE per actor process)
# =============================================================================

class MathVerifyScorer:
    def __init__(self):
        self._verify_func = math_metric(
            gold_extraction_target=(LatexExtractionConfig(),),
            pred_extraction_target=(ExprExtractionConfig(), LatexExtractionConfig()),
        )

    def compute_score(
        self,
        model_output: str,
        ground_truth_unboxed: str,
        timeout_score: float,
        per_item_timeout_s: int,
    ) -> float:
        # math_metric expects boxed GT
        gt_boxed = f"\\boxed{{{ground_truth_unboxed}}}"

        # hard per-item timeout
        signal.signal(signal.SIGALRM, _alarm_handler)
        signal.alarm(per_item_timeout_s)
        try:
            score, _ = self._verify_func([gt_boxed], [model_output])
            return float(score)
        except _ItemTimeout:
            return float(timeout_score)
        except TimeoutException:
            return float(timeout_score)
        except Exception:
            return 0.0
        finally:
            signal.alarm(0)


# =============================================================================
# Ray actor
# =============================================================================

@ray.remote(
    max_restarts=0,
    max_task_retries=0,
)
class RewardScoreActor:
    def __init__(self):
        self._scorer = MathVerifyScorer()

    def compute_scores_batch(
        self,
        batch: List[Tuple[int, str, str]],  # (item_idx, response_str, ground_truth_unboxed)
        timeout_score: float,
        per_item_timeout_s: int,
    ) -> List[Tuple[int, Dict[str, float]]]:
        out: List[Tuple[int, Dict[str, float]]] = []
        for item_idx, response_str, ground_truth in batch:
            score = self._scorer.compute_score(
                response_str,
                ground_truth,
                timeout_score,
                per_item_timeout_s,
            )

            out.append((item_idx, {"score": float(score), "accuracy": float(score)}))
        return out


# =============================================================================
# Majority voting helper
# =============================================================================

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


# Helper to get the number of reward actors
def get_num_reward_actors(
    cpu_per_actor: float = 1.0,
    max_actors: Optional[int] = None,
    min_actors: int = 1,
) -> int:
    resources = ray.available_resources()
    num_cpus = int(resources.get("CPU", 0))

    if num_cpus <= 0:
        return min_actors

    n = int(num_cpus // cpu_per_actor)

    if max_actors is not None:
        n = min(n, max_actors)

    return max(n, min_actors)


# =============================================================================
# Reward Manager
# =============================================================================

@register("multi_thread")
class MultiThreadNaiveRewardManager:
    def __init__(
        self,
        tokenizer,
        num_examine: int,
        compute_score=None,
        reward_fn_key: str = "data_source",
        num_reward_actors: Optional[int] = 16,
        batch_size: int = 8,
        in_flight_batches_per_actor: int = 4,
        per_item_timeout_s: int = 1,
        per_batch_timeout_s: float = 10.0,
        poll_interval_s: float = 0.5,
        timeout_score: float = 0.0,
    ):
        self.tokenizer = tokenizer
        self.num_examine = num_examine
        self.reward_fn_key = reward_fn_key

        self._batch_size = int(batch_size)
        self._timeout_score = float(timeout_score)
        self._per_item_timeout_s = int(per_item_timeout_s)
        self._per_batch_timeout_s = float(per_batch_timeout_s)
        self._poll_interval_s = float(poll_interval_s)

        if isinstance(num_reward_actors, int):
            self.num_reward_actors = num_reward_actors

        else:
            self.num_reward_actors = int(get_num_reward_actors())

        print("\nReward model is using this many reward actors: ", self.num_reward_actors, "\n")

        self._actors = [RewardScoreActor.remote() for _ in range(self.num_reward_actors)]
        self._next_actor = 0
        self._max_inflight_batches = self.num_reward_actors * in_flight_batches_per_actor

        # same interval scheme as earlier versions
        accuracy_intervals = [(0.0, 0.0)]
        low = 0.0
        n_pow = 10
        while n_pow >= 0:
            high = 2.0 ** (-n_pow)
            accuracy_intervals.append((low, high))
            low = high
            n_pow -= 1
        accuracy_intervals.append((1.0, 1.0))
        self.accuracy_intervals = accuracy_intervals

    def _pick_actor(self):
        a = self._actors[self._next_actor]
        self._next_actor = (self._next_actor + 1) % len(self._actors)
        return a

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

    def __call__(self, data: DataProto, return_dict: bool = False):
        # preserve shortcut behavior
        if "rm_scores" in data.batch.keys():
            if return_dict:
                return {"reward_tensor": data.batch["rm_scores"]}
            return data.batch["rm_scores"]

        reward_tensor = torch.zeros_like(data.batch["responses"], dtype=torch.float32)
        reward_extra_info: Dict[str, list] = defaultdict(list)

        # logging counters
        num_item_timeouts = 0
        num_batch_timeouts = 0
        num_batch_exceptions = 0
        num_batches_ok = 0

        already_print_data_sources: Dict[str, int] = {}

        prompt_to_accuracies = defaultdict(lambda: defaultdict(list))
        prompt_to_answers = defaultdict(lambda: defaultdict(list))
        prompt_to_gt_answer = defaultdict(dict)

        n = len(data)

        # decode once
        items: List[Dict[str, Any]] = []
        for i in range(n):
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
            prompt_key = data_item.non_tensor_batch.get("prompt_id", prompt_str)

            items.append(
                dict(
                    i=i,
                    response=response_str,
                    ground_truth=ground_truth,
                    data_source=data_source,
                    prompt_key=prompt_key,
                    prompt_str=prompt_str,
                    valid_resp_len=valid_resp_len,
                )
            )

        # batching scheduler
        pending: Set[ray.ObjectRef] = set()
        start_time: Dict[ray.ObjectRef, float] = {}
        ref_to_batch: Dict[ray.ObjectRef, List[int]] = {}
        results: Dict[int, Dict[str, float]] = {}

        next_i = 0

        def submit_one_batch():
            nonlocal next_i
            if next_i >= n:
                return

            batch: List[int] = []
            while next_i < n and len(batch) < self._batch_size:
                batch.append(next_i)
                next_i += 1

            payload = [(i, items[i]["response"], items[i]["ground_truth"]) for i in batch]
            ref = self._pick_actor().compute_scores_batch.remote(
                payload,
                self._timeout_score,
                self._per_item_timeout_s,
            )

            pending.add(ref)
            start_time[ref] = time.time()
            ref_to_batch[ref] = batch

        # prime inflight
        while len(pending) < self._max_inflight_batches and next_i < n:
            submit_one_batch()

        # gather
        while pending:
            ready, _ = ray.wait(list(pending), num_returns=1, timeout=self._poll_interval_s)
            now = time.time()

            for ref in ready:
                pending.remove(ref)
                batch = ref_to_batch.pop(ref)
                start_time.pop(ref, None)

                try:
                    pairs = ray.get(ref)
                    num_batches_ok += 1
                    for idx, out in pairs:
                        results[idx] = out
                        # count per-item timeouts precisely: if accuracy=0 and score==timeout_score
                        # (this will also count genuine wrong answers when timeout_score==0).
                        # For better diagnostics, track timeout_score hits only if score==timeout_score AND per_item_timeout_s>0.
                        if out.get("score", None) == self._timeout_score:
                            # can't distinguish "wrong" vs "timed out" when timeout_score==0 without extra signals
                            # but still useful as a rough indicator
                            num_item_timeouts += 1

                except Exception:
                    num_batch_exceptions += 1
                    for i in batch:
                        results[i] = {"score": self._timeout_score, "accuracy": 0.0}

            # batch-level safety timeout (should be rare now)
            for ref in list(pending):
                if now - start_time.get(ref, now) > self._per_batch_timeout_s:
                    pending.remove(ref)
                    batch = ref_to_batch.pop(ref)
                    start_time.pop(ref, None)
                    try:
                        ray.cancel(ref, force=True)
                    except Exception:
                        pass
                    num_batch_timeouts += 1
                    for i in batch:
                        results[i] = {"score": self._timeout_score, "accuracy": 0.0}

            # backfill
            while len(pending) < self._max_inflight_batches and next_i < n:
                submit_one_batch()

        # postprocess + metrics
        for i, info in enumerate(items):
            out = results.get(i, {"score": self._timeout_score, "accuracy": 0.0})
            reward_tensor[i, info["valid_resp_len"] - 1] = float(out["score"])

            ds = info["data_source"]
            pk = info["prompt_key"]
            ground_truth = info["ground_truth"]
            prompt_to_accuracies[ds][pk].append(float(out["accuracy"]))

            # examine prints
            if ds not in already_print_data_sources:
                already_print_data_sources[ds] = 0

            if already_print_data_sources[ds] < self.num_examine:
                already_print_data_sources[ds] += 1
                print("[data_source]", ds)
                print("[prompt]", info["prompt_str"])
                print("[response]", info["response"])
                print("[ground_truth]", info["ground_truth"])
                print("[score]", out["score"])
                print("[accuracy]", out["accuracy"])

            response_str = info["response"]

            # Extract prediction answer
            pred_ans = self._extract_answer(response_str)
            if pred_ans is not None:
                prompt_to_answers[ds][pk].append(self._normalize_answer(pred_ans))

            # Extract & store GT answer once per prompt
            if pk not in prompt_to_gt_answer[ds]:
                if ground_truth is not None:
                    prompt_to_gt_answer[ds][pk] = self._normalize_answer(ground_truth)

                else:
                    raise ValueError("No GT answer!")

        # interval fractions per datasource + global
        all_prompt_accuracies: List[float] = []
        per_ds_interval_fractions: Dict[str, float] = {}

        for ds, prompts in prompt_to_accuracies.items():
            per_prompt_accs = []
            for pk, accs in prompts.items():
                if accs:
                    mean_acc = sum(accs) / len(accs)
                    per_prompt_accs.append(mean_acc)
                    all_prompt_accuracies.append(mean_acc)
            frac_dict = self._compute_accuracy_interval_fractions(per_prompt_accs)
            for interval_label, frac in frac_dict.items():
                per_ds_interval_fractions[f"{ds}/{interval_label}"] = frac

        global_interval_fractions = self._compute_accuracy_interval_fractions(all_prompt_accuracies)

        # Calculate majority voting metrics
        per_ds_majority_vote_accuracy = {}
        global_mv_correct = 0
        global_mv_total = 0

        for ds, prompts in prompt_to_answers.items():
            ds_correct = 0
            ds_total = 0

            for prompt_key, ans_list in prompts.items():
                gt = prompt_to_gt_answer[ds].get(prompt_key, None)
                if gt is None:
                    raise ValueError("Ground truth not found for this prompt!")

                ds_total += 1
                global_mv_total += 1

                if len(ans_list) == 0:
                    continue

                # mode (most frequent extracted answer)
                most_frequent_answer = most_frequent_equivalent_answer(
                    answers=ans_list,
                )

                if (
                    most_frequent_answer is not None 
                    and verify(most_frequent_answer, gt)
                ):
                    ds_correct += 1
                    global_mv_correct += 1

            per_ds_majority_vote_accuracy[ds] = (ds_correct / ds_total) if ds_total else 0.0

        global_majority_vote_accuracy = (global_mv_correct / global_mv_total) if global_mv_total else 0.0

        if return_dict:
            return {
                "reward_tensor": reward_tensor,
                "reward_extra_info": reward_extra_info,
                "accuracy_interval_fractions_per_prompt_global": global_interval_fractions,
                "accuracy_interval_fractions_per_prompt_per_datasource": per_ds_interval_fractions,
                "majority_vote_accuracy_global": global_majority_vote_accuracy,
                "majority_vote_accuracy_per_datasource": per_ds_majority_vote_accuracy,
            }

        return reward_tensor

