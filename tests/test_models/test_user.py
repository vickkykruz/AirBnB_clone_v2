import unittest
from models.user import User
from datetime import datetime
from models import storage
import os


class UserTest(unittest.TestCase):
    """ This is the User class that hold the test cases for the user """

    def test_user_one(self):
        """ This is the method the that test the initalixation """

        userOne = User()

        # Testing for the default type
        self.assertEqual(len(userOne.id), 36)
        self.assertTrue(type(userOne.created_at) is datetime)
        self.assertTrue(type(userOne.updated_at) is datetime)
        self.assertTrue(type(userOne.first_name) is str)
        self.assertTrue(type(userOne.last_name) is str)
        self.assertTrue(type(userOne.email) is str)
        self.assertTrue(type(userOne.password) is str)

    def test_user_two(self):
        """ This is a test mthod that test the default """

        users = User()

        # Testing the value by default
        self.assertEqual(users.first_name, "")
        self.assertEqual(users.last_name, "")
        self.assertEqual(users.email, "")
        self.assertEqual(users.password, "")

    def test_user_three(self):
        """ This is a method that tests the input placed by the user """

        user = User()
        user.first_name = "Victor"
        user.last_name = "Chukwuemeka"
        user.email = "onwuegbuchulemvic02@gmail.com"
        user.password = "1234"

        self.assertTrue(type(user.id) is str)
        self.assertEqual(user.first_name, "Victor")
        self.assertEqual(user.last_name, "Chukwuemeka")
        self.assertEqual(user.email, "onwuegbuchulemvic02@gmail.com")
        self.assertEqual(user.password, "1234")

    def test_user_kwargs(self):
        """ This is a test method that test the usermodel with the kwargs """

        user = User()
        user.email = "user@example.com"
        user.first_name = "user_one"
        user_dict = user.to_dict()
        user_two = User(**user_dict)

        self.assertTrue(user is not user_two)
        self.assertEqual(user.id, user_two.id)
        self.assertEqual(user.email, user_two.email)
        self.assertEqual(user.first_name, user_two.first_name)
        self.assertEqual(user.created_at, user_two.created_at)
        self.assertEqual(user.updated_at, user_two.updated_at)

    def test_user_str(self):
        """ This is a test method that test the __str__ method """

        user = User()

        display_str = "[{}] ({}) {}".format(user.__class__.__name__, user.id,
                                            user.__dict__)

        self.assertEqual(user.__str__(), display_str)

    def test_user_save(self):
        """ This is a model that test the save functionality """

        user = User()

        self.assertNotEqual(user.created_at, user.updated_at)
        user.save()

        self.assertTrue(user.created_at != user.updated_at)
        filename = "file.json"

        self.assertTrue(os.path.exists(filename))
        self.assertTrue(os.path.isfile(filename))

        os.remove(filename)

    def test_user_save_args(self):
        """ This is a model the test the save mothod with args """

        user = User()

        with self.assertRaises(TypeError):
            user.save(1, 3)

    def test_user_to_dict(self):
        """ This is a model that test the dictionary of the method user """

        user = User()

        user.email = "user@example.com"
        user.first_name = "user"
        user_to_dict = user.to_dict()
        dict_field = [
                "__class__",
                "updated_at",
                "created_at",
                "id",
                "email",
                "first_name"
                ]
        self.assertTrue(type(user_to_dict) is dict)

        for attr in dict_field:
            self.assertTrue(attr in user_to_dict)
