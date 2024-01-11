#!/usr/bin/env python3
'''
    Type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats as argument and returns their sum as a float.
'''
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    '''
        sum_mixed_list: function
        @mxd_lst: Mixed array of float and int values.
        return: The sum of the values as float.
    '''
    return float(sum(mxd_lst))
