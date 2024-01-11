#!/usr/bin/env python3
'''
    Type-annotated function add that takes a float a and a float b
    as arguments and returns their sum as a float.
'''


def add(a: float, b: float) -> float:
    '''
        add: function
        @a: First float value.
        @b: Second float value.
        return: The sum of the two values a float.
    '''
    return float(a + b)
