#!/usr/bin/env python3
'''
    Asynchronous routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
'''
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
        wait_n: function
        @n: Number of times the wait_random will spawn.
        @max_delay: Integer value default 10.
        return: the list of wait times.
    '''
    list_of_wait_values = []
    for i in range(n):
        wait_value = random.uniform(0, max_delay)
        await asyncio.sleep(wait_value)
        list_of_wait_values.append(wait_value)
    return list_of_wait_values
