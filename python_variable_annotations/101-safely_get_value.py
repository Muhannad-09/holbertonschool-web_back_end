#!/usr/bin/env python3
"""Module that defines a function with advanced type annotations."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Safely get a value from a dictionary with a default.

    Args:
        dct (Mapping): The dictionary to access.
        key (Any): The key to look up.
        default (Union[T, None], optional): The default value if key not found.

    Returns:
        Union[Any, T]: The found value or the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
