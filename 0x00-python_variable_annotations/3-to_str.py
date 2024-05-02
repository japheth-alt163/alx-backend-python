#!/usr/bin/env python3


def to_str(n: float) -> str:
    """
    Converts a float to its string representation.

    Args:
        n (float): The input float number.

    Returns:
        str: The string representation of the input number.
    """
    return str(n)


if __name__ == "__main__":
    to_str = __import__('3-to_str').to_str

    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
