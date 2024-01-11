#!/usr/bin/env python3
'''
    Type-annotated function zoom_array.
'''
from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
        zoom_array: function
        @lst: A tuple.
        @factor: An integer.
        return: A tuple.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
