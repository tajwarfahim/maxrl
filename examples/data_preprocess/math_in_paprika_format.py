import os
import datasets

from verl.utils.hdfs_io import copy, makedirs
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--local_dir', default=None)
    parser.add_argument('--hdfs_dir', default=None)
    parser.add_argument(
        "--data_source", 
        # default="self-label-zanette-lab/big_math_filtered",
        # default="self-label-zanette-lab/math_proper_train_test", 
        # default="self-label-zanette-lab/big_math_filtered_pass_rate_between_0.3_and_0.7",
        default="Maxwell-Jia/AIME_2024",
        help="The dataset to be used. Default one contains all six of them",
    )

    args = parser.parse_args()

    data_source = args.data_source
    print(f"Loading the {data_source} dataset from huggingface...", flush=True)
    dataset = datasets.load_dataset(data_source, trust_remote_code=True)


    assert "train" in dataset, "The dataset must contain a 'train' split."
    # assert "test" in dataset, "The dataset must contain a 'test' split."
    train_dataset = dataset['train']
    # test_dataset = dataset['test'] # math-12k
    # test_dataset = dataset['train'] # big-math-rl-verified
    test_dataset = dataset['train'] # aime 2024

    # Qwen format
    instruction_following = "\n Let's think step by step and output the final answer within \\boxed{{}}"

    # Deepseek format
    # instruction_following = "\nPlease reason step by step, and put your final answer within \\boxed{}."

    # add a row to each data item that represents a unique id
    def make_map_fn(split):

        def process_fn(example, idx):
            # question = example.pop('Problem')  # math-12k
            # question = example.pop('prompt')  # big-math-rl-verified
            question = example.pop('Problem') # AIME 2024

            question = question + instruction_following

            # solution = example.pop('Answer')  # math-12k
            # solution = example.pop('answer')  # big-math-rl-verified
            solution = example.pop('Answer') # AIME 2024
            solution = str(solution)
            data_source = example.pop('data_source', "big_math")

            data = {
                "data_source": data_source,
                "prompt": [{
                    "role": "user",
                    "content": question
                }],
                "ability": "math",
                "reward_model": {
                    "style": "rule",
                    "ground_truth": solution
                },
                "extra_info": {
                    'split': split,
                    'index': idx,
                },
                "paprika_task_scenario": {
                    "task_group_name": "math",
                    "env": solution,
                    "agent": question,
                }
            }
            return data

        return process_fn

    train_dataset = train_dataset.map(function=make_map_fn('train'), with_indices=True)
    test_dataset = test_dataset.map(function=make_map_fn('test'), with_indices=True)

    
    # if not args.local_dir: 
    #     local_dir = "dataset/six_evaluation_individual/" + args.data_source.split('/')[-1]
    # else: 
    #     local_dir = args.local_dir + args.data_source.split('/')[-1]
    hdfs_dir = args.hdfs_dir

    train_dataset.to_parquet(os.path.join(args.local_dir, 'train.parquet'))
    test_dataset.to_parquet(os.path.join(args.local_dir, 'test.parquet'))

    if hdfs_dir is not None:
        makedirs(hdfs_dir)

        copy(src=args.local_dir, dst=hdfs_dir)