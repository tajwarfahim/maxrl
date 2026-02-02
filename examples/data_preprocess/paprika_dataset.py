import argparse
import os
from typing import List, Dict
import json

import datasets

from verl.paprika.environments.env_configs.wordle_config import (
    WORDLE_ENV_DATA,
)
from verl.paprika.environments.env_configs.wordle_modified_config import (
    WORDLE_MODIFIED_ENV_DATA,
)
from verl.paprika.environments.env_configs.twenty_questions_config import (
    TWENTY_QUESTIONS_ENV_DATA,
)
from verl.paprika.environments.env_configs.cellular_automata_config import (
    CELLULAR_AUTOMATA_ENV_DATA,
)
# from verl.paprika.environments.env_configs.mastermind_config import (
#     MASTERMIND_ENV_DATA,
# )
from verl.paprika.environments.env_configs.mastermind_extended_config import (
    MASTERMIND_ENV_DATA,
)
from verl.paprika.environments.env_configs.bandit_best_arm_identification_config import (
    BANDIT_BEST_ARM_IDENTIFICATION_ENV_DATA,
)
from verl.paprika.environments.env_configs.battleship_config import (
    BATTLESHIP_ENV_DATA,
)
from verl.paprika.environments.env_configs.minesweeper_config import (
    MINESWEEPER_ENV_DATA,
)
from verl.paprika.environments.env_configs.hangman_config import (
    HANGMAN_ENV_DATA,
)
from verl.paprika.environments.env_configs.jotto_config import (
    JOTTO_ENV_DATA,
)

# Qwen3 envs
from verl.paprika.environments.env_configs.wordle_qwen3_config import (
    WORDLE_QWEN3_ENV_DATA
)


def get_all_tasks(
    task_group_name: str,
    split: str,
) -> List[Dict[str, str]]:
    """
    Returns all the tasks within a task group.

    Args:
        task_group_name (str):
            The name of the task group

        split (str):
            Which split to load
    """
    assert split in ["train", "test"]

    if task_group_name == "wordle":
        data = WORDLE_ENV_DATA[split]

    elif task_group_name == "wordle_modified":
        data = WORDLE_MODIFIED_ENV_DATA[split]

    elif task_group_name == "twenty_questions":
        data = TWENTY_QUESTIONS_ENV_DATA[split]

    elif task_group_name == "cellular_automata":
        data = CELLULAR_AUTOMATA_ENV_DATA[split]

    elif task_group_name == "mastermind":
        data = MASTERMIND_ENV_DATA[split]

    elif task_group_name == "bandit_best_arm_identification":
        data = BANDIT_BEST_ARM_IDENTIFICATION_ENV_DATA[split]

    elif task_group_name == "battleship":
        data = BATTLESHIP_ENV_DATA[split]

    elif task_group_name == "minesweeper":
        data = MINESWEEPER_ENV_DATA[split]

    elif task_group_name == "hangman":
        data = HANGMAN_ENV_DATA[split]

    elif task_group_name == "jotto":
        data = JOTTO_ENV_DATA[split]

    # Qwen3 envs
    elif task_group_name == "wordle_qwen3":
        data = WORDLE_QWEN3_ENV_DATA[split]
    
    else:
        raise ValueError(f"Given task group {task_group_name} is not supported.")
    
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--local_dir", default="~/data/math", type=str)
    parser.add_argument("--task_group_name", default="wordle", type=str)
    parser.add_argument("--num_test_examples", default=10, type=int)
    parser.add_argument("--num_train_examples", default=2000, type=int)

    args = parser.parse_args()

    # Get train dataset
    train_dataset = get_all_tasks(
        task_group_name=args.task_group_name,
        split="train",
    )[:args.num_train_examples]
    train_dataset = datasets.Dataset.from_list(
        train_dataset
    )

    # Get test dataset
    test_dataset = get_all_tasks(
        task_group_name=args.task_group_name,
        split="test" if args.task_group_name != "wordle_modified" else "train",
    )[:args.num_test_examples]
    
    test_dataset = datasets.Dataset.from_list(
        test_dataset
    )

    instruction_following = "Let's think step by step and output the final answer within \\boxed{}."

    # add a row to each data item that represents a unique id
    def make_map_fn(split):
        def process_fn(example, idx):
            question = "Dummy question"
            answer = "Dummy answer"
            env_scenario = example.pop("env")
            agent_scenario = example.pop("agent")

            if not isinstance(env_scenario, str):
                env_scenario = json.dumps(env_scenario)

            if not isinstance(agent_scenario, str):
                agent_scenario = json.dumps(agent_scenario)

            data = {
                "data_source": "paprika",
                "prompt": [{"role": "user", "content": question}],
                "ability": "math",
                "reward_model": {"style": "rule", "ground_truth": answer},
                "extra_info": {
                    "split": split, 
                    "index": idx,
                    "unique_task_id": f"{args.task_group_name}_id_{idx}",
                },
                "paprika_task_scenario": {
                    "task_group_name": args.task_group_name,
                    "env": env_scenario,
                    "agent": agent_scenario,
                }
            }
            return data

        return process_fn

    train_dataset = train_dataset.map(function=make_map_fn("train"), with_indices=True)
    test_dataset = test_dataset.map(function=make_map_fn("test"), with_indices=True)

    local_dir = args.local_dir

    train_dataset.to_parquet(os.path.join(local_dir, "train.parquet"))
    test_dataset.to_parquet(os.path.join(local_dir, "test.parquet"))
