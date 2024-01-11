#!/usr/bin/env python3
'''
    Type-annotated function safely_get_value that takes a Mapping object
    and a key and returns the value correspending in the Mapping object
    or default value.
'''
from typing import Any, Sequence, Union, Mapping, TypeVar

T = TypeVar('T')
Default = Union[T, None]
Res = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Default = None) -> Res:
    '''
        safely_get_value: function
        @dct: Mapping object.
        @key: A key of any type.
        @default: A T object or nothing.
        return: Any value or T object.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
