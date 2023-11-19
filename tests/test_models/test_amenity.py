import unittest
from models.amenity import Amenity
from models import storage
from datetime import datetime
import os


class AmenityTest(unittest.TestCase):
    """ This is a model that holds the yest cases for class amenity """

    def test_amenity_model(self):
        """ This is a model the test the attribute by default """

        amenity1 = Amenity()

        self.assertEqual(len(amenity1.id), 36)
        self.assertTrue(type(amenity1.created_at) is datetime)
        self.assertTrue(type(amenity1.updated_at) is datetime)
        self.assertTrue(type(amenity1.name) is str)
        # self.assertTrue(amenity1.created_at == amenity1.updated_at)

    def test_amenity_model_two(self):
        """ This is a model that test the value by default """
        amenity1 = Amenity()

        self.assertEqual(amenity1.name, "")

    def test_amenity_model_three(self):
        """ This is a model that test the input value by the user """

        amenity1 = Amenity()
        amenity1.name = "new_amenity"

        self.assertEqual(amenity1.name, "new_amenity")
        self.assertTrue(type(amenity1.name) is str)

    def test_amenity_model_args(self):
        """ This is a test model amenity that test with args"""

        amenity1 = Amenity(2, 5)

        self.assertTrue(amenity1.id is not None)
        self.assertTrue(amenity1.id != 2)
        self.assertTrue(amenity1.id != 5)

        self.assertTrue(amenity1.created_at is not None)
        self.assertTrue(amenity1.created_at != 2)
        self.assertTrue(amenity1.created_at != 5)

        self.assertTrue(amenity1.updated_at is not None)
        self.assertTrue(amenity1.updated_at != 2)
        self.assertTrue(amenity1.updated_at != 5)

    def test_amenity_kwargs(self):
        """This is a test model that test the amenity class with kwargs"""

        amenity1 = Amenity()
        amenity1.name = "new_amenity"
        amenity1_to_dict = amenity1.to_dict()
        amenity2 = Amenity(**amenity1_to_dict)

        self.assertTrue(amenity1 is not amenity2)
        self.assertEqual(amenity1.id, amenity2.id)
        self.assertEqual(amenity1.created_at, amenity2.created_at)
        self.assertEqual(amenity1.updated_at, amenity2.updated_at)
        self.assertEqual(amenity1.name, amenity2.name)

    def test_amenity_str(self):
        """This is a test model that test the __str__ method"""

        amenity1 = Amenity()
        display_str = "[{}] ({}) {}".format(amenity1.__class__.__name__,
                                            amenity1.id, amenity1.__dict__)

        self.assertEqual(amenity1.__str__(), display_str)

    def test_amenity_save(self):
        """This is a method that test the save method"""

        amenity1 = Amenity()

        self.assertNotEqual(amenity1.created_at, amenity1.updated_at)

        amenity1.save()
        self.assertTrue(amenity1.created_at != amenity1.updated_at)

        filename = "file.json"
        # checkif the file exists
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(os.path.isfile(filename))

        os.remove(filename)

    def test_amenity_save_args(self):
        """This is a method that test the save method with args"""

        amenity1 = Amenity()

        with self.assertRaises(TypeError):
            amenity1.save(2, 4)

    def test_amenity_dict(self):
        """This is a test model that test the to_dict method"""

        amenity1 = Amenity()

        amenity1.name = "new_amenity"
        amenity1_to_dict = amenity1.to_dict()
        dict_field = [
            "__class__", "updated_at", "created_at", "id", "name"
        ]

        self.assertTrue(type(amenity1_to_dict) is dict)
        for attr in dict_field:
            self.assertTrue(attr in amenity1_to_dict)
