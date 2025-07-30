#!/usr/bin/env python3
"""Async generator that yields random numbers between 0 and 10."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield a random float between 0 and 10.

    This coroutine loops 10 times, each time asynchronously
    waiting for 1 second before yielding a random number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
