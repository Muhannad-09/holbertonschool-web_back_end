#!/usr/bin/env python3
"""Module for zoom_array function with type annotations."""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Create a new list where each element in the input tuple
    is repeated `factor` times.

    Args:
        lst (Tuple): A tuple of items.
        factor (int): Number of times to repeat each item. Defaults to 2.

    Returns:
        List: A new list with repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), 3)
