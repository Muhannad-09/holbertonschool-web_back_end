#!/usr/bin/env python3
"""Measure runtime for running async_comprehension four times in parallel."""

import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times concurrently and measure total runtime.

    Returns:
        Total time taken in seconds as a float.
    """
    start = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = perf_counter()
    return end - start
