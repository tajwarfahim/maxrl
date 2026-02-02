from typing import List, Dict, Union, Optional, Any
from copy import deepcopy

from verl.paprika.environments.base_env import BaseEnv
from verl.utils.reward_score.countdown import compute_score

COUNTDOWN_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
COUNTDOWN_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0


class CountdownEnv(BaseEnv):
    """
    This class contains the logic for the game of Countdown.
    Code adopted from this codebase: https://github.com/Jiayi-Pan/TinyZero
    """

    custom_system_prompt_str = (
        "You are a helpful assistant. "
        "You first think about the reasoning process in the mind and "
        "then provide the user with the answer."
    )

    default_system_prompt_str = (
        "You are a helpful assistant. "
        "You first think about the reasoning process in the mind and "
        "then provide the user with the answer."
    )

    def __init__(
        self,
        task_state: Dict[str, Any],
        mode: str = "train",
    ):
        assert "env" in task_state
        self.goal_state = deepcopy(task_state["env"])

        # goal state = target number
        assert isinstance(self.goal_state, int)

        assert "agent" in task_state
        self.start_state = deepcopy(task_state["agent"])
        
        # start state = list of numbers that the model needs to work with
        assert isinstance(self.start_state, list)
        for num in self.start_state:
            assert isinstance(num, int)

        self.mode = mode
        assert self.mode in ["train", "test"]

        self.trajectory_level_reward = COUNTDOWN_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 1024

    def get_start_state(self) -> str:
        start_state_str = (
            "Using the numbers {numbers}, create an equation that equals {target}. "
            "You can use basic arithmetic operations (+, -, *, /) "
            "and each number can only be used once. "
            "Show your work in <think> </think> tags. "
            "And return the final answer in <answer> </answer> tags, "
            "for example <answer> (1 + 2) / 3 </answer>. "
            "Think step by step and the provide a solution."
        )
        
        start_state_str = start_state_str.format(
            numbers=self.start_state,
            target=self.goal_state,
        )

        return start_state_str
        
    def get_max_turns(self) -> int:
        return 1
    
    def get_custom_system_prompt(
       self     
    ) -> str:
        return self.custom_system_prompt_str
    
    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_system_prompt(self) -> str:
        return self.custom_system_prompt_str

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

        score = compute_score(
            solution_str=last_assistant_response,
            ground_truth={
                "target": self.goal_state,
                "numbers": self.start_state,
            },
        )

        if score == 1:
            feedback = "Goal reached"
            self.trajectory_level_reward = COUNTDOWN_DEFAULT_REWARD_FOR_SOLVED_TASK
        
        else:
            feedback = "You did not write a correct solution, better luck next time!"
            self.trajectory_level_reward = COUNTDOWN_DEFAULT_REWARD_FOR_UNSOLVED_TASK
        
        return {
            "content": feedback,
            "goal_reached": (feedback == "Goal reached"),
            "judge_label": (feedback == "Goal reached"),
        }