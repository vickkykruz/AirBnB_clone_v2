import unittest
from models.place import Place
from models import storage
from datetime import datetime
import os


class PlaceTest(unittest.TestCase):
    """ This is a model that holds the yest cases for class place """

    def test_place_model(self):
        """ This is a model the test the attribute by default """

        place1 = Place()

        self.assertEqual(len(place1.id), 36)
        self.assertTrue(type(place1.created_at) is datetime)
        self.assertTrue(type(place1.updated_at) is datetime)
        self.assertTrue(type(place1.name) is str)
        # self.assertTrue(place1.created_at == place1.updated_at)

    def test_place_model_two(self):
        """ This is a model that test the value by default """
        place1 = Place()

        self.assertEqual(place1.name, "")

    def test_place_model_three(self):
        """ This is a model that test the input value by the user """

        place1 = Place()
        place1.name = "new_place"

        self.assertEqual(place1.name, "new_place")
        self.assertTrue(type(place1.name) is str)

    def test_place_model_args(self):
        """ This is a test model place that test with args"""

        place1 = Place(2, 5)

        self.assertTrue(place1.id is not None)
        self.assertTrue(place1.id != 2)
        self.assertTrue(place1.id != 5)

        self.assertTrue(place1.created_at is not None)
        self.assertTrue(place1.created_at != 2)
        self.assertTrue(place1.created_at != 5)

        self.assertTrue(place1.updated_at is not None)
        self.assertTrue(place1.updated_at != 2)
        self.assertTrue(place1.updated_at != 5)

    def test_place_kwargs(self):
        """This is a test model that test the place class with kwargs"""

        place1 = Place()
        place1.name = "new_place"
        place1_to_dict = place1.to_dict()
        place2 = Place(**place1_to_dict)

        self.assertTrue(place1 is not place2)
        self.assertEqual(place1.id, place2.id)
        self.assertEqual(place1.created_at, place2.created_at)
        self.assertEqual(place1.updated_at, place2.updated_at)
        self.assertEqual(place1.name, place2.name)

    def test_place_str(self):
        """This is a test model that test the __str__ method"""

        place1 = Place()
        display_str = "[{}] ({}) {}".format(place1.__class__.__name__,
                                            place1.id, place1.__dict__)

        self.assertEqual(place1.__str__(), display_str)

    def test_place_save(self):
        """This is a method that test the save method"""

        place1 = Place()

        self.assertNotEqual(place1.created_at, place1.updated_at)

        place1.save()
        self.assertTrue(place1.created_at != place1.updated_at)

        filename = "file.json"
        # checkif the file exists
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(os.path.isfile(filename))

        os.remove(filename)

    def test_place_save_args(self):
        """This is a method that test the save method with args"""

        place1 = Place()

        with self.assertRaises(TypeError):
            place1.save(2, 4)

    def test_place_dict(self):
        """This is a test model that test the to_dict method"""

        place1 = Place()

        place1.name = "new_place"
        place1_to_dict = place1.to_dict()
        dict_field = [
            "__class__", "updated_at", "created_at", "id", "name"
        ]

        self.assertTrue(type(place1_to_dict) is dict)
        for attr in dict_field:
            self.assertTrue(attr in place1_to_dict)
