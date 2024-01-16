#!/usr/bin/env python3
'''
    Coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second
    then yield a random number between 0 and 10. Use the random module.
'''
import asyncio
import random


async def async_generator() -> float:
    '''
        async_generator: function
        return: yield a random number between 0 and 10.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
