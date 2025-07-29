#!/usr/bin/env python3
"""Measure average runtime of wait_n coroutine."""

import time
import asyncio
from typing import Union
from concurrent.futures import ProcessPoolExecutor

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total time taken to execute wait_n(n, max_delay),
    return average time per task.

    Args:
        n (int): number of times to run wait_random concurrently
        max_delay (int): max delay passed to wait_random

    Returns:
        float: average execution time per task
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    total_time = end - start
    return total_time / n
