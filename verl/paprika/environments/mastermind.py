import re
from typing import List, Dict, Union, Optional, Any
from copy import deepcopy

from verl.paprika.environments.base_env import BaseEnv

from verl.paprika.environments.env_configs.mastermind_config import MASTERMIND_ENV_DATA

MASTERMIND_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
MASTERMIND_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0

MASTERMIND_SECRET_CODE_LENGTH = 4


class MastermindEnv(BaseEnv):
    """
    This class contains the logic for generating feedback for the 
    Mastermind game (https://en.wikipedia.org/wiki/Mastermind_(board_game)),
    given a guess of the secret 4-digit code by the LLM or player.
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
        self.goal_state = deepcopy(task_state["env"]).strip()
        assert len(self.goal_state) ==  MASTERMIND_SECRET_CODE_LENGTH
        assert self.goal_state.isdigit()

        self.mode = mode
        assert self.mode in ["train", "test"]

        self.trajectory_level_reward = MASTERMIND_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_start_state(self) -> str:
        return MASTERMIND_ENV_DATA["agent"]
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 1024
    
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
                    <Think> Step-by-step thinking </Think> <Answer> 9 0 9 4 </Answer>

        Returns:
            str: 
                The extracted answer between <Answer> and </Answer> tokens

                Example:
                    In the above example, we would return "9 0 9 4"
        """
        match = re.search(r"<Answer>(.*?)</Answer>", response, re.DOTALL)

        if match:
            return match.group(1).strip().lower()
        
        else:
            raise ValueError(f"Given response {response} is invalid")
        
    def get_max_turns(self) -> int:
        return MASTERMIND_ENV_DATA["max_turns"]
    
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
            last_code_guess_raw = self.extract_response(response=last_assistant_response)

        except:
            return {
                "content": MASTERMIND_ENV_DATA["environment_default_response"],
                "goal_reached": False,
                "judge_label": False,
            }
        
        last_code_guess = "".join(last_code_guess_raw.split())

        secret_code = self.goal_state
        assert (
            isinstance(secret_code, str)
            and len(secret_code) == MASTERMIND_SECRET_CODE_LENGTH 
            and secret_code.isdigit()
        )

        # Generate environment feedback for each case
        feedback = ""

        if not last_code_guess.isdigit():
            feedback = (
                f"The code you guessed does not consist of 4 digits only, "
                f"please guess a new code!"
            )

            feedback += MASTERMIND_ENV_DATA["agent_optional_message"]

        elif len(last_code_guess) != MASTERMIND_SECRET_CODE_LENGTH:
            feedback = (
                f"The code you guessed does not have 4 digits, "
                f"but instead has {len(last_code_guess)} digits. "
                f"According to the rule of the game, you must generate a "
                f"4 digit guess."
            )

            feedback += MASTERMIND_ENV_DATA["agent_optional_message"]

        elif last_code_guess == secret_code:
            feedback = "Goal reached"
            self.trajectory_level_reward = MASTERMIND_DEFAULT_REWARD_FOR_SOLVED_TASK

        else:
            # count exact matches
            num_exact_matches = 0

            for index in range(len(last_code_guess)):
                if last_code_guess[index] == secret_code[index]:
                    num_exact_matches += 1

            # Count partial matches
            # Create frequency counts of unmatched digits in secret_code and guess
            secret_unmatched = {}
            guess_unmatched = {}

            for s, g in zip(secret_code, last_code_guess):
                if s != g:  # Only consider non-matching positions
                    secret_unmatched[s] = secret_unmatched.get(s, 0) + 1
                    guess_unmatched[g] = guess_unmatched.get(g, 0) + 1

            # Calculate partial matches by comparing counts of unmatched digits
            partial_matches = 0
            for digit in guess_unmatched:
                partial_matches += min(
                    secret_unmatched.get(digit, 0),
                    guess_unmatched[digit],
                )

            feedback = (
                f"Your last guess has "
                f"{num_exact_matches} exact matches with the secret code. "
                f"In other words, exactly {num_exact_matches} digit(s) in your last guess, "
                f"{last_code_guess_raw}, "
                f"are in the correct position in the secret code. "
                f"(We won't reveal the particular digits within your guess "
                f"that are exact matches, they can be any digit within your guess) "
                f"Your last guess also has {partial_matches} partial matches. "
                f"In other words, {partial_matches} digits in your guess, "
                f"{last_code_guess_raw}, "
                f"are in the secret code, but in the wrong position. "
                f"(We won't reveal which digits within your guess are "
                f"partial matches, they can be any, you must deduce them with reasoning "
                f"and further guesses and feedbacks.)"
            )

            feedback += MASTERMIND_ENV_DATA["agent_optional_message"]

        feedback = feedback.strip()
        
        return {
            "content": feedback,
            "goal_reached": (feedback == "Goal reached"),
            "judge_label": (feedback == "Goal reached"),
        }