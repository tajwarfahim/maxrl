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
Preprocess the GSM8k dataset to parquet format
"""

import argparse
import os
os.environ['CURL_CA_BUNDLE'] = ''

import re

import datasets

# from verl.utils.hdfs_io import copy, makedirs
from huggingface_hub import login


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_source", default="guanning-ai/gsm8k-platinum", help="HuggingFace dataset name")
    parser.add_argument("--local_dir", default="~/data/gsm8k")
    parser.add_argument("--hdfs_dir", default="~/data/gsm8k")
    parser.add_argument("--additional_key", default=None)
    parser.add_argument("--no_train", action="store_true", help="Skip training set processing")
    parser.add_argument("--no_test", action="store_true", help="Skip test set processing")

    args = parser.parse_args()

    data_source = args.data_source
    
    if not args.local_dir:
        args.local_dir = os.path.join(os.environ["CACHE"], "verl-data", data_source.split("/")[-1])

    dataset = datasets.load_dataset(data_source)

    train_dataset = None
    if not args.no_train:
        train_dataset = dataset["train"]
    
    test_dataset = None
    if not args.no_test:
        test_dataset = dataset["test"]

    instruction_following = "Let's think step by step and output the final answer within \\boxed{}."

    # add a row to each data item that represents a unique id
    def make_map_fn(split):
        def process_fn(example, idx):
            question_raw = example.pop("problem")

            question = question_raw + " " + instruction_following

            answer_raw = example.pop("answer")
            solution = answer_raw
            data = {
                "data_source": data_source,
                "prompt": [
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                "ability": "math",
                "reward_model": {"style": "rule", "ground_truth": solution},
                "extra_info": {
                    "split": split,
                    "index": idx,
                    "answer": answer_raw,
                    "question": question_raw,
                },
            }
            if args.additional_key is not None:
                data["extra_info"][args.additional_key] = example[args.additional_key]
            return data

        return process_fn

    local_dir = args.local_dir
    hdfs_dir = args.hdfs_dir

    if not args.no_train:
        train_dataset = train_dataset.map(function=make_map_fn("train"), with_indices=True)
        train_dataset.to_parquet(os.path.join(local_dir, "train.parquet"))

    if not args.no_test:
        test_dataset = test_dataset.map(function=make_map_fn("test"), with_indices=True)
        test_dataset.to_parquet(os.path.join(local_dir, "test.parquet"))

    # if hdfs_dir is not None:
    #     makedirs(hdfs_dir)

    #     copy(src=local_dir, dst=hdfs_dir)