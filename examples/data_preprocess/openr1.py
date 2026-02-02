# Copyright 2024 Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Preprocess the MATH-lighteval dataset to parquet format
"""

import argparse
import os

import datasets

from verl.utils.hdfs_io import copy, makedirs
from verl.utils.reward_score.math import last_boxed_only_string, remove_boxed


def extract_solution(solution_str):
    return remove_boxed(last_boxed_only_string(solution_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--local_dir", default="~/data/math")
    parser.add_argument("--hdfs_dir", default=None)
    parser.add_argument("--start_index", type=int, default=0)
    parser.add_argument("--end_index", type=int, default=30)

    args = parser.parse_args()

    # 'lighteval/MATH' is no longer available on huggingface.
    # Use mirror repo: DigitalLearningGmbH/MATH-lighteval
    # data_source = "self-label-zanette-lab/math_proper_train_test"
    # data_source = "ftajwar/srt_test_dataset"
    # data_source = "Maxwell-Jia/AIME_2024"
    # data_source = "POLARIS-Project/Polaris-Dataset-53K"
    data_source = "open-r1/OpenR1-Math-220k"
    # data_source = "zwhe99/amc23"
    # data_source = "math-ai/aime25"
    # data_source = "math-ai/minervamath"
    # data_source = "math-ai/olympiadbench"
    # data_source = "ByteDance-Seed/BeyondAIME"
    # data_source = "ftajwar/deduplicated_dapo_dataset"

    # data_source = "self-label-zanette-lab/big_math_filtered_pass_rate_between_0.3_and_0.7"

    print(f"Loading the {data_source} dataset from huggingface...", flush=True)
    # dataset = datasets.load_dataset(data_source, trust_remote_code=True)
    dataset = datasets.load_dataset(data_source, "default", trust_remote_code=True)

    train_dataset = dataset["train"]
    test_dataset = dataset["train"] # srt test dataset, aime 2024

    # train_dataset = train_dataset.select(
    #     # range(args.start_index, args.end_index)
    #     range(0, 257)
    # )
    # test_dataset = test_dataset.select(
    #     # range(args.start_index, args.end_index)
    #     range(300, 400)
    # )

    # test_dataset = dataset["test"] # math-12k
    # test_dataset = dataset["train"] # big-math-rl-verified

    # instruction_following = " " + "Let's think step by step and output the final answer within \\boxed{}."
    instruction_following = "\nPlease reason step by step, and put your final answer within \\boxed{{}}."

    # add a row to each data item that represents a unique id
    def make_map_fn(split):
        def process_fn(example, idx):
            # question = example.pop("question")   # amc23, minerva, olympiadbench
            question = example.pop("problem") # polaris, open-r1, aime25, beyondaime
            # question = example.pop("Problem") # math-12k + srt test dataset + aime24
            # question = example.pop("prompt") # big-math-rl-verified, dapo

            # question = question + " " + instruction_following
            question = question + instruction_following

            # answer = example.pop("final_answer")[0]  # olympiadbench
            answer = example.pop("answer")  # polaris, open-r1, amc23, aime25, minerva, beyondaime, dapo
            # answer = example.pop("Answer") # math-12k + srt test dataset + aime24
            # answer = example.pop('answer') # big-math-rl-verified
            # solution = extract_solution(answer)
            
            answer = str(answer)

            # data_source = "DigitalLearningGmbH/MATH-lighteval"   # math-12k
            # data_source = example.pop("data_source") # srt test dataset
            data_source = "polaris"

            if idx == 0:
                print("Question: ", question)
                print("Answer: ", type(answer), " ", answer)

            data = {
                "data_source": data_source,
                "id": idx, 
                "prompt": [
                    {
                        "role": "user", 
                        "content": question,
                    },
                ],
                "ability": "math",
                "reward_model": {"style": "rule", "ground_truth": answer},
                "extra_info": {"split": split, "index": idx},
            }
            return data

        return process_fn

    train_dataset = train_dataset.map(function=make_map_fn("train"), with_indices=True)
    test_dataset = test_dataset.map(function=make_map_fn("test"), with_indices=True)

    local_dir = args.local_dir
    hdfs_dir = args.hdfs_dir

    train_dataset.to_parquet(os.path.join(local_dir, "train.parquet"))
    test_dataset.to_parquet(os.path.join(local_dir, "test.parquet"))

    if hdfs_dir is not None:
        makedirs(hdfs_dir)

        copy(src=local_dir, dst=hdfs_dir)