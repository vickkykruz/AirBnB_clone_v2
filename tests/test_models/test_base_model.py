#!/usr/bin/env python3
"""
    This is a test model that testing the atttibutes and method in the base
    model.
"""


import os
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ This is a class TestBaseModel that contains the attributes and methid
        for the functionality of the class
    """

    def test_initialization(self):
        """ This is a method that testes the intialization of the self
            attributes and value
        """
        instClass = BaseModel()
        self.assertIs(type(instClass), BaseModel)
        self.assertEqual(len(instClass.id), 36)
        self.assertTrue(type(instClass.updated_at) is datetime)
        self.assertTrue(type(instClass.created_at) is datetime)
        # self.assertTrue(instClass.created_at == instClass.updated_at)

    def test_base(self):
        """This is a method that tests the base model"""
        instClass = BaseModel()
        instClass.name = "My First Model"
        instClass.my_number = 89

        self.assertTrue(type(instClass.id) is str)
        self.assertEqual(instClass.name, "My First Model")
        self.assertEqual(instClass.my_number, 89)

    def test_base_model_args(self):
        """ This is a test mothod that testes the *args"""
        instClass = BaseModel()

        # Testing that id exist and 2 or 1
        self.assertTrue(instClass.id is not None)
        self.assertTrue(instClass.id != 2)
        self.assertTrue(instClass.id != 1)

        # Testing that the created_at exist and is not 2 or 1
        self.assertTrue(instClass.created_at is not None)
        self.assertTrue(instClass.created_at != 2)
        self.assertTrue(instClass.created_at != 1)

        # Testing that the updated_at exist and is not a number
        self.assertTrue(instClass.updated_at is not None)
        self.assertTrue(instClass.updated_at != 2)
        self.assertTrue(instClass.updated_at != 1)

    def test_base_model_kwargs(self):
        """ This is a test model that tests the *kwargs """
        instClass = BaseModel()

        instClass__dir = instClass.to_dict()
        instClass2__dir = BaseModel(**instClass__dir)

        self.assertEqual(instClass.created_at, instClass2__dir.created_at)
        self.assertEqual(instClass.updated_at, instClass2__dir.updated_at)
        self.assertTrue(instClass is not instClass2__dir)

    # This is a method that print __str__
    def test_base_model_str(self):
        """ This is a test model that tests the __str__ method """
        instClass = BaseModel()

        print_str = "[{}] ({}) {}".format(instClass.__class__.__name__,
                                          instClass.id, instClass.__dict__)
        self.assertEqual(instClass.__str__(), print_str)

    # Testing the method base model save
    def test_base_model_save(self):
        """This is a test model that tests the save method"""
        instClass = BaseModel()

        # Testing if the created_at and the updated_at attribute are the same
        # self.assertEqual(instClass.created_at, instClass.updated_at)
        instClass.save()
        # Saving instClass to a file

        # self.assertTrue(instClass.created_at != instClass.updated_at)
        filename = "file.json"
        # test if that file exist
        self.assertTrue(os.path.exists(filename))
        # test if that file "test_file.json" is a file
        self.assertTrue(os.path.isfile(filename))

        os.remove(filename)

    def test_base_model_save_args(self):
        """This is test model that tests the save method with args """
        instClass = BaseModel()

        with self.assertRaises(TypeError):
            instClass.save(1, 2)

    # testing the to_dict method of the base model
    def test_base_to_dict1(self):
        """ This is a test model that test the method to_dict"""

        instClass = BaseModel()
        instClass_to_dict = instClass.to_dict()
        dict_field = ["__class__", "updated_at", "created_at", "id"]

        self.assertTrue(type(instClass_to_dict) is dict)
        for attr in dict_field:
            self.assertTrue(attr in instClass_to_dict)

    def test_base_to_dict_args(self):
        """ This is a test model that test the methid "to_dict" with args """

        instClass = BaseModel()

        with self.assertRaises(TypeError):
            instClass.to_dict("h")
