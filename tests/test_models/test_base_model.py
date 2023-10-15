#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:09 2020
@author: meco
"""
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
import uuid
from contextlib import redirect_stdout
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    class for testing BaseModel class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def setUp(self):
        """Set up method for object BM of BAseModel"""
        self.BM = BaseModel()

    def tearDown(self):
        """Set tmp object"""
        self.BM = None

    def test_pep8_conformance_BaseModel(self):
        """
        Test that base_model.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_BaseModel(self):
        """
        Test that test_base_model.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/\
                                        test_base_model.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_type(self):
        """test method for type testing of BaseModel
        """
        self.assertIsInstance(self.BM, BaseModel)
        self.assertEqual(type(self.BM), BaseModel)

    def test_basic_attribute_set(self):
        """test method for basic attribute assignment
        """
        self.BM.first_name = 'Meco'
        self.BM.last_name = 'Montes'
        self.assertEqual(self.BM.first_name, 'Meco')
        self.assertEqual(self.BM.last_name, 'Montes')

    def test_str(self):
        """tests str method
        """
        string = str(self.BM)
        BMid = "[{}] ({}) {}".format(self.BM.__class__.__name__, self.BM.id,
                                     self.BM.__dict__)
        test = BMid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime" in string
        self.assertEqual(True, test)

    def test_to_dict(self):
        """tests to_dict method
        """
        my_dict = self.BM.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.BM.created_at.isoformat())
        self.assertEqual(datetime, type(self.BM.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.BM.__class__.__name__)
        self.assertEqual(my_dict['id'], self.BM.id)

    def test_to_dict_more(self):
        """tests to_dict method
        """
        my_dict = self.BM.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.BM.created_at, time)

    def test_from_dict_basic(self):
        """tests from_dict method
        """
        my_dict = self.BM.to_dict()
        BM1 = BaseModel(**my_dict)
        self.assertEqual(BM1.id, self.BM.id)
        self.assertEqual(BM1.updated_at, self.BM.updated_at)
        self.assertEqual(BM1.created_at, self.BM.created_at)
        self.assertEqual(BM1.__class__.__name__,
                         self.BM.__class__.__name__)

    def test_from_dict_hard(self):
        """test for the from_dict method for BaseModel objects
        """
        self.BM.student = 'Science'
        my_dict = self.BM.to_dict()
        self.assertEqual(my_dict['student'], 'Science')
        BM1 = BaseModel(**my_dict)
        self.assertEqual(BM1.created_at, self.BM.created_at)

    def test_unique_id(self):
        """test for id in BaseModel objects
        """
        BM1 = BaseModel()
        BM2 = BaseModel()
        self.assertNotEqual(self.BM.id, BM1.id)
        self.assertNotEqual(self.BM.id, BM2.id)

    def test_id_type_string(self):
        """test id in BaseModel is a string
        """
        self.assertEqual(type(self.BM.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.BM.updated_at
        self.BM.save()
        time2 = self.BM.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
