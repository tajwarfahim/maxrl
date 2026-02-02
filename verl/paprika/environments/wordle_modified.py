import re
from typing import List, Dict, Union, Optional, Any
from copy import deepcopy

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.wordle_modified_config import (
    WORDLE_MODIFIED_WORD_LENGTH_MAP,
    WORDLE_MODIFIED_ENV_DATA,
)

WORDLE_MODIFIED_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
WORDLE_MODIFIED_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0


class WordleModifiedEnv(BaseEnv):
    """
    This class contains the logic for generating feedback for the 
    Wordle game (https://en.wikipedia.org/wiki/Wordle),
    given a guess of the secret word by the LLM or player.

    NOTE: this particular env is a variation of the wordle environment.
    Main difference: instead of guessing a 5 letter word, 
    the agent/player needs to guess a word with variable number of 
    letters. 
    """
    default_system_prompt_str = "You are a helpful assistant."

    letter_positions = {
        0: "First",
        1: "Second",
        2: "Third",
        3: "Fourth",
        4: "Fifth",
        5: "Sixth",
        6: "Seventh",
        7: "Eighth",
        8: "Ninth",
        9: "Tenth",
    }

    def __init__(
        self,
        task_state: Dict[str, Any],
        mode: str = "train",
    ):
        assert "env" in task_state
        self.goal_state = deepcopy(
            task_state["env"]
        ).strip().lower()
        assert self.goal_state.isalpha()

        self.start_state = WORDLE_MODIFIED_WORD_LENGTH_MAP[
            len(self.goal_state)
        ]

        self.mode = mode
        self.trajectory_level_reward = WORDLE_MODIFIED_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 1024

    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_custom_system_prompt(self) -> str:
        # No custom system prompt for modified wordle yet
        return self.default_system_prompt_str
    
    def get_system_prompt(self) -> str:
        return self.default_system_prompt_str

    def get_start_state(self) -> str:
        return WORDLE_MODIFIED_ENV_DATA["agent"].format(agent=self.start_state)
    
    def extract_response(
        self,
        response: str,
    ) -> str:
        """
        Given a response string, potentially with a chain-of-thought
        and a final answer, this function returns the final answer,
        to generate the rule based next state.

        Args:
            response (str):
                LLM generated response. 

                Example: 
                    <Think> Step-by-step thinking </Think> <Answer> TOTEM </Answer>

        Returns:
            str: 
                The extracted answer between <Answer> and </Answer> tokens

                Example:
                    In the above example, we would return "TOTEM"
        """
        match = re.search(r"<Answer>(.*?)</Answer>", response, re.DOTALL)

        if match:
            return match.group(1).strip().lower()
        
        else:
            raise ValueError(f"Given response {response} is invalid")
        
    def get_max_turns(self) -> int:
        return WORDLE_MODIFIED_ENV_DATA["max_turns"]

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

        try:
            last_word = self.extract_response(response=last_assistant_response)

        except:
            return {
                "content": WORDLE_MODIFIED_ENV_DATA["environment_default_response"],
                "goal_reached": False,
                "judge_label": False,
            }

        correct_word = self.goal_state

        feedback = ""

        if len(last_word) != len(correct_word):
            feedback = (
                f"The word you guessed, {last_word}, does not have {self.start_state} letters, "
                f"but has {len(last_word)}. "
                f"It is thus not a correct guess and does not follow the rules of "
                f"this game. Please make another guess!"
            )

            feedback += WORDLE_MODIFIED_ENV_DATA["agent_optional_message"]

        elif last_word == correct_word:
            feedback = "Goal reached"

        else:
            for index in range(len(last_word)):
                if last_word[index] == correct_word[index]:
                    feedback += (
                        f"{self.letter_positions[index]} letter, "
                        f"{last_word[index]}, is correct and "
                        f"in the correct position in the target word"
                    )

                elif last_word[index] in correct_word:
                    feedback += (
                        f"{self.letter_positions[index]} letter, "
                        f"{last_word[index]}, exists in the "
                        f"target word but in a different position"
                    )

                else:
                    feedback += (
                        f"{self.letter_positions[index]} letter, "
                        f"{last_word[index]}, is not "
                        f"in the target word"
                    )

                if index < len(last_word) - 1:
                    feedback += " \n"

            feedback += WORDLE_MODIFIED_ENV_DATA["agent_optional_message"]
        
        
        return {
            "content": feedback,
            "goal_reached": (feedback == "Goal reached"),
            "judge_label": (feedback == "Goal reached"),
        }
