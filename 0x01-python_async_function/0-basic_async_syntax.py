#!/usr/bin/env python3
'''
    Asynchronous coroutine that takes in an integer max_delay default 10
    named wait_random that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
'''
import random
import asyncio


async def wait_random(max_delay: int = 10):
    number = random.uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
