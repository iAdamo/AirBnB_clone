#!/usr/bin/python3
"""
test_city module: A unittest subclass for testing city module

All your tests should be executed by using this command:
(python3 -m unittest discover tests)
or
(python3 -m unittest tests/test_models/test_city.py)
"""

from models import city
import inspect
import unittest


class Testcity(unittest.TestCase):
    """
    Testcity: (class) - unittest subclass to run test cases on city
    """
    @classmethod
    def setUp(cls):
        """
        setUp: (class method) - method for sharing resources across all methods

        setup: assigned with a list of all the functions in BaseModel
        """
        cls.setup = inspect.getmembers(city.BaseModel,
                                       inspect.isfunction)

    def test_module_docs(self):
        """
        test for module docstring
        """
        self.assertTrue(len(city.__doc__) >= 1)

    def test_class_docs(self):
        """
        test for class docstring
        """
        self.assertTrue(len(city.BaseModel.__doc__) >= 1)

    def test_function_docs(self):
        """
        test for functions docstrings
        """
        for each_func in self.setup:
            self.assertTrue(len(each_func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
