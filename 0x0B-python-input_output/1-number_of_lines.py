#!/usr/bin/python3
# 1-number_of_lines.py
# Givens Emmah Abraham <givens.abraham@live.com>
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
