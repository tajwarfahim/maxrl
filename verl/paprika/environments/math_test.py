from typing import Dict, List, Union, Optional, Any
from copy import deepcopy

from verl.paprika.environments.base_env import BaseEnv
from verl.utils.reward_score.math_verify import compute_score


MATH_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
MATH_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0


class Math(BaseEnv):
    default_system_prompt_str = "Please reason step by step, and put your final answer within \\boxed{}. "

    def __init__(
        self,
        task_state: Dict[str, Any],
        mode: str = "train",
    ):
        assert "env" in task_state
        self.goal_state = deepcopy(task_state["env"])
        self.start_state = deepcopy(task_state["agent"])
        self.mode = mode
        self.trajectory_level_reward = MATH_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_custom_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str

    def get_start_state(self) -> str:
        return self.start_state
    
    def get_max_turns(self) -> int:
        return 1
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 3072
    
    def step(
        self,
        conversation_history: List[Dict[str, str]],
    ) -> Dict[str, Union[str, bool]]:
        self.validate_conversation_history(
            conversation_history=conversation_history,
        )

        # Preliminary checks on the conversation_history
        assert len(conversation_history) >= 2

        assert conversation_history[-1]["role"] == "assistant"
        last_assistant_response = conversation_history[-1]["content"]

        ret_score = compute_score(
            model_output=last_assistant_response,
            ground_truth=self.goal_state,
        )

        if ret_score == 1.0:
            feedback = "Goal reached"
            self.trajectory_level_reward = MATH_DEFAULT_REWARD_FOR_SOLVED_TASK

        else:
            feedback = (
                "Sorry, you have made a mistake, "
                "your solution did not reach the correct answer!"
            )
            self.trajectory_level_reward = MATH_DEFAULT_REWARD_FOR_UNSOLVED_TASK

        return {
            "content": feedback,
            "goal_reached": (feedback == "Goal reached"),
            "judge_label": (feedback == "Goal reached"),
        }