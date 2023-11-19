import unittest
from models.state import State
from models import storage
from datetime import datetime
import os


class StateTest(unittest.TestCase):
    """ This is a model that holds the yest cases for class State """

    def test_state_model(self):
        """ This is a model the test the attribute by default """

        state1 = State()

        self.assertEqual(len(state1.id), 36)
        self.assertTrue(type(state1.created_at) is datetime)
        self.assertTrue(type(state1.updated_at) is datetime)
        self.assertTrue(type(state1.name) is str)
        # self.assertTrue(state1.created_at == state1.updated_at)

    def test_state_model_two(self):
        """ This is a model that test the value by default """
        state1 = State()

        self.assertEqual(state1.name, "")

    def test_state_model_three(self):
        """ This is a model that test the input value by the user """

        state1 = State()
        state1.name = "new_state"

        self.assertEqual(state1.name, "new_state")
        self.assertTrue(type(state1.name) is str)

    def test_state_model_args(self):
        """ This is a test model state that test with args"""

        state1 = State(2, 5)

        self.assertTrue(state1.id is not None)
        self.assertTrue(state1.id != 2)
        self.assertTrue(state1.id != 5)

        self.assertTrue(state1.created_at is not None)
        self.assertTrue(state1.created_at != 2)
        self.assertTrue(state1.created_at != 5)

        self.assertTrue(state1.updated_at is not None)
        self.assertTrue(state1.updated_at != 2)
        self.assertTrue(state1.updated_at != 5)

    def test_state_kwargs(self):
        """This is a test model that test the state class with kwargs"""

        state1 = State()
        state1.name = "new_state"
        state1_to_dict = state1.to_dict()
        state2 = State(**state1_to_dict)

        self.assertTrue(state1 is not state2)
        self.assertEqual(state1.id, state2.id)
        self.assertEqual(state1.created_at, state2.created_at)
        self.assertEqual(state1.updated_at, state2.updated_at)
        self.assertEqual(state1.name, state2.name)

    def test_state_str(self):
        """This is a test model that test the __str__ method"""

        state1 = State()
        display_str = "[{}] ({}) {}".format(state1.__class__.__name__,
                                            state1.id, state1.__dict__)

        self.assertEqual(state1.__str__(), display_str)

    def test_state_save(self):
        """This is a method that test the save method"""

        state1 = State()

        self.assertNotEqual(state1.created_at, state1.updated_at)

        state1.save()
        self.assertTrue(state1.created_at != state1.updated_at)

        filename = "file.json"
        # checkif the file exists
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(os.path.isfile(filename))

        os.remove(filename)

    def test_state_save_args(self):
        """This is a method that test the save method with args"""

        state1 = State()

        with self.assertRaises(TypeError):
            state1.save(2, 4)

    def test_state_dict(self):
        """This is a test model that test the to_dict method"""

        state1 = State()

        state1.name = "new_state"
        state1_to_dict = state1.to_dict()
        dict_field = [
            "__class__", "updated_at", "created_at", "id", "name"
        ]

        self.assertTrue(type(state1_to_dict) is dict)
        for attr in dict_field:
            self.assertTrue(attr in state1_to_dict)
