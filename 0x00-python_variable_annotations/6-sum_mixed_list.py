#!/usr/bin/env python3

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the input list.
    """
    return sum(mxd_lst)


if __name__ == "__main__":
    sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print(sum_mixed_list.__annotations__)
    print(f"sum_mixed_list(mixed) returns {ans} which is a {type(ans)}")
