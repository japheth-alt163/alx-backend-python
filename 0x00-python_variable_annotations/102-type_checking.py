#!/usr/bin/env python3
"""
Contains a function that returns a list of
integers multiplied by a certain factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Returns a list of integers multiplied by a certain factor.
    Args:
        lst: A tuple of integers.
        factor: An integer (default is 2).
    Returns:
        A list of integers multiplied by the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
