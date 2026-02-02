from typing import List, Dict, Any

# envs for regular instruct models except qwen3

from verl.paprika.environments.base_env import BaseEnv
from verl.paprika.environments.wordle import WordleEnv
from verl.paprika.environments.math_test import Math
from verl.paprika.environments.wordle_modified import WordleModifiedEnv
from verl.paprika.environments.countdown import CountdownEnv
from verl.paprika.environments.twenty_questions import TwentyQuestionsEnv
from verl.paprika.environments.cellular_automata import CellularAutomataEnv
from verl.paprika.environments.mastermind import MastermindEnv
from verl.paprika.environments.bandit_bai import BanditBestArmIdentificationEnv
from verl.paprika.environments.battleship import BattleshipEnv
from verl.paprika.environments.minesweeper import MinesweeperEnv
from verl.paprika.environments.hangman import HangmanEnv
from verl.paprika.environments.jotto import JottoEnv

# qwen3 envs
from verl.paprika.environments.wordle_qwen3 import WordleQwen3Env


def get_environment(
    task_group_name: str,
    task_state: Dict[str, Any],
    mode: str = "train",
) -> BaseEnv:
    """
    Given a single task group name and a task state,
    this function creates and returns the corresponding
    environment.

    Args:
        task_group_name (str):
            Name of the Task Group

            Example: 'wordle'

        task_state (Dict[str, Any]):
            A dictionary containing the task state, of the
            following format:
            {
                "env": <env information, hidden from agent>,
                "agent": <optional information that agent may receive>,
            } 

            Example: 
                {
                    "env": 'TOTEM',
                    "agent": 'word',
                }

        mode (str):
            Mode of the environment
            Has to be either "train" or "test"

            Default:
                "train"

    Returns:
        BaseEnv: Corresponding environment object
    """
    assert mode in ["train", "test"]
    env_kwagrs = {
        "task_state": task_state,
        "mode": mode,
    }

    if task_group_name == "wordle":
        env = WordleEnv(**env_kwagrs)

    elif task_group_name == "math":
        env = Math(**env_kwagrs)

    elif task_group_name == "wordle_modified":
        env = WordleModifiedEnv(**env_kwagrs)

    elif task_group_name == "countdown":
        env = CountdownEnv(**env_kwagrs)

    elif task_group_name == "twenty_questions":
        env = TwentyQuestionsEnv(**env_kwagrs)

    elif task_group_name == "cellular_automata":
        env = CellularAutomataEnv(**env_kwagrs)

    elif task_group_name == "mastermind":
        env = MastermindEnv(**env_kwagrs)

    elif task_group_name == "bandit_best_arm_identification":
        env = BanditBestArmIdentificationEnv(**env_kwagrs)

    elif task_group_name == "battleship":
        env = BattleshipEnv(**env_kwagrs)

    elif task_group_name == "minesweeper":
        env = MinesweeperEnv(**env_kwagrs)

    elif task_group_name == "hangman":
        env = HangmanEnv(**env_kwagrs)

    elif task_group_name == "jotto":
        env = JottoEnv(**env_kwagrs)

    # qwen3 envs
    elif task_group_name == "wordle_qwen3":
        env = WordleQwen3Env(**env_kwagrs)

    else:
        raise ValueError(
            f"Task group {task_group_name} is not supported."
        )
    
    return env


def get_batch_of_environments(
    task_group_names: List[str],
    task_states: List[Dict[str, Any]],
    env_modes: List[str],
) -> List[BaseEnv]:
    """
    Given a batch of task group names and task states,
    this function returns a batch of task environment objects corresponding
    to these names and task states.

    Args:
        task_group_names (List[str]):
            a list, whose i-th element corrsponds to the i-th
            task group in the batch.

            Example: ['wordle', 'wordle', 'battleship', 'wordle']

        task_states (List[Dict[str, Any]]):
            A list containing the task states. Each element in
            this list is a dictionary, of the following format:
                {
                    "env": <env information, hidden from agent>,
                    "agent": <optional information that agent may receive>,
                } 

            Example: 
                [
                    {
                        "env": 'TOTEM',
                        "agent": 'word',
                    },
                    ....
                ]

        env_modes (List[str]):
            A list containing the environment modes
            env_modes[i] = mode of the i-th environment
                            Has to be either "train" or "test"

    Returns:
        List[BaseEnv]: A list of environment objects
    """
    assert len(task_group_names) == len(task_states)
    assert len(task_group_names) > 0

    all_environments = []
    for index in range(len(task_group_names)):
        env = get_environment(
            task_group_name=task_group_names[index],
            task_state=task_states[index],
            mode=env_modes[index],
        )

        all_environments.append(env)

    return all_environments
