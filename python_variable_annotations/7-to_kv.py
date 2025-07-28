#!/usr/bin/env python3
"""Module that contains a function to return a
tuple from a string and number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number (as float).

    Args:
        k (str): The string key.
        v (Union[int, float]): An int or float value.

    Returns:
        Tuple[str, float]: A tuple with the string
        and the square of the number.
    """
    return (k, float(v ** 2))
