#!/usr/bin/env python3

"""
Module Name: concurrent_coroutines
Description: This module contains asynchronous
coroutines for concurrent operations.
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay.

    Parameters:
    - n (int): The number of times to call wait_random.
    - max_delay (int): The maximum delay in seconds
    for each call to wait_random.

    Returns:
    - List[float]: List of all the delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

if __name__ == "__main__":
    import asyncio
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
