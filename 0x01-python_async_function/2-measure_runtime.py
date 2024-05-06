#!/usr/bin/env python3

"""
Module Name: measure_runtime
Description: This module contains functions for
measuring the runtime of asynchronous coroutines.
"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n,
    max_delay) and return total_time / n.

    Parameters:
    - n (int): The number of times to call wait_random.
    - max_delay (int): The maximum delay in seconds for
    each call to wait_random.

    Returns:
    - float: The average time taken for each call to wait_random.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
