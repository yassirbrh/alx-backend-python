#!/usr/bin/env python3
'''
    TestAccessNestedMap class that inherits from unittest.TestCase.
'''
from parameterized import parameterized
from typing import Dict, Tuple, Union
import unittest


access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
        Class that inherits from unittest.TestCase to test access_nested_map.
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            output: Union[int, Dict]
            ) -> None:
        '''
            test_access_nested_map: function
            @self: class constructor.
            @nested_map: nested map to get the values from it.
            @path: the path to follow to get the output.
            @output: the output to get.
            return: no return
        '''
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exp: Exception
            ) -> None:
        '''
            test_access_nested_map_exception: function
            @self: class constructor.
            @nested_map: nested map to get the values from it.
            @path: the path to follow to get the output.
            @exp: the exception to throw.
            return: no return
        '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
