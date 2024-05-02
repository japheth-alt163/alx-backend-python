#!/usr/bin/env python3

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the input string and the square of the input int/float.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the input string and the square of v.
    """
    return (k, v ** 2)


if __name__ == "__main__":
    to_kv = __import__('7-to_kv').to_kv

    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
