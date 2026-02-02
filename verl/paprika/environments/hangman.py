import re
from typing import List, Dict, Union, Optional, Any
from copy import deepcopy

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.hangman_config import HANGMAN_ENV_DATA


HANGMAN_MAX_WRONG_GUESSES_MADE = 6
HANGMAN_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
HANGMAN_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0


class HangmanEnv(BaseEnv):
    """
    This class contains the logic for generating feedback for the 
    Hangman game (https://en.wikipedia.org/wiki/Hangman_(game)),
    given a guess of the secret word by the LLM or the player.
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
        self.goal_state = deepcopy(task_state["env"]).strip().upper()
        assert self.goal_state.isalpha()

        self.num_wrong_guesses_so_far = 0
        self.current_word_representation = ["_" for _ in range(len(self.goal_state))]
        self.previous_guesses_made = []

        self.mode = mode
        assert self.mode in ["train", "test"]

        self.trajectory_level_reward = HANGMAN_DEFAULT_REWARD_FOR_UNSOLVED_TASK

    def get_start_state(self) -> str:
        return HANGMAN_ENV_DATA["agent"].format(
            agent=self.get_current_word_representation(),
        )
    
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
            return match.group(1).strip().upper()
        
        else:
            raise ValueError(f"Given response {response} is invalid")
        
    def get_max_turns(self) -> int:
        return HANGMAN_ENV_DATA["max_turns"]
    
    def get_custom_system_prompt(
       self     
    ) -> str:
        return self.custom_system_prompt_str
    
    def get_default_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_system_prompt(self) -> str:
        return self.default_system_prompt_str
    
    def get_current_word_representation(self) -> str:
        return " ".join(self.current_word_representation)

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
            last_hangman_guess = self.extract_response(response=last_assistant_response)

        except:
            self.num_wrong_guesses_so_far += 1

            if self.num_wrong_guesses_so_far >= HANGMAN_MAX_WRONG_GUESSES_MADE:
                feedback = (
                    f"Your current guess did not follow "
                    f"the proper formatting rules for the game of Hangman. "
                    f"This counts as a wrong guess. "
                    f"The target word to guess was {self.goal_state}. "
                    f"You have run out of the budget for "
                    f"maximum number of incorrect guesses allowed. "
                    f"Therefore, you have lost the game! Game over."
                )

            else:
                feedback = HANGMAN_ENV_DATA["environment_default_response"].format(
                    curr_word_representation=self.get_current_word_representation()
                )

            return {
                "content": feedback,
                "goal_reached": (self.num_wrong_guesses_so_far >= HANGMAN_MAX_WRONG_GUESSES_MADE),
                "judge_label": False,
            }
        
        # Agent did not guess a word or a letter
        if not last_hangman_guess.isalpha():
            feedback = (
                f"Your guess needs to be either a single letter, or "
                f"the entire hidden word. However, your guess, {last_hangman_guess}, "
                f"is neither, so it counts as wrong guess. "
            )
            feedback += HANGMAN_ENV_DATA["agent_optional_message"].format(
                curr_word_representation=self.get_current_word_representation()
            )
            self.num_wrong_guesses_so_far += 1

        elif last_hangman_guess in self.previous_guesses_made:
            feedback = (
                f"You have already made this guess, {last_hangman_guess}, before. "
                f"So this counts as one incorrect guess. "
            )
            feedback += HANGMAN_ENV_DATA["agent_optional_message"].format(
                curr_word_representation=self.get_current_word_representation()
            )
            self.num_wrong_guesses_so_far += 1
        
        # Agent guessed the entire word
        elif len(last_hangman_guess) > 1:
            if last_hangman_guess.upper() == self.goal_state.upper():
                feedback = (
                    f"You correctly guessed the target word, "
                    f"which was {self.goal_state}. "
                    f"Congratulations! "
                    f"Goal reached."
                )
                self.trajectory_level_reward = HANGMAN_DEFAULT_REWARD_FOR_SOLVED_TASK

            else:
                feedback = (
                    f"You guessed the entire hidden word at once. "
                    f"However, your guess, {last_hangman_guess}, is not correct. "
                )
                feedback += HANGMAN_ENV_DATA["agent_optional_message"].format(
                    curr_word_representation=self.get_current_word_representation()
                )
                self.num_wrong_guesses_so_far += 1

        # Agent guessed a single letter
        elif len(last_hangman_guess) == 1:
            letter_found = False
            num_letters_left_to_guess = 0

            for letter_index in range(len(self.goal_state)):
                if self.goal_state[letter_index] == last_hangman_guess:
                    self.current_word_representation[letter_index] = last_hangman_guess
                    letter_found = True

                if self.current_word_representation[letter_index] == "_":
                    num_letters_left_to_guess += 1

            if not letter_found:
                self.num_wrong_guesses_so_far += 1

            if num_letters_left_to_guess == 0:
                feedback = (
                    f"You have revealed all the letters in the target word, "
                    f"which was {self.goal_state}. "
                    f"Congratulations! "
                    f"Goal reached."
                )

                self.trajectory_level_reward = HANGMAN_DEFAULT_REWARD_FOR_SOLVED_TASK

            else:
                feedback = (
                    f"You have guessed the letter {last_hangman_guess} in your last turn. "
                )
                if not letter_found:
                    feedback += (
                        "This letter is not in the target word, so this counts as wrong guess. "
                    )
                else:
                    feedback += (
                        "This letter is in the target word, congratulations! "
                    )

                feedback += HANGMAN_ENV_DATA["agent_optional_message"].format(
                    curr_word_representation=self.get_current_word_representation()
                )
            
        # Agent guessed nothing
        else:
            self.num_wrong_guesses_so_far += 1
            feedback = (
                f"Your guess needs to be either a single letter, or "
                f"the entire hidden word. However, your guess "
                f"is neither, so it counts as wrong guess. "
            )
            feedback += HANGMAN_ENV_DATA["agent_optional_message"].format(
                curr_word_representation=self.get_current_word_representation()
            )


        feedback = feedback.strip()

        if len(last_hangman_guess) > 0 and last_hangman_guess.isalpha():
            self.previous_guesses_made.append(last_hangman_guess)

        if "Goal reached" in feedback:
            assert self.num_wrong_guesses_so_far < HANGMAN_MAX_WRONG_GUESSES_MADE

        if self.num_wrong_guesses_so_far >= HANGMAN_MAX_WRONG_GUESSES_MADE:
            feedback = (
                f"The target word to guess was {self.goal_state}. "
                f"You have run out of the budget for "
                f"maximum number of incorrect guesses allowed "
                f"for the game of Hangman. "
                f"Therefore, you have lost the game! Game over."
            )
        
        return {
            "content": feedback,
            "goal_reached": (
                "Goal reached" in feedback
                or self.num_wrong_guesses_so_far >= HANGMAN_MAX_WRONG_GUESSES_MADE
            ),
            "judge_label": ("Goal reached" in feedback),
        }