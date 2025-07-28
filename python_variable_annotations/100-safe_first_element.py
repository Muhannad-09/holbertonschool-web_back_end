#!/usr/bin/env python3
"""Module that defines a duck-typed function to safely
return the first element of a sequence.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence if it exists, else None.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Optional[Any]: The first element or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
