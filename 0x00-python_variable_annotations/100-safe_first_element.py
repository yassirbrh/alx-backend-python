#!/usr/bin/env python3
'''
    Type-annotated function element_length that takes an Iterable
    and returns a list of tuples containing the iterable elements
    and their lengths.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
        safe_first_element: function
        @lst: The sequence of elements with type of Any.
        return: Any value or nothing.
    '''
    if lst:
        return lst[0]
    else:
        return None
