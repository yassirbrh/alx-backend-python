#!/usr/bin/env python3
'''
    Function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.
'''
import asyncio
import random
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    '''
        measure_time: function
        @n: Number of times the wait_random will spawn.
        @max_delay: Integer value default 10.
        return: total_time / n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
