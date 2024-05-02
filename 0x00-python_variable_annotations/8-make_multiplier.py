#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the provided multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by the multiplier.
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply


if __name__ == "__main__":
    make_multiplier = __import__('8-make_multiplier').make_multiplier

    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
