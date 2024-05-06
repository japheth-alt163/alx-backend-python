#!/usr/bin/env python3

"""
Module Name: tasks
Description: This module contains functions
for creating asyncio tasks.
"""

import asyncio
from typing import Awaitable


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task that waits for a random delay.

    Parameters:
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - asyncio.Task: The asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
