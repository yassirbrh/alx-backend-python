#!/usr/bin/env python3
'''
    measure_runtime coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
'''
import asyncio
import random
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
        measure_runtime: function
        return: The total runtime.
    '''
    start = time.time()
    coroutines = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*coroutines)
    return time.time() - start
