#!/usr/bin/env python3
'''
    Asynchronous routine called task_wait_n that takes in 2 int arguments
    (in this order): n and max_delay
    task_wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
'''
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
        task_wait_n: function
        @n: Number of times the wait_random will spawn.
        @max_delay: Integer value default 10.
        return: the list of wait times.
    '''
    list_of_wait_values = []
    for i in range(n):
        task = task_wait_random(max_delay)
        await task
        list_of_wait_values.append(task.result())
    return sorted(list_of_wait_values)
