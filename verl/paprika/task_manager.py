from copy import deepcopy
from typing import Dict, List, Optional

from verl.paprika.environments import BaseEnv


"""
TODO: need to implement mechanism for environment failure, 
which can happen for tasks like 
20 questions, where another LLM acts as the environment.
"""

class TaskManager:
    """
    A class that handles a sequence of tasks and their trajectories,
    each with dynamic number of turns.
    """
    def __init__(
        self,
        list_of_environments: List[BaseEnv],
    ):
        self.list_of_environments: List[BaseEnv] = list_of_environments
        self.num_tasks = len(list_of_environments)
        self.all_valid_task_ids = [i for i in range(self.num_tasks)]

        # Get start states
        self.recorded_trajectories = []

        all_start_states =  [
            self.list_of_environments[index].get_start_state()
            for index in range(self.num_tasks)
        ]

        all_system_prompts = [
            self.list_of_environments[index].get_system_prompt()
            for index in range(self.num_tasks)
        ]

        # start trajectory recording
        for index in range(self.num_tasks):
            start_state = all_start_states[index]
            trajectory = [
                {
                    "role": "system",
                    "content": all_system_prompts[index],
                },
                {
                    "role": "user",
                    "content": start_state,
                },
            ]
            self.recorded_trajectories.append(trajectory)

        self.num_turns = [
            0 for _ in range(self.num_tasks)
        ]
        self.trajectory_level_rewards = [
            self.list_of_environments[env_index].get_trajectory_level_reward()
            for env_index in range(len(self.list_of_environments))
        ]

        self.env_max_turns = [
            self.list_of_environments[index].get_max_turns()
            for index in range(self.num_tasks)
        ]

        # record tasks that ended in success
        self.task_success_labels = [0 for _ in range(self.num_tasks)]

        # record agent generation tokens directly,
        # since tokens ---> text ---> tokens can result in distortions
        # shape: (num_tasks, num turns, generated tokens)
        # not square shaped/padded
        self.agent_generated_tokens: List[List[List[int]]] = [[] for _ in range(self.num_tasks)]

    def get_all_valid_task_ids(self) -> List[int]:
        return self.all_valid_task_ids

    def get_num_valid_tasks(self) -> int:
        return self.num_tasks
    
    def get_trajectory_states_for_next_round_of_generations(
        self
    ) -> List[List[Dict[str, str]]]:
        all_trajectories = []

        # Return trajectories that have not finished yet
        for task_id in self.all_valid_task_ids:
            trajectory_for_task = self.recorded_trajectories[task_id]
            all_trajectories.append(trajectory_for_task)

        return all_trajectories
    
    def get_all_agent_generated_tokens_for_next_round_of_generations(
        self
    ) -> List[List[List[int]]]:
        agent_generated_tokens_so_far = []

        # Return agent generated tokens for trajectories that have not finished yet
        for task_id in self.all_valid_task_ids:
            agent_generated_tokens_for_task = deepcopy(self.agent_generated_tokens[task_id])
            agent_generated_tokens_so_far.append(agent_generated_tokens_for_task)

        return agent_generated_tokens_so_far
    
    def get_all_env_max_tokens_per_turn_for_next_round_of_generations(
        self
    ) -> List[Optional[int]]:
        all_env_max_tokens_per_turn = []

        for task_id in self.all_valid_task_ids:
            env = self.list_of_environments[task_id]
            max_tokens_per_turn = env.get_max_num_tokens_per_turn()
            all_env_max_tokens_per_turn.append(max_tokens_per_turn)

        return all_env_max_tokens_per_turn
    
    def get_all_trajectories_with_default_system_prompt(self) -> List[List[Dict[str, str]]]:
        all_trajectories_for_training = []

        for index in range(len(self.recorded_trajectories)):
            trajectory_copy = deepcopy(self.recorded_trajectories[index])

            if trajectory_copy[0]["role"] == "system":
                new_system_prompt = self.list_of_environments[
                    index
                ].get_default_system_prompt()
                trajectory_copy[0]["content"] = new_system_prompt

            all_trajectories_for_training.append(trajectory_copy)
            
        return all_trajectories_for_training
    
    def get_all_trajectories_with_system_prompts_as_is(
        self,
    ) -> List[List[Dict[str, str]]]:
        return self.recorded_trajectories
    
    def get_all_trajectories_with_custom_system_prompt(
        self
    ) -> List[List[Dict[str, str]]]:
        all_trajectories_with_custom_system_prompt = []

        for index in range(len(self.recorded_trajectories)):
            trajectory_copy = deepcopy(self.recorded_trajectories[index])

            if trajectory_copy[0]["role"] == "system":
                new_system_prompt = self.list_of_environments[
                    index
                ].get_custom_system_prompt()
                trajectory_copy[0]["content"] = new_system_prompt

            all_trajectories_with_custom_system_prompt.append(trajectory_copy)
            
        return all_trajectories_with_custom_system_prompt
    
    def get_all_trajectory_level_rewards(self) -> List[float]:
        return self.trajectory_level_rewards
    
    def get_all_task_success_labels(self) -> List[int]:
        return self.task_success_labels
    
    def get_all_task_num_turns(self) -> List[int]:
        return self.num_turns
    
    def get_all_agent_generated_tokens(self) -> List[List[List[int]]]:
        return deepcopy(self.agent_generated_tokens)

    def update_task_trajectories_with_agent_actions(
        self,
        agent_responses: List[str],
        agent_response_tokens: List[List[int]],
    ) -> None:
        leftover_valid_task_ids = []

        # Run through environments to obtain enviro
        env_observations = []
        for index in range(self.num_tasks):
            agent_response = agent_responses[index]
            task_response_tokens = agent_response_tokens[index]
            task_id = self.all_valid_task_ids[index]

            environment = self.list_of_environments[task_id]
            trajectory = self.recorded_trajectories[task_id]
            all_agent_response_tokens = self.agent_generated_tokens[task_id]

            trajectory.append(
                {
                    "role": "assistant",
                    "content": agent_response,
                }
            )

            env_observations.append(
                environment.step(conversation_history=trajectory)
            )

            all_agent_response_tokens.append(task_response_tokens)

        # Update trajectories
        for index in range(self.num_tasks):
            task_id = self.all_valid_task_ids[index]
            trajectory = self.recorded_trajectories[task_id]

            trajectory.append(
                {
                    "role": "user",
                    "content": env_observations[index]["content"],
                }
            )

            self.num_turns[task_id] += 1

            # task finished, should be removed from queue
            if (
                self.num_turns[task_id] >= self.env_max_turns[task_id]
                or env_observations[index]["goal_reached"]
            ):
                # agent succeeded
                if (
                    env_observations[index]["goal_reached"]
                    and env_observations[index]["judge_label"]
                ):
                    self.task_success_labels[task_id] = 1.0

                self.trajectory_level_rewards[task_id] = self.list_of_environments[
                    task_id
                ].get_trajectory_level_reward()

            # task not finished, so keep in queue
            else:
                leftover_valid_task_ids.append(task_id)

        self.all_valid_task_ids = leftover_valid_task_ids
        self.num_tasks = len(leftover_valid_task_ids)
                