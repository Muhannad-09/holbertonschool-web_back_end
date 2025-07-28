#!/usr/bin/env python3
"""Module for zoom_array function with type annotations."""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), 3)
