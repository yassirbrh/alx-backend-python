#!/usr/bin/env python3
'''
    Type-annotated function to_kv that takes a string k and an int OR float v
    The first element of the tuple is the string k.
    The second element is the square of the int/float v
    and should be annotated as a float.
'''
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    '''
        to_kv: function
        @k: A string.
        @v: A tuple of two values string and float.
        return: The tuple containing the string k and the number v square.
    '''
    return (str(k), pow(v, 2))
