#!/usr/bin/env python3
"""
Module to create asyncio.Task for wait_random coroutine.
"""

import asyncio
from typing import Optional
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that runs wait_random with max_delay.

    Args:
        max_delay (int): Maximum delay for wait_random coroutine.

    Returns:
        asyncio.Task: Task object wrapping wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
