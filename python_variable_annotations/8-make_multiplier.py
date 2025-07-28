#!/usr/bin/env python3
"""Module that contains a function returning a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies
        its input by multiplier.
    """
    def multiply(value: float) -> float:
        """Multiply the input value by the outer multiplier."""
        return value * multiplier

    return multiply
