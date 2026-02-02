import re
from typing import List, Dict, Union, Optional, Any
from copy import deepcopy

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.jotto_config import JOTTO_ENV_DATA

JOTTO_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
JOTTO_DEFAULT_REWARD_FOR_SOLVED_TASK = 10.0
JOTTO_FORMAT_REWARD_PENALTY = -1.0


class JottoEnv(BaseEnv):
    """
    This class contains the logic for generating feedback for the 
    Jotto game (https://en.wikipedia.org/wiki/Jotto),
    given a guess of the secret word by the LLM or player.
    """

    custom_system_prompt_str = (
        "You are a helpful assistant."
    )

    default_system_prompt_str = "You are a helpful assistant."

    def __init__(
        self,
        task_state: Dict[str, Any],
        mode: str = "train",
    ):
        assert "env" in task_state
        assert isinstance(task_state["env"], str)
        self.goal_state = deepcopy(
            task_state["env"]
        ).strip().upper()
        assert self.goal_state.isalpha()

        # Check target word has all unique letters
        # by the rules of Jotto
        assert self.get_unique_letter_count(word=self.goal_state) == len(self.goal_state)

        self.mode = mode
        assert self.mode in ["train", "test"]

        self.trajectory_level_reward = JOTTO_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_start_state(self) -> str:
        return JOTTO_ENV_DATA["agent"].format(
            num_letters=len(self.goal_state),
        )
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 256
    
    def get_unique_letter_count(
        self, 
        word: str,
    ) -> int:
        return len(set([letter for letter in word]))
    
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
            return match.group(1).strip().upper()
        
        else:
            raise ValueError(f"Given response {response} is invalid")
        
    def get_max_turns(self) -> int:
        return JOTTO_ENV_DATA["max_turns"]
    
    def get_custom_system_prompt(
       self     
    ) -> str:
        return self.custom_system_prompt_str
    
    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_system_prompt(self) -> str:
        return self.default_system_prompt_str

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
            self.trajectory_level_reward += JOTTO_FORMAT_REWARD_PENALTY

            return {
                "content": JOTTO_ENV_DATA["environment_default_response"].format(
                    num_letters=len(self.goal_state),
                ),
                "goal_reached": False,
                "judge_label": False,
            }

        correct_word = self.goal_state

        feedback = ""

        if len(last_word) != len(correct_word):
            feedback = (
                f"The word you guessed, {last_word}, does not have the same "
                f"number of letters as the target word you need to guess. "
                f"The target word has {len(correct_word)} letters, "
                f"whereas your guess has {len(last_word)}. "
                f"It is thus not a correct guess and does not follow the rules of Jotto. "
            )

            feedback += JOTTO_ENV_DATA["agent_optional_message"].format(
                num_letters=len(self.goal_state),
            )

        elif last_word == correct_word:
            feedback = "Goal reached"
            self.trajectory_level_reward += JOTTO_DEFAULT_REWARD_FOR_SOLVED_TASK

        elif self.get_unique_letter_count(word=last_word) != len(last_word):
            feedback = (
                f"The word you guessed, {last_word}, does not have all "
                f"unique letters (i.e., it has at least one letter that appears more than once in the word). "
                f"The rules of Jotto does not permit this "
                f"as a valid guess. "
            )

            feedback += JOTTO_ENV_DATA["agent_optional_message"].format(
                num_letters=len(self.goal_state),
            )

        else:
            last_word_letters = set([l_letter for l_letter in last_word])
            correct_word_letters = set([c_letter for c_letter in correct_word])
            common_letters = last_word_letters.intersection(correct_word_letters)
            num_common_letters = len(common_letters)

            feedback = (
                f"The word you guessed, {last_word}, has {num_common_letters} letters "
                f"common with the target word that you need to guess. "
            )
                
            feedback += JOTTO_ENV_DATA["agent_optional_message"].format(
                num_letters=len(self.goal_state),
            )
        
        
        return {
            "content": feedback,
            "goal_reached": (feedback == "Goal reached"),
            "judge_label": (feedback == "Goal reached"),
        }
