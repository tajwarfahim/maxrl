import datasets
from datasets import Dataset, DatasetDict
import tqdm

from typing import List, Dict
    

def deduplicate_dataset() -> List[Dict[str, str]]:
    dataset_path = 'SynthLabsAI/Big-Math-RL-Verified'
    dataset = datasets.load_dataset(dataset_path, trust_remote_code=True)['train']

    deduplicated_prompt_to_entry_map = {}
    for index in tqdm.tqdm(range(len(dataset))):
        question = dataset[index]['problem']
        solution = dataset[index]['answer']

        llama8b_solve_rate = dataset[index]["llama8b_solve_rate"]
        if llama8b_solve_rate is None:
            print("Yes")
            llama8b_solve_rate = 0.0

        if llama8b_solve_rate >= 0.3 and llama8b_solve_rate <= 0.7:
            deduplicated_prompt_to_entry_map[question] = {
                'prompt': question,
                'answer': solution,
            }

    print("\nNumber of unique datapoints: ", len(deduplicated_prompt_to_entry_map), "\n")

    new_dataset = []
    all_questions = list(deduplicated_prompt_to_entry_map.keys())

    for question_index in tqdm.tqdm(range(len(all_questions))):
        question = all_questions[question_index]

        entry = deduplicated_prompt_to_entry_map[question]
        entry["id"] = question_index
        entry["source"] = "big_math_rl_verified"

        new_dataset.append(entry)

    dataset = Dataset.from_list(new_dataset)
    dataset_dict = DatasetDict({"train": dataset})
    dataset_dict.push_to_hub("self-label-zanette-lab/big_math_filtered_pass_rate_between_0.3_and_0.7")


if __name__ == "__main__":
    deduplicate_dataset()