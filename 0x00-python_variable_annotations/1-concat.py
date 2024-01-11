#!/usr/bin/env python3
'''
    Type-annotated function concat that takes a string str1 and a string str2
    as arguments and returns a concatenated string.
'''


def concat(str1: str, str2: str) -> str:
    '''
        concat: function
        @str1: First string value.
        @str2: Second string value.
        return: The concatenated string of str1 and str2
    '''
    return str(str1 + str2)
