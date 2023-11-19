import unittest
import sys
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from unittest.mock import patch
from models import storage
from io import StringIO

""" This is a test model that testes the console class """


class ConsoleTest(unittest.TestCase):
    """ This is a class console the tests the method side """

    models = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
            }

    @classmethod
    def setUpClass(cls):
        """ This is a vlass method that used in the created models """

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create BaseModel")
            cls.base_id = fd.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create User")
            cls.user_id = fd.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create State")
            cls.state_id = fd.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create City")
            cls.city_id = fd.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create Place")
            cls.place_id = fd.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create Amenity")
            cls.amenity_id = fd.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create Review")
            cls.review_id = fd.getvalue()[:-1]

    def setUp(self):
        """ This is a test method that testing the call before each test """

        objs = storage.all()
        review_key = "Review.{}".format(self.review_id)
        place_key = "Place.{}".format(self.place_id)

        try:
            objs[review_key]
        except KeyError:
            with patch("sys.stdout", new=StringIO()) as fd:
                HBNBCommand().onecmd("create Review")
                ConsoleTest.review_id = fd.getvalue()[:-1]

        try:
            objs[place_key]
        except KeyError:
            with patch("sys.stdout", new=StringIO()) as fd:
                HBNBCommand().onecmd("create Place")
                ConsoleTest.place_id = fd.getvalue()[:-1]

    def test_creates(self):
        """ This is a method that test for the create command """

        # So we will create the models
        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create BaseModel")
            val = fd.getvalue()[:-1]

            # Tesing of the result in the val is string
            self.assertTrue(type(val) is str)

            objs = storage.all()
            obj_key = "BaseModel.{}".format(val)

            # tesing id tje id are the same
            self.assertEqual(val, objs[obj_key].id)

            # testing of the key is in the storage
            self.assertTrue(obj_key in objs)

            # testing the model to create a user
            with patch("sys.stdout", new=StringIO()) as fd:
                HBNBCommand().onecmd("create BaseModel")
                val = fd.getvalue()[:-1]

                # testing if the value type is a str
                self.assertTrue(type(val) is str)

                objs = storage.all()
                obj_key = "User.{}".format(val)
                self.assertFalse(obj_key in objs)
                # self.assertEqual(val, objs[obj_key].id)

    def test_create_model_wrong(self):
        """ This is a test model that creywd with an unknown type """

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create Users")
            val = fd.getvalue()
            self.assertEqual(val, "** class doesn't exist **\n")

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create MyModel")
            val = fd.getvalue()
            self.assertEqual(val, "** class doesn't exist **\n")

    # Testing the for no model
    def test_create_no_model(self):
        """ This model test if there is no model"""
        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create")
            val = fd.getvalue()
            self.assertEqual(val, "** class name missing **\n")

    # Testinh the show model
    def test_show_no_model(self):
        """ This is a method that test the show no model """
        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("create")
            val = fd.getvalue()[:-1]
            self.assertEqual(val, "** class name missing **")

    def test_delete_model(self):
        """ This is a method that test for delete model """

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("destroy Review {}".format(self.review_id))
            val = fd.getvalue()
            # This context does not print
            self.assertEqual(val, "")

    def test_delete_wrong_model(self):
        """ This is a mothod that tests for wrong model """

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("destroy model")
            val = fd.getvalue()[:-1]
            self.assertEqual(val, "** class doesn't exist **")

    def test_destroy_no_model(self):
        """ This is a method the test the destroy cmd with mo model """

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("destroy")
            val = fd.getvalue()[:-1]
            self.assertEqual(val, "** class name missing **")

    # testing all the models
    def test_all_models(self):
        """ This is a method that tje test all the model """

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("all BaseModel ")
            val = fd.getvalue()[:-1]

            # This will print out an array in form of a string
            objs = storage.all()
            exp_val = []
            for key, value in objs.items():
                if value.__class__.__name__ == "BaseModel":
                    exp_val.append(objs[key].__str__())

            self.assertEqual(val, exp_val.__str__())

        with patch("sys.stdout", new=StringIO()) as fd:
            HBNBCommand().onecmd("all User ")
            val = fd.getvalue()[:-1]

            objs = storage.all()
            exp_val = []
            for key, value in objs.items():
                if value.__class__.__name__ == "User":
                    exp_val.append(objs[key].__str__())
