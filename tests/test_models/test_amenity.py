#!/usr/bin/python3
"""
test_amenity module: A unittest subclass for testing amenity module

All your tests should be executed by using this command:
(python3 -m unittest discover tests)
or
(python3 -m unittest tests/test_models/test_amenity.py)
"""

from models import amenity
import inspect
import unittest


class Testamenity(unittest.TestCase):
    """
    Testamenity: (class) - unittest subclass to run test cases on amenity
    """
    @classmethod
    def setUp(cls):
        """
        setUp: (class method) - method for sharing resources across all methods

        setup: assigned with a list of all the functions in BaseModel
        """
        cls.setup = inspect.getmembers(amenity.BaseModel,
                                       inspect.isfunction)

    def test_module_docs(self):
        """
        test for module docstring
        """
        self.assertTrue(len(amenity.__doc__) >= 1)

    def test_class_docs(self):
        """
        test for class docstring
        """
        self.assertTrue(len(amenity.BaseModel.__doc__) >= 1)

    def test_function_docs(self):
        """
        test for functions docstrings
        """
        for each_func in self.setup:
            self.assertTrue(len(each_func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
