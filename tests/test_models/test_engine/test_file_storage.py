import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage
import os


class FileStorageTest(unittest.TestCase):
    """ This is a class FileStorageTest that holds test cases """

    storageTest = FileStorage()
    storageObj = storageTest._FileStorage__objects
    storageFile = storageTest._FileStorage__file_path

    @classmethod
    def setUpClass(cls):
        """This is the default class method of the test"""

        objs = cls.storageTest._FileStorage__objects.copy()

        for key in objs.keys():
            del cls.storageTest._FileStorage__objects[key]

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_storage(self):
        """ This is a method that test the file storage by default"""

        self.assertTrue(type(self.storageFile) is str)
        self.assertTrue(type(self.storageObj) is dict)

    def test_storage_two(self):
        """This is a method that test the value of the file storage by
        default"""

        self.assertEqual(self.storageFile, "file.json")
        self.assertNotEqual(self.storageObj, {})

    def test_storage_new_storage(self):
        """This is a method that process the storage"""

        amenity1 = Amenity()
        base1 = BaseModel()
        city1 = City()
        state1 = State()
        place1 = Place()
        review1 = Review()
        user1 = User()
        objs = [amenity1, base1, city1, state1, place1, review1, user1]

        self.assertEqual(len(objs), 7)

        # testing each objs in __object if their are the same model
        i = 0
        for key, value in self.storageObj.items():
            obj_key = "{}.{}".format(objs[i].__class__.__name__, objs[i].id)
            self.assertEqual(obj_key, key)
            self.assertTrue(value is objs[i])
            i += 1

    def test_storage_more_args(self):
        """ This is a method that test the file storege with args"""

        with self.assertRaises(TypeError):
            self.storageTest.new("base1", "state1")

    def test_storge_all(self):
        """This is test storage that test the all the method"""

        objs = self.storageTest.all()

        self.assertTrue(type(objs) is dict)

        for key, value in objs.items():
            self.assertTrue(key in self.storageObj)
            self.assertTrue(value, self.storageObj[key])

        self.assertTrue(objs is self.storageObj)

    def test_storage_save_and_reload(self):
        """ This is a test storage file that save and reload the method"""

        # testing to check if the file exits
        self.assertFalse(os.path.exists(self.storageFile))

        # we have to call the save method
        self.storageTest.save()

        self.assertTrue(os.path.exists(self.storageFile))
        self.assertTrue(os.path.isfile(self.storageFile))

        # to test this first delete all the objects in __objects file
        obj_dict = self.storageObj.copy()
        for key, value in obj_dict.items():
            del self.storageObj[key]

        self.assertEqual(len(self.storageObj), 0)
        self.assertEqual(len(self.storageTest._FileStorage__objects), 0)

        # Then we call the reload
        self.storageTest.reload()
        FileStorageTest.storageObj = self.storageTest._FileStorage__objects

        # Then we check if the object has been reload
        self.assertEqual(len(self.storageObj), 7)
        self.assertEqual(len(self.storageTest._FileStorage__objects), 7)

        # Check each model
        i = 0
        models = [BaseModel, User, State, City, Amenity, Place, Review]
        for key, value in self.storageObj.items():
            self.assertFalse(type(value) is models[i])
            i += 1

    def test_storage_save_args(self):
        """This is a method that save the method with args"""

        with self.assertRaises(TypeError):
            self.storageTest.save("Good")

    def test_storage_reload_args(self):
        """This is a method that reload the method with args"""
        with self.assertRaises(TypeError):
            self.storageTest.save(12)

    @classmethod
    def tearDownClass(cls):
        """This is a method that is call after the test"""

        objs = cls.storageTest._FileStorage__objects.copy()

        for key in objs.keys():
            del cls.storageTest._FileStorage__objects[key]
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
