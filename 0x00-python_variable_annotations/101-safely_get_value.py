#!/usr/bin/env python3

"""Contains method that safely gets value from dictionary."""

from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely gets value from dictionary.
    Args: dct (Mapping): Dictionary to get value from.
        key (Any): Key to get value from.
        default (Optional[T], optional): Default
        value to return if key is not found.
        Defaults to None.
    Returns:
        Union[Any, T]: Value from dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
