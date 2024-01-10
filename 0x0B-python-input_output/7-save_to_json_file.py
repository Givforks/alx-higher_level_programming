#!/usr/bin/python3
# 7-save_to_json_file.py
# Givens Emmah Abraham <givens.abraham@live.com>
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
