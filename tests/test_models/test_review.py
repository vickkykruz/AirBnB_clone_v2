import unittest
from models.review import Review
from models import storage
from datetime import datetime
import os


class ReviewTest(unittest.TestCase):
    """ This is a model that holds the yest cases for class review """

    def test_review_model(self):
        """ This is a model the test the attribute by default """

        review1 = Review()

        self.assertEqual(len(review1.id), 36)
        self.assertTrue(type(review1.created_at) is datetime)
        self.assertTrue(type(review1.updated_at) is datetime)
        self.assertTrue(type(review1.place_id) is str)
        self.assertTrue(type(review1.user_id) is str)
        self.assertTrue(type(review1.text) is str)
        # self.assertTrue(review1.created_at == review1.updated_at)

    def test_review_model_two(self):
        """ This is a model that test the value by default """
        review1 = Review()

        self.assertEqual(review1.user_id, "")
        self.assertEqual(review1.place_id, "")
        self.assertEqual(review1.text, "")

    def test_review_model_three(self):
        """ This is a model that test the input value by the user """

        review1 = Review()
        review1.text = "new_review"
        review1.place_id = "2345"
        review1.user_id = "1234"

        self.assertEqual(review1.text, "new_review")
        self.assertEqual(review1.place_id, "2345")
        self.assertEqual(review1.user_id, "1234")

    def test_review_model_args(self):
        """ This is a test model review that test with args"""

        review1 = Review(2, 5)

        self.assertTrue(review1.id is not None)
        self.assertTrue(review1.id != 2)
        self.assertTrue(review1.id != 5)

        self.assertTrue(review1.created_at is not None)
        self.assertTrue(review1.created_at != 2)
        self.assertTrue(review1.created_at != 5)

        self.assertTrue(review1.updated_at is not None)
        self.assertTrue(review1.updated_at != 2)
        self.assertTrue(review1.updated_at != 5)

    def test_review_kwargs(self):
        """This is a test model that test the review class with kwargs"""

        review1 = Review()
        review1.name = "new_review"
        review1_to_dict = review1.to_dict()
        review2 = Review(**review1_to_dict)

        self.assertTrue(review1 is not review2)
        self.assertEqual(review1.id, review2.id)
        self.assertEqual(review1.created_at, review2.created_at)
        self.assertEqual(review1.updated_at, review2.updated_at)
        self.assertEqual(review1.name, review2.name)

    def test_review_str(self):
        """This is a test model that test the __str__ method"""

        review1 = Review()
        display_str = "[{}] ({}) {}".format(review1.__class__.__name__,
                                            review1.id, review1.__dict__)

        self.assertEqual(review1.__str__(), display_str)

    def test_review_save(self):
        """This is a method that test the save method"""

        review1 = Review()

        self.assertNotEqual(review1.created_at, review1.updated_at)

        review1.save()
        self.assertTrue(review1.created_at != review1.updated_at)

        filename = "file.json"
        # checkif the file exists
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(os.path.isfile(filename))

        os.remove(filename)

    def test_review_save_args(self):
        """This is a method that test the save method with args"""

        review1 = Review()

        with self.assertRaises(TypeError):
            review1.save(2, 4)

    def test_review_dict(self):
        """This is a test model that test the to_dict method"""

        review1 = Review()

        review1.name = "new_review"
        review1_to_dict = review1.to_dict()
        dict_field = [
            "__class__", "updated_at", "created_at", "id", "name"
        ]

        self.assertTrue(type(review1_to_dict) is dict)
        for attr in dict_field:
            self.assertTrue(attr in review1_to_dict)
