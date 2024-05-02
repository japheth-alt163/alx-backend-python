#!/usr/bin/env python3

import math


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
        n (float): The input float number.

    Returns:
        int: The floor of the input number.
    """
    return math.floor(n)


if __name__ == "__main__":
    floor = __import__('2-floor').floor

    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
