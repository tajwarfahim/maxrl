import os
import torch
import numpy as np

from collections import defaultdict
from typing import Dict
from verl import DataProto


def task_scenario_to_unique_string(
    task_scenario: Dict[str, str],
) -> str:
    task_scenario_keys = [
        'agent',
        'env',
        'task_group_name',
    ]

    for task_scenario_key in task_scenario_keys:
        assert task_scenario_key in task_scenario

    unique_task_string = (
        f"agent: {task_scenario['agent']} "
        f"env: {task_scenario['env']} "
        f"task_group_name: {task_scenario['task_group_name']}"
    )
    
    return unique_task_string


class ReplayBuffer:
    def __init__(
        self,
        replay_buffer_location: str,
        num_max_off_policy_rollouts_per_task_group: int,
    ):
        assert replay_buffer_location.endswith(".pt")
        assert os.path.isfile(replay_buffer_location)

        self.replay_buffer_for_off_policy_data = torch.load(
            replay_buffer_location,
            weights_only=False,
        )

        replay_buffer_keys = [
            'tensor_data',
            'non_tensor_batch',
            'meta_info',
        ]

        for replay_buffer_key in replay_buffer_keys:
            assert replay_buffer_key in self.replay_buffer_for_off_policy_data

        # Make a task scenario to index map
        assert "paprika_task_scenario" in self.replay_buffer_for_off_policy_data['non_tensor_batch']
        self.replay_buffer_size = len(
            self.replay_buffer_for_off_policy_data['non_tensor_batch']['paprika_task_scenario']
        )

        task_scenario_to_index_map = defaultdict(list)
        all_task_scenarios = self.replay_buffer_for_off_policy_data['non_tensor_batch']['paprika_task_scenario']

        for data_index in range(self.replay_buffer_size):
            unique_task_string = task_scenario_to_unique_string(
                task_scenario=all_task_scenarios[data_index],
            )
            task_scenario_to_index_map[unique_task_string].append(
                data_index,
            )

        print("Num unique task scenarios: ", len(task_scenario_to_index_map))
        self.task_scenario_to_index_map = task_scenario_to_index_map

        for unique_task_string in self.task_scenario_to_index_map:
            assert (
                len(self.task_scenario_to_index_map[unique_task_string]) 
                >= num_max_off_policy_rollouts_per_task_group
            )

        # finally convert replay buffer to DataProto format
        self.replay_buffer_for_off_policy_data = DataProto.from_dict(
            tensors=self.replay_buffer_for_off_policy_data['tensor_data'].to_dict(),
            non_tensors=self.replay_buffer_for_off_policy_data['non_tensor_batch'],
            meta_info=self.replay_buffer_for_off_policy_data['meta_info'],
        )

    def check_if_sampled_data_has_correct_structure(
        self,
        combined_data_batch: DataProto,
        num_onpolicy_rollouts_per_task_group: int,
        num_offpolicy_rollouts_per_task_group: int,
        train_batch_size: int,
    ) -> None:
        num_on_policy_rollouts_per_unique_task = defaultdict(int)
        num_off_policy_rollouts_per_unique_task = defaultdict(int)
        num_unique_uids = set()

        for data_index in range(len(combined_data_batch)):
            data_item = combined_data_batch[data_index]

            task_scenario = data_item.non_tensor_batch["paprika_task_scenario"]
            unique_task_string = task_scenario_to_unique_string(
                task_scenario=task_scenario,
            )
            data_policy_label = data_item.non_tensor_batch["data_policy_labels"]

            if data_policy_label == "on_policy":
                num_on_policy_rollouts_per_unique_task[unique_task_string] += 1

            elif data_policy_label == "off_policy":
                num_off_policy_rollouts_per_unique_task[unique_task_string] += 1

            else:
                raise ValueError(f"{data_policy_label} is an invalid data policy label")
            
            unique_id = data_item.non_tensor_batch["uid"]
            num_unique_uids.add(unique_id)

        assert (
            num_offpolicy_rollouts_per_task_group == 0
            or len(num_unique_uids) == len(num_off_policy_rollouts_per_unique_task)
        )

        assert (
            num_onpolicy_rollouts_per_task_group == 0
            or len(num_unique_uids) == len(num_on_policy_rollouts_per_unique_task)
        )

        assert len(num_unique_uids) == train_batch_size

        tasks_with_on_policy_rollouts = set(num_on_policy_rollouts_per_unique_task.keys())
        tasks_with_off_policy_rollouts = set(num_off_policy_rollouts_per_unique_task.keys())

        if (
            num_onpolicy_rollouts_per_task_group > 0
            and num_offpolicy_rollouts_per_task_group > 0
        ):
            assert tasks_with_on_policy_rollouts == tasks_with_off_policy_rollouts

        for task_string in num_off_policy_rollouts_per_unique_task:
            assert (
                num_off_policy_rollouts_per_unique_task[task_string] 
                ==  num_offpolicy_rollouts_per_task_group 
            )

        for task_string in num_on_policy_rollouts_per_unique_task:
            assert (
                num_on_policy_rollouts_per_unique_task[task_string]
                == num_onpolicy_rollouts_per_task_group 
            )

    def construct_training_batch_combining_on_and_off_policy_data(
        self,
        on_policy_batch: DataProto,
        num_onpolicy_rollouts_per_task_group: int,
        num_offpolicy_rollouts_per_task_group: int,
        train_batch_size: int,
        include_old_log_probs: bool,
    ) -> DataProto:
        # TODO: implement padding if on and offpolicy data dont have same shape

        # STEP 1: First, gather unique task ids + strings in the on-policy batch
        unique_task_string_to_uid_map = {}

        for data_index in range(len(on_policy_batch)):
            data_item = on_policy_batch[data_index]
            uid = data_item.non_tensor_batch["uid"]
            task_scenario = data_item.non_tensor_batch["paprika_task_scenario"]

            unique_task_string = task_scenario_to_unique_string(
                task_scenario=task_scenario,
            )

            if unique_task_string in unique_task_string_to_uid_map:
                assert unique_task_string_to_uid_map[unique_task_string] == uid

            else:
                unique_task_string_to_uid_map[unique_task_string] = uid

        # STEP 2: Next, gather the list of task indices that we need to sample from replay buffer
        indices_to_sample_from_replay_buffer = []
        list_of_uids = []

        for unique_task_string in unique_task_string_to_uid_map:
            assert unique_task_string in self.task_scenario_to_index_map
            replay_buffer_indices_for_this_task = self.task_scenario_to_index_map[unique_task_string]

            assert (
                len(replay_buffer_indices_for_this_task) 
                >= num_offpolicy_rollouts_per_task_group
            )

            randomly_sampled_indices = np.random.choice(
                a=replay_buffer_indices_for_this_task,
                size=num_offpolicy_rollouts_per_task_group,
                replace=False,
            ).tolist()

            indices_to_sample_from_replay_buffer += randomly_sampled_indices
            list_of_uids += (
                [unique_task_string_to_uid_map[unique_task_string]] 
                * num_offpolicy_rollouts_per_task_group
            )

        list_of_uids = np.array(list_of_uids, dtype=object)

        # STEP 3: Now sample these indices from the replay buffer
        off_policy_batch = self.replay_buffer_for_off_policy_data.select_idxs(
            idxs=indices_to_sample_from_replay_buffer,
        )
        off_policy_batch.non_tensor_batch["uid"] = list_of_uids

        # STEP 4: Merge on-policy and off-policy batch

        # STEP 4a: merge tensor items
        merged_tensor_dict = {}
        for tensor_item_key in off_policy_batch.batch.keys():
            if (
                include_old_log_probs 
                or tensor_item_key != "old_log_probs"
            ):
                assert tensor_item_key in on_policy_batch.batch.keys()

                merged_tensor_dict[tensor_item_key] = torch.cat(
                    (
                        on_policy_batch.batch[tensor_item_key],
                        off_policy_batch.batch[tensor_item_key],
                    ),
                    dim=0,
                )


        # STEP 4b: merge non-tensor items
        merged_non_tensor_dict = {}
        for non_tensor_item_key in off_policy_batch.non_tensor_batch.keys():
            assert non_tensor_item_key in on_policy_batch.non_tensor_batch.keys()

            merged_non_tensor_dict[non_tensor_item_key] = np.concatenate(
                (
                    on_policy_batch.non_tensor_batch[non_tensor_item_key],
                    off_policy_batch.non_tensor_batch[non_tensor_item_key],
                ),
                axis=0,
            )

        # STEP 4c: use the meta info from on-policy batch (irrelevant step for now)
        meta_info = on_policy_batch.meta_info

        # STEP 4d: keep tabs on what is on-policy and what is off-policy
        data_policy_labels = (
            ["on_policy"] * len(on_policy_batch)
            + ["off_policy"] * len(off_policy_batch)
        )

        data_policy_labels = np.array(
            data_policy_labels,
            dtype=object,
        )

        merged_non_tensor_dict["data_policy_labels"] = data_policy_labels

        # STEP 5: Merge to make one batch
        combined_data_batch = DataProto.from_dict(
            tensors=merged_tensor_dict,
            non_tensors=merged_non_tensor_dict,
            meta_info=meta_info,
        )

        # STEP 6: Run checks to make sure the basic structure of the data is correct
        # Checks: 
        # 1. Number of unique tasks is the same as training batch size
        # 2. Number of on-policy examples per task is the same as the onpolicy number defined in the config
        # 3. Number of off-policy examples per task is also the same as that defined in the config

        self.check_if_sampled_data_has_correct_structure(
            combined_data_batch=combined_data_batch,
            num_onpolicy_rollouts_per_task_group=num_onpolicy_rollouts_per_task_group,
            num_offpolicy_rollouts_per_task_group=num_offpolicy_rollouts_per_task_group,
            train_batch_size=train_batch_size,
        )

        return combined_data_batch
    
    def construct_purely_off_policy_data(
        self,
        on_policy_batch: DataProto,
        num_offpolicy_rollouts_per_task_group: int,
        train_batch_size: int,
        include_old_log_probs: bool,
    ) -> DataProto:
        # STEP 1: First, gather unique task ids + strings in the on-policy batch
        unique_task_string_to_uid_map = {}

        for data_index in range(len(on_policy_batch)):
            data_item = on_policy_batch[data_index]
            uid = data_item.non_tensor_batch["uid"]
            task_scenario = data_item.non_tensor_batch["paprika_task_scenario"]

            unique_task_string = task_scenario_to_unique_string(
                task_scenario=task_scenario,
            )

            if unique_task_string in unique_task_string_to_uid_map:
                assert unique_task_string_to_uid_map[unique_task_string] == uid

            else:
                unique_task_string_to_uid_map[unique_task_string] = uid

        # STEP 2: Next, gather the list of task indices that we need to sample from replay buffer
        indices_to_sample_from_replay_buffer = []
        list_of_uids = []

        for unique_task_string in unique_task_string_to_uid_map:
            assert unique_task_string in self.task_scenario_to_index_map
            replay_buffer_indices_for_this_task = self.task_scenario_to_index_map[unique_task_string]

            assert (
                len(replay_buffer_indices_for_this_task) 
                >= num_offpolicy_rollouts_per_task_group
            )

            randomly_sampled_indices = np.random.choice(
                a=replay_buffer_indices_for_this_task,
                size=num_offpolicy_rollouts_per_task_group,
                replace=False,
            ).tolist()

            indices_to_sample_from_replay_buffer += randomly_sampled_indices
            list_of_uids += (
                [unique_task_string_to_uid_map[unique_task_string]] 
                * num_offpolicy_rollouts_per_task_group
            )

        list_of_uids = np.array(list_of_uids, dtype=object)

        # STEP 3: Now sample these indices from the replay buffer
        off_policy_batch = self.replay_buffer_for_off_policy_data.select_idxs(
            idxs=indices_to_sample_from_replay_buffer,
        )
        off_policy_batch.non_tensor_batch["uid"] = list_of_uids

        data_policy_labels = ["off_policy"] * len(off_policy_batch)

        data_policy_labels = np.array(
            data_policy_labels,
            dtype=object,
        )

        off_policy_batch.non_tensor_batch["data_policy_labels"] = data_policy_labels

        self.check_if_sampled_data_has_correct_structure(
            combined_data_batch=off_policy_batch,
            num_onpolicy_rollouts_per_task_group=0,
            num_offpolicy_rollouts_per_task_group=num_offpolicy_rollouts_per_task_group,
            train_batch_size=train_batch_size,
        )

        if not include_old_log_probs:
            off_policy_batch.batch.pop("old_log_probs")

        return off_policy_batch
