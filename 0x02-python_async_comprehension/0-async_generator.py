#!/usr/bin/env python3
"""
Async generator module
"""

import asyncio
import random


async def async_generator():
    """
    Coroutine that generates random numbers asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    import asyncio

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)
    asyncio.run(print_yielded_values())
