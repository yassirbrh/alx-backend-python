#!/usr/bin/env python3
'''
    Type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.
'''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    '''
        make_multiplier: function
        @k: The float value of the multiplier
        return: Function that multiplies a float by multiplier.
    '''
    def inner(value: float) -> float:
        return float(value * multiplier)
    return inner
