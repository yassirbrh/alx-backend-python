#!/usr/bin/env python3
'''
    Coroutine called async_comprehension that takes no arguments.
    The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator
    then return the 10 random numbers.
'''
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
        async_comprehension: function
        return: 10 random numbers between 0 and 10 in list.
    '''
    return [elem async for elem in async_generator()]
