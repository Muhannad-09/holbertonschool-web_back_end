#!/usr/bin/env python3
"""Type checking with zoom_array."""

from typing import Tuple, List, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Return a list where each item is repeated `factor` times."""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
