from verl.utils.reward_score.openmathinst_utils import (
    math_equal,
    extract_answer,
    time_limit,
    TimeoutException,
)

from math_verify import verify, parse
from typing import Union, Tuple,Optional

def math_equal_direct(
    prediction: Union[bool, float, str],
    reference: Union[float, str],
    include_percentage: bool = True,
    tolerance: float = 1e-4,
    timeout: float = 10.0,
    check_antlr_version: bool = False,
) -> bool:
    return math_equal(prediction, reference, include_percentage, tolerance, timeout, check_antlr_version)


def verify_direct(
    gold,
    target,
    float_rounding: int=6,
    numeric_precision: int=15,
    strict: bool=True,
    timeout_seconds: int=3
) -> bool:
    return verify(gold, target, float_rounding, numeric_precision, strict, timeout_seconds)


def eq(a: Optional[str], b: Optional[str]) -> Tuple[bool, bool]:
    if a is None or b is None:
        return False, False

    # Run math_equal with 1.0s timeout (can be slow on complex expressions)
    try:
        with time_limit(1.0):
            omi_correct = math_equal_direct(a, b, check_antlr_version=False, timeout=1.0)

    except (TimeoutException, Exception):
        omi_correct = False

    # Run verify without timeout (already fast)
    try:
        with time_limit(1.0):
            mathv_pred = parse(a)
            mathv_correct = verify_direct(parse(f"\\boxed{{${b}$}}"), mathv_pred)
            
    except (TimeoutException, Exception):
        mathv_correct = False

    return omi_correct, mathv_correct


def compute_score(model_output: str, ground_truth: str, timeout_score: float = 0) -> bool:
    extracted_answer = extract_answer(model_output)
    omi_correct, mathv_correct = eq(extracted_answer, ground_truth)

    ret_score = 0.0
    if omi_correct or mathv_correct:
        ret_score = 1.0

    return ret_score