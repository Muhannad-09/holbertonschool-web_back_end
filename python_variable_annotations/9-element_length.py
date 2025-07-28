#!/usr/bin/env python3
"""Module that contains a function with annotated iterable
input and tuple list output.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-type
        elements (e.g. list, str, tuple).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples (element, length).
    """
    return [(i, len(i)) for i in lst]
