#!/usr/bin/env python3
"""
Tests for utility functions
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping[str, Any],
                               path: Sequence[str], expected: Any) -> None:
        """
        Test the access_nested_map method.
        Args:
            nested_map (Mapping[str, Any]): A dictionary that may have nested dictionaries.
            path (Sequence[str]): Keys to get to the required value in the nested dictionary.
            expected (Any): The expected result.
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping[str, Any],
                                         path: Sequence[str], missing_key: str) -> None:
        """
        Test that access_nested_map raises a KeyError for invalid paths.
        Args:
            nested_map (Mapping[str, Any]): A dictionary that may have nested dictionaries.
            path (Sequence[str]): Keys to get to the required value in the nested dictionary.
            missing_key (str): The key that is missing in the path.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], missing_key)


class TestGetJson(unittest.TestCase):
    """
    Tests the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: dict, mock_get) -> None:
        """
        Test the get_json method to ensure it returns the expected output.
        Args:
            test_url (str): URL to send HTTP request to.
            test_payload (dict): Expected JSON response.
            mock_get (MagicMock): Mocked requests.get.
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Tests the memoize decorator
    """
    def test_memoize(self) -> None:
        """
        Test that the memoize decorator caches the result of a method.
        """
        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        with patch.object(TestClass, 'a_method', wraps=TestClass.a_method) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property(), 42)
            self.assertEqual(test_instance.a_property(), 42)
            mock_method.assert_called_once()

if __name__ == "__main__":
    unittest.main()
