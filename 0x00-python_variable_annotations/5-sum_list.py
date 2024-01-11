#!/usr/bin/env python3
'''
    Type-annotated function sum_list which takes a list input_list of floats
    as argument and returns their sum as a float.
'''
import typing


def sum_list(input_list: typing.List[float]) -> float:
    '''
        sum_list: function
        @input_list: Array of float values.
        return: The sum of the float values.
    '''
    return sum(input_list)
