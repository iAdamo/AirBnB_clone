#!/usr/bin/python3
"""
test_place module: A unittest subclass for testing place module

All your tests should be executed by using this command:
(python3 -m unittest discover tests)
or
(python3 -m unittest tests/test_models/test_place.py)
"""

from models import place
import inspect
import unittest


class Testplace(unittest.TestCase):
    """
    Testplace: (class) - unittest subclass to run test cases on place
    """
    @classmethod
    def setUp(cls):
        """
        setUp: (class method) - method for sharing resources across all methods

        setup: assigned with a list of all the functions in BaseModel
        """
        cls.setup = inspect.getmembers(place.BaseModel,
                                       inspect.isfunction)

    def test_module_docs(self):
        """
        test for module docstring
        """
        self.assertTrue(len(place.__doc__) >= 1)

    def test_class_docs(self):
        """
        test for class docstring
        """
        self.assertTrue(len(place.BaseModel.__doc__) >= 1)

    def test_function_docs(self):
        """
        test for functions docstrings
        """
        for each_func in self.setup:
            self.assertTrue(len(each_func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
