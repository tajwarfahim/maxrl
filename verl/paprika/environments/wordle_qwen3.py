import re
from typing import List, Dict, Union, Optional, Any
from copy import deepcopy

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.wordle_qwen3_config import (
    WORDLE_QWEN3_WORD_LENGTH,
    WORDLE_QWEN3_ENV_DATA,
)

WORDLE_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
WORDLE_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0


class WordleQwen3Env(BaseEnv):
    """
    This class contains the logic for generating feedback for the 
    Wordle game (https://en.wikipedia.org/wiki/Wordle),
    given a guess of the secret word by the LLM or player.

    NOTE:
        This version is for Qwen3 models only.
    """

    custom_system_prompt_str = (
        "You are a helpful assistant. "
        "You have to play wordle. Try to follow the following strategy: "
        "1. Start with a common five-letter word using distinct and frequent "
        "letters (e.g., 'SLATE', 'CRANE', 'AUDIO') to maximize information gain.\n"
        "2. After each guess, interpret the feedback:"
        "\n   - If a letter is correct and in the right position, lock it in that position." 
        "\n   - If a letter exists but is in the wrong position, include it but exclude its current position."
        "\n   - If a letter does not exist in the target word, exclude it from future guesses unless it has already been confirmed elsewhere.\n" 
        "3. Maintain three sets: confirmed letters with positions, present letters with excluded positions, and eliminated letters.\n"
        "4. Filter the list of possible words to include only those that match all constraints.\n"
        "5. For the next guess, pick a word that:"
        "\n   - Fits all known constraints"
        "\n   - Introduces new letters (early on) to gather more information"
        "\n   - Narrows down the solution space (later on) to focus on likely answers\n" 
        "6. Continue refining guesses based on new feedback until the word is found or attempts run out. "
        "7. Finally, make sure to wrap your answers like this: \\boxed{SLATE}"
    )

    default_system_prompt_str = "You are a helpful assistant."

    # default_system_prompt_str = (
    #     "You are a helpful assistant. "
    #     "You have to play wordle. Try to follow the following strategy: "
    #     "1. Start with a common five-letter word using distinct and frequent "
    #     "letters (e.g., 'SLATE', 'CRANE', 'AUDIO') to maximize information gain.\n"
    #     "2. After each guess, interpret the feedback:"
    #     "\n   - If a letter is correct and in the right position, lock it in that position." 
    #     "\n   - If a letter exists but is in the wrong position, include it but exclude its current position."
    #     "\n   - If a letter does not exist in the target word, exclude it from future guesses unless it has already been confirmed elsewhere.\n" 
    #     "3. Maintain three sets: confirmed letters with positions, present letters with excluded positions, and eliminated letters.\n"
    #     "4. Filter the list of possible words to include only those that match all constraints.\n"
    #     "5. For the next guess, pick a word that:"
    #     "\n   - Fits all known constraints"
    #     "\n   - Introduces new letters (early on) to gather more information"
    #     "\n   - Narrows down the solution space (later on) to focus on likely answers\n" 
    #     "6. Continue refining guesses based on new feedback until the word is found or attempts run out. "
    #     "7. Finally, make sure to wrap your answers like this: <Answer> SLATE </Answer>"
    # )

    # custom_system_prompt_str = (
    #     "You are a helpful assistant. "
    #     "If you will play wordle, please do not guess the word "
    #     "House at the first turn."
    # )

    letter_positions = {
        0: "First",
        1: "Second",
        2: "Third",
        3: "Fourth",
        4: "Fifth",
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
        assert len(self.goal_state) ==  WORDLE_QWEN3_WORD_LENGTH
        assert self.goal_state.isalpha()

        self.mode = mode
        assert self.mode in ["train", "test"]

        self.trajectory_level_reward = WORDLE_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_start_state(self) -> str:
        return WORDLE_QWEN3_ENV_DATA["agent"]
    
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
                    .... Step-by-step thinking .... \\boxed{TOTEM}

        Returns:
            str: 
                The extracted answer from the \\boxed{} answer

                Example:
                    In the above example, we would return "TOTEM"
        """
        positions = [m.start() for m in re.finditer(r'\\boxed\{', response)]
        if not positions:
            raise ValueError("No \\boxed{...} found")

        # Start at the last match
        i = positions[-1] + len(r'\boxed{')
        depth = 1
        start = i

        while i < len(response) and depth > 0:
            if response[i] == '{':
                depth += 1
            elif response[i] == '}':
                depth -= 1
            i += 1

        if depth != 0:
            raise ValueError("Unbalanced braces in last \\boxed")

        return response[start:i-1]
        
    def get_max_turns(self) -> int:
        return WORDLE_QWEN3_ENV_DATA["max_turns"]
    
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
            return {
                "content": WORDLE_QWEN3_ENV_DATA["environment_default_response"],
                "goal_reached": False,
                "judge_label": False,
            }

        correct_word = self.goal_state

        feedback = ""

        if len(last_word) != WORDLE_QWEN3_WORD_LENGTH:
            feedback = (
                f"The word you guessed, {last_word}, does not have five letters, "
                f"but has {len(last_word)}. "
                f"It is thus not a correct guess and does not follow the rules of "
                f"the game wordle. Please make another guess!"
            )

            feedback += WORDLE_QWEN3_ENV_DATA["agent_optional_message"]

        elif last_word == correct_word:
            feedback = "Goal reached"
            self.trajectory_level_reward = WORDLE_DEFAULT_REWARD_FOR_SOLVED_TASK

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

            feedback += WORDLE_QWEN3_ENV_DATA["agent_optional_message"]
        
        
        return {
            "content": feedback,
            "goal_reached": (feedback == "Goal reached"),
            "judge_label": (feedback == "Goal reached"),
        }
