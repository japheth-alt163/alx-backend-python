#!/usr/bin/env python3

"""
Module Name: tasks
Description: This module contains functions
for creating asyncio tasks.
"""

import asyncio
from typing import List, Awaitable


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously create tasks that wait for random delays.

    Parameters:
    - n (int): The number of tasks to create.
    - max_delay (int): The maximum delay in seconds for each task.

    Returns:
    - List[float]: List of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
