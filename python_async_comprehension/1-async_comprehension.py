#!/usr/bin/env python3
"""Async comprehension that collects 10 random
numbers from async_generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async comprehension over async_generator.

    Returns:
        List of 10 floats yielded from async_generator.
    """
    return [i async for i in async_generator()]
