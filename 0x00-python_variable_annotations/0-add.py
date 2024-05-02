#!/usr/bin/env python3


def add(a: float, b: float) -> float:
    """
    Adds two float numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


if __name__ == "__main__":
    add = __import__('0-add').add

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
