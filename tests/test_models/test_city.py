import unittest
from models.city import City
from models import storage
from datetime import datetime
import os


class CityTest(unittest.TestCase):
    """ This is a model that holds the yest cases for class city """

    def test_city_model(self):
        """ This is a model the test the attribute by default """

        city1 = City()

        self.assertEqual(len(city1.id), 36)
        self.assertTrue(type(city1.created_at) is datetime)
        self.assertTrue(type(city1.updated_at) is datetime)
        self.assertTrue(type(city1.name) is str)
        # self.assertTrue(city1.created_at == city1.updated_at)

    def test_city_model_two(self):
        """ This is a model that test the value by default """
        city1 = City()

        self.assertEqual(city1.name, "")

    def test_city_model_three(self):
        """ This is a model that test the input value by the user """

        city1 = City()
        city1.name = "new_city"

        self.assertEqual(city1.name, "new_city")
        self.assertTrue(type(city1.name) is str)

    def test_city_model_args(self):
        """ This is a test model city that test with args"""

        city1 = City(2, 5)

        self.assertTrue(city1.id is not None)
        self.assertTrue(city1.id != 2)
        self.assertTrue(city1.id != 5)

        self.assertTrue(city1.created_at is not None)
        self.assertTrue(city1.created_at != 2)
        self.assertTrue(city1.created_at != 5)

        self.assertTrue(city1.updated_at is not None)
        self.assertTrue(city1.updated_at != 2)
        self.assertTrue(city1.updated_at != 5)

    def test_city_kwargs(self):
        """This is a test model that test the city class with kwargs"""

        city1 = City()
        city1.name = "new_city"
        city1_to_dict = city1.to_dict()
        city2 = City(**city1_to_dict)

        self.assertTrue(city1 is not city2)
        self.assertEqual(city1.id, city2.id)
        self.assertEqual(city1.created_at, city2.created_at)
        self.assertEqual(city1.updated_at, city2.updated_at)
        self.assertEqual(city1.name, city2.name)

    def test_city_str(self):
        """This is a test model that test the __str__ method"""

        city1 = City()
        display_str = "[{}] ({}) {}".format(city1.__class__.__name__,
                                            city1.id, city1.__dict__)

        self.assertEqual(city1.__str__(), display_str)

    def test_city_save(self):
        """This is a method that test the save method"""

        city1 = City()

        self.assertNotEqual(city1.created_at, city1.updated_at)

        city1.save()
        self.assertTrue(city1.created_at != city1.updated_at)

        filename = "file.json"
        # checkif the file exists
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(os.path.isfile(filename))

        os.remove(filename)

    def test_city_save_args(self):
        """This is a method that test the save method with args"""

        city1 = City()

        with self.assertRaises(TypeError):
            city1.save(2, 4)

    def test_city_dict(self):
        """This is a test model that test the to_dict method"""

        city1 = City()

        city1.name = "new_city"
        city1_to_dict = city1.to_dict()
        dict_field = [
            "__class__", "updated_at", "created_at", "id", "name"
        ]

        self.assertTrue(type(city1_to_dict) is dict)
        for attr in dict_field:
            self.assertTrue(attr in city1_to_dict)
