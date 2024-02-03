#!/usr/bin/env python3
'''
    TestAccessNestedMap class that inherits from unittest.TestCase.
'''
from parameterized import parameterized
from typing import Dict, Tuple, Union
import unittest
from unittest.mock import Mock, patch


access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


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


class TestGetJson(unittest.TestCase):
    '''
        class TestGetJson that inherits from unittest.TestCase.
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''
            test_get_json: function
            @self: class constructor.
            @mock_get: mocked function
            return: the Mock object.
        '''
        mock_object = Mock()
        mock_object.json = Mock(return_value=test_payload)
        mock_get.return_value = mock_object
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
