import json
import numpy as np
from typing import Dict, Any, Tuple

from verl import DataProto


def calculate_paprika_metrics(
    data: DataProto,
    num_trajectories_per_task: int,
    metric_type: str,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    # First, make clusters based on task group and
    # individual tasks
    clusters = {}
    # Additional structure to track metrics per data_policy_labels
    # Example: clusters_by_policy["on_policy"][task_group][task_uid][metric_name] -> list of values
    clusters_by_policy = {}

    metric_names_to_processing_functions = {
        "rewards": lambda x: x,
        "task_success_labels": lambda x: x,
        "task_num_turns": lambda x: x,
        "records": lambda x: json.loads(x),
    }

    for index in range(len(data)):
        data_item = data[index]

        task_group = data_item.non_tensor_batch["paprika_task_scenario"]["task_group_name"]
        individual_task_scenario = data_item.non_tensor_batch["uid"]

        if task_group not in clusters:
            clusters[task_group] = {}

        if individual_task_scenario not in clusters[task_group]:
            clusters[task_group][individual_task_scenario] = {
                metric_name: [] for metric_name in metric_names_to_processing_functions
            }

        # Add to main (overall) clusters
        for metric_name in metric_names_to_processing_functions:
            data_item_metric_value = metric_names_to_processing_functions[metric_name](
                data_item.non_tensor_batch[metric_name]
            )
            clusters[task_group][individual_task_scenario][metric_name].append(
                data_item_metric_value
            )

        # If there is a data_policy_labels field, also add to policy-specific clusters
        if "data_policy_labels" in data_item.non_tensor_batch:
            policy_label = data_item.non_tensor_batch["data_policy_labels"]

            if policy_label not in clusters_by_policy:
                clusters_by_policy[policy_label] = {}

            if task_group not in clusters_by_policy[policy_label]:
                clusters_by_policy[policy_label][task_group] = {}

            if individual_task_scenario not in clusters_by_policy[policy_label][task_group]:
                clusters_by_policy[policy_label][task_group][individual_task_scenario] = {
                    metric_name: [] for metric_name in metric_names_to_processing_functions
                }

            for metric_name in metric_names_to_processing_functions:
                data_item_metric_value = metric_names_to_processing_functions[metric_name](
                    data_item.non_tensor_batch[metric_name]
                )
                clusters_by_policy[policy_label][task_group][individual_task_scenario][
                    metric_name
                ].append(data_item_metric_value)

    # check if clusters formed are okay (overall, regardless of policy label)
    for task_group in clusters:
        for individual_task_scenario in clusters[task_group]:
            for metric_name in metric_names_to_processing_functions:
                assert isinstance(
                    clusters[task_group][individual_task_scenario][metric_name],
                    list,
                )

                assert (
                    len(clusters[task_group][individual_task_scenario][metric_name])
                    == num_trajectories_per_task
                ), (
                    f"Obtained num trajectories: "
                    f"{len(clusters[task_group][individual_task_scenario][metric_name])} "
                    f"Required num trajectories: {num_trajectories_per_task} "
                    f"For task: {individual_task_scenario}, task group: {task_group}"
                )

    metrics_dict: Dict[str, Any] = {}

    # ---- Original metrics (unchanged) ----
    for task_group in clusters:
        num_total_success = 0.0
        total_reward = 0.0
        num_total_turns = 0.0
        num_total_tasks = 0
        best_at_k_success = 0.0
        min_reward = float("inf")
        max_reward = float("-inf")
        min_total_turns = float("inf")
        max_total_turns = float("-inf")

        for individual_task_scenario in clusters[task_group]:
            rewards = np.array(
                clusters[task_group][individual_task_scenario]["rewards"]
            )
            success_labels = np.array(
                clusters[task_group][individual_task_scenario]["task_success_labels"]
            )
            num_turns = np.array(
                clusters[task_group][individual_task_scenario]["task_num_turns"]
            )

            num_total_success += np.sum(success_labels)
            total_reward += np.sum(rewards)
            min_reward = min(min_reward, np.min(rewards))
            max_reward = max(max_reward, np.max(rewards))

            num_total_turns += np.sum(num_turns)
            min_total_turns = min(min_total_turns, np.min(num_turns))
            max_total_turns = max(max_total_turns, np.max(num_turns))

            best_at_k_success += np.max(success_labels)
            num_total_tasks += 1

        # calculate task group metrics
        metrics_dict[
            f"{metric_type}/{task_group}/"
            f"avg@{num_trajectories_per_task}_success_rate"
        ] = num_total_success / (num_total_tasks * num_trajectories_per_task)

        metrics_dict[
            f"{metric_type}/{task_group}/average_reward"
        ] = total_reward / (num_total_tasks * num_trajectories_per_task)

        metrics_dict[
            f"{metric_type}/{task_group}/average_num_turns"
        ] = num_total_turns / (num_total_tasks * num_trajectories_per_task)

        metrics_dict[
            f"{metric_type}/{task_group}/"
            f"pass@{num_trajectories_per_task}_success_rate"
        ] = best_at_k_success / num_total_tasks

        metrics_dict[
            f"{metric_type}/{task_group}/num_tasks_sampled"
        ] = num_total_tasks

        metrics_dict[f"{metric_type}/{task_group}/min_reward"] = min_reward
        metrics_dict[f"{metric_type}/{task_group}/max_reward"] = max_reward
        metrics_dict[f"{metric_type}/{task_group}/min_num_turns"] = min_total_turns
        metrics_dict[f"{metric_type}/{task_group}/max_num_turns"] = max_total_turns

    # ---- Additional metrics split by data_policy_labels (on_policy / off_policy) ----
    # Only computed if data_policy_labels were present
    for policy_label, policy_clusters in clusters_by_policy.items():
        for task_group, scenarios in policy_clusters.items():
            num_total_success = 0.0
            total_reward = 0.0
            num_total_turns = 0.0
            num_total_tasks = 0
            num_total_samples = 0  # total number of trajectories in this group+policy
            best_at_k_success = 0.0
            min_reward = float("inf")
            max_reward = float("-inf")
            min_total_turns = float("inf")
            max_total_turns = float("-inf")

            for individual_task_scenario, metrics in scenarios.items():
                rewards = np.array(metrics["rewards"])
                success_labels = np.array(metrics["task_success_labels"])
                num_turns = np.array(metrics["task_num_turns"])

                if rewards.size == 0:
                    continue  # no samples for this scenario+policy

                n = rewards.size
                num_total_samples += n

                num_total_success += np.sum(success_labels)
                total_reward += np.sum(rewards)
                min_reward = min(min_reward, np.min(rewards))
                max_reward = max(max_reward, np.max(rewards))

                num_total_turns += np.sum(num_turns)
                min_total_turns = min(min_total_turns, np.min(num_turns))
                max_total_turns = max(max_total_turns, np.max(num_turns))

                best_at_k_success += np.max(success_labels)
                num_total_tasks += 1

            if num_total_tasks == 0 or num_total_samples == 0:
                continue

            prefix = f"{policy_label}_data_metrics/{metric_type}/{task_group}"

            # Use actual number of samples as denominator here; task-group-level
            metrics_dict[f"{prefix}/avg_success_rate"] = (
                num_total_success / num_total_samples
            )

            metrics_dict[f"{prefix}/average_reward"] = (
                total_reward / num_total_samples
            )

            metrics_dict[f"{prefix}/average_num_turns"] = (
                num_total_turns / num_total_samples
            )

            # best success over trajectories per task, averaged over tasks
            metrics_dict[f"{prefix}/pass_success_rate"] = (
                best_at_k_success / num_total_tasks
            )

            metrics_dict[f"{prefix}/num_tasks_sampled"] = num_total_tasks
            metrics_dict[f"{prefix}/min_reward"] = min_reward
            metrics_dict[f"{prefix}/max_reward"] = max_reward
            metrics_dict[f"{prefix}/min_num_turns"] = min_total_turns
            metrics_dict[f"{prefix}/max_num_turns"] = max_total_turns

    # Record trajectories (unchanged)
    all_trajectories = []
    for task_group in clusters:
        for individual_task_scenario in clusters[task_group]:
            all_trajectories.append(
                clusters[task_group][individual_task_scenario]["records"]
            )

    return metrics_dict, all_trajectories
