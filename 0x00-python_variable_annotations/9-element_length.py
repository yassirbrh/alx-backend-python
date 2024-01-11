#!/usr/bin/env python3
'''
    Type-annotated function element_length that takes an Iterable
    and returns a list of tuples containing the iterable elements
    and their lengths.
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
        element_length: function
        @lst: The iterable to check its elements lengths
        return: The list of the tuples containing each element and its length.
    '''
    return [(i, len(i)) for i in lst]
