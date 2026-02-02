# Code adapted from: https://github.com/tajwarfahim/llm_exploration/blob/main/llm_exploration/utils/data_utils.py

import json
import os
from typing import Any


def read_json(fname: str) -> Any:
    """
    Given a filename, reads a json file and returns the data stored inside.

    Input:
        fname (str):
            Name of the file to be read.

    Output:
        data (Any):
            The data loaded from the json file.
    """

    assert os.path.isfile(fname)
    assert fname.endswith(".json")

    with open(fname, "r") as file:
        data = json.load(file)

    return data


def write_json(
    data: Any,
    fname: str,
) -> None:
    """
    Given a data and the filename, writes the data to the specified
    fname.
    If the directory that the specified filename should be in
    does not exist, then it creates the directory first.

    Input:
        data (Any):
            the data that needs to stored in a json format.

        fname (str):
            path to the file where the data needs to be saved.

    Output:
        None
    """

    assert isinstance(fname, str) and fname.endswith(".json")
    splits = fname.split("/")[:-1]
    root_dir = "/".join(splits)
    if not os.path.isdir(root_dir):
        os.makedirs(root_dir, exist_ok=True)

    with open(fname, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)