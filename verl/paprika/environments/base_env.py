from abc import ABC, abstractmethod
from typing import List, Dict, Union, Optional, Any


class BaseEnv(ABC):
    """
    The Base Class for Paprika environments,
    defines the member functions that all child classes
    that inherits from this class, should have.
    """
    trajectory_level_reward = None

    def __init__(
        self,
        task_state: Dict[str, Any],
        mode: str = "train",
    ):
        """
        Initializes an object of this class.

        Args:
            task_state (Dict[str, str]):
                A dictionary containing the task state, of the
                following format:
                {
                    "env": <env information, hidden from agent>,
                    "agent": <optional information that agent may receive>,
                }  

            mode (str):
                Which mode the environment is in.  
                Options: "train" and "test"
                Default: "train"
        """
        raise NotImplementedError
    
    def get_system_prompt(
        self
    ) -> str:
        """
        Returns the system prompt at the beginning
        of the trajectory.

        Args:
            None

        Returns:
            str:
                system prompt for the environment
        """
        return NotImplementedError
    
    def get_default_system_prompt(
        self
    ) -> str:
        """
        Returns the system prompt at the beginning
        of the trajectory.

        Args:
            None

        Returns:
            str:
                system prompt for the environment
        """
        return NotImplementedError
    
    def get_trajectory_level_reward(
        self
    ) -> float:
        """
        Returns the trajectory level reward of the
        this environment object.

        Args:
            None

        Returns:
            float:
                The trajectory level reward, in case
                the trajectory has reached the end.
        """
        assert self.trajectory_level_reward is not None, (
            "Trajectory rollout for this task has not finished, "
            "so no trajectory level reward is available. "
        )
        
        return self.trajectory_level_reward
    
    def get_custom_system_prompt(
       self     
    ) -> str:
        """
        Some environments would have a custom system prompt.
        This will return that.

        Args:
            None

        Returns:
            str:
                custom system prompt for the environment
        """
        return NotImplementedError
    
    def validate_conversation_history(
        self,
        conversation_history: List[Dict[str, str]],
    ) -> None:
        """
        This class validates whether the conversation
        has proper formats, namely:
        [
            {
                "role": "user",
                "content": str,
            },
            {
                "role": "assistant",
                "content": str,
            }
        ]

        Args:
            conversation_history (List[Dict[str, str]]):
                conversation history that needs to be validated

        Returns:
            None
        """
        assert (
            isinstance(conversation_history, list)
        ), "conversation_history must be list"

        valid_roles = ["user", "system"]

        for index in range(len(conversation_history)):
            conv_item = conversation_history[index]
            assert (
                isinstance(conv_item, dict)
            ), "conv_item (item within conversation_history) must be a dict"

            assert "role" in conv_item
            assert "content" in conv_item

            for key in conv_item:
                assert key in ["role", "content"]
                assert isinstance(conv_item[key], str)

            # user and assistant tokens must appear alternatively
            assert conv_item["role"] in valid_roles

            if conv_item["role"] in ["system", "assistant"]:
                valid_roles = ["user"]

            else:
                valid_roles = ["assistant"]

    @abstractmethod
    def step(
        self,
        conversation_history: List[Dict[str, str]],
    ) -> Dict[str, Union[str, bool]]:
        """
        Given the state of the trajectory so far, it returns the next
        state, namely a dictionary of the following format:

            {
                "content": str,
                "goal_reached": bool,
                "judge_label": bool,
            }

        Args:
            conversation_history (List[Dict[str, str]]):
                conversation history that needs to be validated
                It has to have the following format:
                    [
                        {
                            "role": "user",
                            "content": str,
                        },
                        {
                            "role": "assistant",
                            "content": str,
                        }
                    ]

        Returns:
            Dict[str, Union[str, bool]]: 
                contains the environment feedback, which should have the 
                following format:
                    {
                        "content": str,
                        "goal_reached": bool,
                        "judge_label": bool,
                    }

                where 
                1. "content" maps to the environment feedback that
                    the agent will receive in the next stage (if any)

                2. "goal_reached" refers to whether the agent has 
                    received their goal at this step

                3. "judge_label" refers to if the secondary judge
                    also thinks that the agent has reached the goal at this step.
                    judge label has the power to override goal_reached, to
                    reduce false positives.
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_start_state(self) -> str:
        """
        Returns the system prompt that the LLM agent will receive,
        with instructions for solving this task.

        Args:
            None

        Returns:
            str: 
                The system prompt with the task instructions for
                this problem.
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_max_turns(self) -> int:
        """
        Returns the maximum number of allowable turns.

        Args:
            None

        Returns:
            int:
                Number of turns spent so far.
        """
        raise NotImplementedError
    
    def get_max_num_tokens_per_turn(self) -> Optional[int]:
        return None
