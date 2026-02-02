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

from typing import Optional

try:
    from math_verify.errors import TimeoutException
    from math_verify.metric import math_metric
    from math_verify.parser import ExprExtractionConfig, LatexExtractionConfig
except ImportError:
    raise RuntimeError(
        "To use Math-Verify, please install it first: pip install math-verify"
    )

from verl.utils.reward_score.math import (
    last_boxed_only_string,
    remove_boxed,
)

# -----------------------------------------------------------------------------
# NOTE:
# - math_metric MUST be created once per Ray actor process
# - This function MUST NOT be called directly in the main process
# -----------------------------------------------------------------------------


class MathVerifyScorer:
    """
    One instance per Ray actor process.
    """

    def __init__(self):
        self._verify_func = math_metric(
            gold_extraction_target=(LatexExtractionConfig(),),
            pred_extraction_target=(ExprExtractionConfig(), LatexExtractionConfig()),
        )

    def compute_score(
        self,
        model_output: str,
        ground_truth: str,
        timeout_score: float = 0.0,
    ) -> float:
        """
        Safe to call repeatedly inside a Ray actor.
        """

        ground_truth_boxed = f"\\boxed{{{ground_truth}}}"

        try:
            score, _ = self._verify_func(
                [ground_truth_boxed],
                [model_output],
            )
            return float(score)

        except TimeoutException:
            return float(timeout_score)

        except Exception:
            return 0.0

