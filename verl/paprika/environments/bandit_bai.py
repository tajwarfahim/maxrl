import re
import numpy as np
import json
from copy import deepcopy
from typing import List, Dict, Union, Optional, Any

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.env_configs.bandit_best_arm_identification_config import (
    BANDIT_BEST_ARM_IDENTIFICATION_ENV_DATA,
)


BANDIT_BEST_ARM_IDENTIFICATION_DEFAULT_REWARD_FOR_UNSOLVED_TASK = 0.0
BANDIT_BEST_ARM_IDENTIFICATION_DEFAULT_REWARD_FOR_SOLVED_TASK = 1.0


class BanditBestArmIdentificationEnv(BaseEnv):
    """
    This class contains the logic for generating feedback for the 
    Bandit best arm identification task.
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
        task_state = deepcopy(task_state)
        assert "env" in task_state
        assert "agent" in task_state

        task_state["env"] = json.loads(deepcopy(task_state["env"]))

        # Recover env states
        self.task_description = deepcopy(task_state["agent"])
        self.arm_names_string = deepcopy(task_state["env"]["arm_names_string"])
        self.arm_names = deepcopy(task_state["env"]["arm_names"])
        self.mean_arm_rewards = deepcopy(task_state["env"]["mean_arm_rewards"])

        # Necessary checks
        assert len(self.arm_names) == len(self.mean_arm_rewards)
        arm_names_reconstituted = ", ".join(self.arm_names)
        assert arm_names_reconstituted.lower() == self.arm_names_string.lower()

        # Set best arm based on mean arm rewards
        self.best_arm = self.arm_names[np.argmax(self.mean_arm_rewards)]

        self.mode = mode
        assert self.mode in ["train", "test"]

        self.trajectory_level_reward = (
            BANDIT_BEST_ARM_IDENTIFICATION_DEFAULT_REWARD_FOR_UNSOLVED_TASK
        )

    def get_start_state(self) -> str:
        return BANDIT_BEST_ARM_IDENTIFICATION_ENV_DATA["agent"].format(
            agent=self.task_description,
            env=self.arm_names_string,
        )
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return 512
    
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
        return BANDIT_BEST_ARM_IDENTIFICATION_ENV_DATA["max_turns"]
    
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
            action = self.extract_response(response=last_assistant_response)

        except:
            return {
                "content": BANDIT_BEST_ARM_IDENTIFICATION_ENV_DATA["environment_default_response"],
                "goal_reached": False,
                "judge_label": False,
            }
        
        # Extract total number of turns spent so far
        num_turns = 0
        for time_step in range(len(conversation_history)):
            if conversation_history[time_step]["role"] == "assistant":
                num_turns += 1

        feedback = None

        # In this turn, the agent needs to decide what the best arm is
        # So we give reward based on this
        if num_turns == self.get_max_turns():
            if action == self.best_arm:
                feedback = "Goal reached"
                self.trajectory_level_reward = (
                    BANDIT_BEST_ARM_IDENTIFICATION_DEFAULT_REWARD_FOR_SOLVED_TASK
                )

            else:
                feedback = (
                    f"You chose the wrong best arm! The correct best arm was {self.best_arm}. Game over!"
                )

        # Intermediate step, provides observations from the bandit world
        # Case 1: model chose an arm not in the given list
        elif action not in self.arm_names:
            feedback = "You have made an invalid choice, please choose again!"

            feedback += BANDIT_BEST_ARM_IDENTIFICATION_ENV_DATA[
                "agent_optional_message"
            ].format(
                env=self.arm_names_string,
            )

        # Case 2: regular case, generate observed reward from 
        # bernoulli distribution 
        else:
            action_index = self.arm_names.index(action)
            random_number = np.random.uniform(
                low=0.0,
                high=1.0,
                size=None,
            )

            reward = 0
            if random_number <= self.mean_arm_rewards[action_index]:
                reward = 1

            feedback = f"You have received reward {reward}\n"

            # Second to last step, need to instruct the model to choose the best arm
            if num_turns == self.get_max_turns() - 1:
                feedback += (
                    f"You have exhausted your budget for trying out different choices "
                    f"and observe their rewards. Now make a deduction about what the "
                    f"best choice is. In other words, deduce the choice with the highest mean reward. "
                    f"Format your answer as follows: "
                    f"<Think> Any optional thinking to go over the interaction history so far "
                    f"that will help decide what the best choice is </Think> \n"
                    f"<Answer> your decision about the best choice in this scenario </Answer>"
                )

            else:
                feedback += BANDIT_BEST_ARM_IDENTIFICATION_ENV_DATA[
                    "agent_optional_message"
                ].format(
                    env=self.arm_names_string,
                )
        
        return {
            "content": feedback,
            "goal_reached": (feedback == "Goal reached"),
            "judge_label": (feedback == "Goal reached"),
        }