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
Preprocess the madrylab/gsm8k-platinum dataset and push to hub
- Rename "question" to "problem"
- Keep "answer" but only the part after the last "### "
- Add "datasource": "gsm8k-platinum"
- Push to guanning-ai/gsm8k-platinum
"""

import os
os.environ['CURL_CA_BUNDLE'] = ''

import datasets
from huggingface_hub import login


def process_example(example):
    """Process a single example from the dataset."""
    # Get the answer and extract only the part after the last "### "
    answer_raw = example["answer"]
    if "### " in answer_raw:
        # Split by "### " and take the last part
        answer_processed = answer_raw.rsplit("### ", 1)[-1]
    else:
        # If no "### " found, keep the original
        answer_processed = answer_raw
    
    return {
        "problem": example["question"],
        "answer": answer_processed,
        "datasource": "gsm8k-platinum"
    }


if __name__ == "__main__":
    # Load the source dataset
    source_dataset = "madrylab/gsm8k-platinum"
    target_dataset = "guanning-ai/gsm8k-platinum"
    
    print(f"Loading dataset from {source_dataset}...")
    dataset = datasets.load_dataset(source_dataset)
    
    print(f"Dataset structure: {dataset}")
    
    # Process all splits
    processed_dataset = {}
    for split_name in dataset.keys():
        print(f"Processing split: {split_name}")
        split_data = dataset[split_name]
        
        # Remove all columns except what we need, then add new ones
        processed_split = split_data.map(
            process_example,
            remove_columns=split_data.column_names  # Remove all original columns
        )
        processed_dataset[split_name] = processed_split
        
        # Print sample
        print(f"Sample from {split_name}:")
        print(processed_split[0])
        print()
    
    # Create a DatasetDict
    final_dataset = datasets.DatasetDict(processed_dataset)
    
    # Push to hub
    print(f"Pushing to {target_dataset}...")
    final_dataset.push_to_hub(target_dataset)
    print("Done!")

