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

try:
    from math_verify.errors import TimeoutException
    from math_verify.metric import math_metric
    from math_verify.parser import ExprExtractionConfig, LatexExtractionConfig
except ImportError:
    print("To use Math-Verify, please install it first by running `pip install math-verify`.")

from verl.utils.reward_score.math import (
    last_boxed_only_string,
    remove_boxed,
)


def extract_solution(solution_str: str) -> str:
    """Extract the answer from a solution string by finding the last boxed content."""
    solution_substr = last_boxed_only_string(solution_str)
    if solution_substr is None:
        return None
    try:
        box_removed = remove_boxed(solution_substr)
    except:
        box_removed = None

    return box_removed


from verl.utils.reward_score.math import (
    last_boxed_only_string,
    remove_boxed,
)


def compute_score(model_output: str, ground_truth: str, timeout_score: float = 0) -> bool:
    verify_func = math_metric(
        gold_extraction_target=(LatexExtractionConfig(),),
        pred_extraction_target=(ExprExtractionConfig(), LatexExtractionConfig()),
    )
    ret_score = 0.0

    # Wrap the ground truth in \boxed{} format for verification
    ground_truth_boxed = "\\boxed{" + ground_truth + "}"
    try:
        ret_score, _ = verify_func([ground_truth_boxed], [model_output])
    except TimeoutException:
        # TimeoutException may be raised from unexpected places due to signal handler
        ret_score = timeout_score
    except BaseException:
        # Catch all exceptions including those raised during signal handling
        # in unexpected contexts (e.g., weakref cleanup, GC, etc.)
        # Note: TimeoutException inherits from BaseException, not Exception!
        pass

    return ret_score


def extract_solution(solution_str: str) -> str:
    solution_substr = last_boxed_only_string(solution_str)
    if solution_substr is None:
        return None
    try:
        box_removed = remove_boxed(solution_substr)
    except:
        box_removed = None

    return box_removed
