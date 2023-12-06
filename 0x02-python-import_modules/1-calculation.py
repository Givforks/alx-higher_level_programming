#!/usr/bin/python3
# 1-calculation.py
# Givens E Abraham  <givens.abraham@live.com>

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    f = 10
    g = 5

    print("{} + {} = {}".format(f, g, add(f, g)))
    print("{} - {} = {}".format(f, g, sub(f, g)))
    print("{} * {} = {}".format(f, g, mul(f, g)))
    print("{} / {} = {}".format(f, g, div(f, g)))
