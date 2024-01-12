#!/usr/bin/python3
import unittest
from models import review


class TestReview(unittest.TestCase):

    def test_init(self):
        """Test the __init__ method"""
        # Create a new Review instance
        review = review.Review()

        # Check the attributes of the new instance
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str(self):
        """Test the __str__ method"""
        # Create a new Review instance
        review = review.Review()

        # Get the string representation of the instance
        output = str(review)

        # Check the format of the string representation
        self.assertEqual(output, "[Review] [{}] {}".format(
            review.id, review.__dict__))

    def test_save(self):
        """Test the save method"""
        # Create a new Review instance
        review = review.Review()

        # Save the instance
        review.save()

        # Check that the updated_at attribute has been updated
        self.assertNotEqual(review.updated_at, review.created_at)
