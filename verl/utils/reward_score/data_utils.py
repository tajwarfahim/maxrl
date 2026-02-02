import os
import re
import json
import tiktoken
import subprocess
from collections import Counter
from typing import List, Union
from transformers import DataCollatorForSeq2Seq
from transformers.utils import logging
from functools import lru_cache

logger = logging.get_logger(__name__)

def read_json(file: str) -> dict:
    """
    Read a JSON file.

    Args:
        file (str): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file.
    """
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)
    
def write_json(file: str, data: dict):
    """
    Write data to a JSON file.

    Args:
        file (str): The path to the JSON file.
        data (dict): The data to write.
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

def read_jsonl(file):
    """
    Read a JSONL file.

    Args:
        file (str): The path to the JSONL file.

    Returns:
        List[dict]: A list of dictionaries, each representing a sample.
    """
    if not os.path.exists(file):
        return []

    with open(file, "r", encoding="utf-8") as f:
        # Read all lines at once instead of line by line
        lines = f.readlines()

        # Use list comprehension with json.loads
        return [json.loads(line) for line in lines]

def append_jsonl(file: str, data: Union[dict, List[dict]]):
    """
    Append data to a JSONL file.

    Args:
        file (str): The path to the JSONL file.
        data (Union[dict, List[dict]]): The data to append.
    """
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            pass

    if isinstance(data, dict):
        data = [data]

    with open(file, "a", encoding="utf-8") as f:
        for d in data:
            f.write(json.dumps(d) + "\n")

def write_jsonl(file: str, data: Union[dict, List[dict]]):
    """
    Write data to a JSONL file.

    Args:
        file (str): The path to the JSONL file.
        data (Union[dict, List[dict]]): The data to write.
    """
    if isinstance(data, dict):
        data = [data]

    with open(file, "w", encoding="utf-8") as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

def check_conversation_format(sample, tokenizer):
    """
    Check if the conversation format is valid.

    Args:
        sample (dict): The conversation sample.
        tokenizer: The tokenizer object.

    Returns:
        bool: True if the conversation format is valid, False otherwise.
    """
    try:
        tokenizer.apply_chat_template(
            conversation=sample["openai_format"],
            tokenize=False
        )
    except Exception:
        return False

    if len([turn for turn in sample["openai_format"] if turn["role"] == "assistant" ]) == 0:
        # No assistant turns
        logger.warning("No assistant turns in the conversation.")
        return False

    return True

def find_substrings_between_include(s, substr1, substr2, greedy=False):
    """
    Find the positions of substrings between two given substrings in a string.

    Args:
        s (str): The input string.
        substr1 (str): The first substring.
        substr2 (str): The second substring.
        greedy (bool, optional): Whether to use greedy matching. Defaults to False.

    Returns:
        list: A list of tuples representing the start and end positions of the substrings.

    Note: 
        re.DOTALL matches all characters, including newlines.
    """
    if greedy:
        pattern = re.escape(substr1) + r'(.*)' + re.escape(substr2)
    else:
        pattern = re.escape(substr1) + r'(.*?)' + re.escape(substr2)
    positions = []

    for match in re.finditer(pattern, s, re.DOTALL):
        start = match.start()
        end = match.end()
        content = match.group(0)
        positions.append((start, end))

    return positions

def find_substrings_between_exclude(s, substr1, substr2, greedy=False):
    """
    Find the positions of substrings between two given substrings in a string.

    Args:
        s (str): The input string.
        substr1 (str): The first substring.
        substr2 (str): The second substring.
        greedy (bool, optional): Whether to use greedy matching. Defaults to False.

    Returns:
        list: A list of tuples representing the start and end positions of the substrings.

    Note: 
        re.DOTALL matches all characters, including newlines.
    """
    if greedy:
        pattern = re.escape(substr1) + r'(.*)' + re.escape(substr2)
    else:
        pattern = re.escape(substr1) + r'(.*?)' + re.escape(substr2)
    positions = []

    for match in re.finditer(pattern, s, re.DOTALL):
        start = match.start() + len(substr1) # Exclude substr1
        end = match.end() - len(substr2) # Exclude substr2
        content = match.group(0)
        positions.append((start, end))

    return positions

def has_intersection(interval1, interval2):
    """
    Check if two intervals have an intersection.

    Args:
        interval1 (tuple): The first interval, represented as a tuple (start, end).
        interval2 (tuple): The second interval, represented as a tuple (start, end).

    Returns:
        bool: True if the intervals have an intersection, False otherwise.
    """
    return not (interval1[1] <= interval2[0] or interval1[0] >= interval2[1])

def num_lines(file):
    """
    Count the number of lines in a file.
    
    Args:
        file (str): The path to the file.
        
    Returns:
        int: The number of lines in the file.
    """
    assert os.path.exists(file), f"File {file} does not exist. Cannot count lines."
    result = subprocess.run(['wc', '-l', file], stdout=subprocess.PIPE)
    return int(result.stdout.split()[0])

def read_lines(file):
    """
    Read all lines from a file.
    
    Args:
        file (str): The path to the file.
        
    Returns:
        List[str]: A list of lines in the file.
    """
    if not os.path.exists(file):
        return []

    with open(file, "r") as f:
        return f.readlines()

def most_common_element(data):
    """
    Finds the most common element in a list.

    Parameters:
        data (list): The list of elements.

    Returns:
        The most common element in the list. If there are multiple elements with
        the same highest frequency, it returns the first one encountered.
    """
    assert data and len(data) > 0, "Data is empty"

    counter = Counter(data)
    return counter.most_common(1)[0][0]

@lru_cache(maxsize=None)
def get_encoding(model: str):
    """Get the encoding for a model. If the model is not found in tiktoken, use gpt-4o as fallback."""
    try:
        return tiktoken.encoding_for_model(model)
    except KeyError:
        logger.warning_once(f"Model {model} not found in tiktoken. Using gpt-4o as fallback.") #! Do NOT use transformers.AutoTokenizer which is very slow
        return tiktoken.encoding_for_model("gpt-4o")

def num_tokens_consumed_from_request(
    request_json: dict,
    api_endpoint: str,
    model: str,
):
    """Count the number of tokens in the request. Only supports completion and embedding requests."""
    encoding = get_encoding(model)
    # if completions request, tokens = prompt + n * max_tokens
    if api_endpoint.endswith("completions"):
        max_tokens = request_json.get("max_tokens", 15)
        n = request_json.get("n", 1)
        completion_tokens = n * max_tokens

        # chat completions
        if api_endpoint.startswith("chat/"):
            num_tokens = 0
            for message in request_json["messages"]:
                num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":  # if there's a name, the role is omitted
                        num_tokens -= 1  # role is always required and always 1 token
            num_tokens += 2  # every reply is primed with <im_start>assistant
            return num_tokens + completion_tokens
        # normal completions
        else:
            prompt = request_json["prompt"]
            if isinstance(prompt, str):  # single prompt
                prompt_tokens = len(encoding.encode(prompt))
                num_tokens = prompt_tokens + completion_tokens
                return num_tokens
            elif isinstance(prompt, list):  # multiple prompts
                prompt_tokens = sum([len(encoding.encode(p)) for p in prompt])
                num_tokens = prompt_tokens + completion_tokens * len(prompt)
                return num_tokens
            else:
                raise TypeError(
                    'Expecting either string or list of strings for "prompt" field in completion request'
                )
    # if embeddings request, tokens = input tokens
    elif api_endpoint == "embeddings":
        input = request_json["input"]
        if isinstance(input, str):  # single input
            num_tokens = len(encoding.encode(input))
            return num_tokens
        elif isinstance(input, list):  # multiple inputs
            num_tokens = sum([len(encoding.encode(i)) for i in input])
            return num_tokens
        else:
            raise TypeError(
                'Expecting either string or list of strings for "inputs" field in embedding request'
            )
    # more logic needed to support other API calls (e.g., edits, inserts, DALL-E)
    else:
        raise NotImplementedError(
            f'API endpoint "{api_endpoint}" not implemented in this script'
        )

class DataCollatorForSeq2SeqWithoutAttentionMask(DataCollatorForSeq2Seq):
    def __call__(self, features, return_tensors=None):
        batch = super().__call__(features, return_tensors=return_tensors)
        batch.pop("attention_mask", None)
        return batch