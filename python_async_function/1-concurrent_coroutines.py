#!/usr/bin/env python3
"""Module for concurrently executing multiple async
tasks and collecting their results.
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently with max_delay.

    Args:
        n (int): Number of times to run wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order (using as_completed).
    """
    delays: List[float] = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for coroutine in asyncio.as_completed(tasks):
        result = await coroutine
        delays.append(result)
    return delays
