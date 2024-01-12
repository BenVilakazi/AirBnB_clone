#!/usr/bin/python3
import unittest
from models import place


class TestPlace(unittest.TestCase):

    def test_init(self):
        """Test the __init__ method"""
        # Create a new Place instance
        place = place.Place()

        # Check the attributes of the new instance
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.descrption, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.amnenity_ids, [])

    def test_str(self):
        """Test the __str__ method"""
        # Create a new Place instance
        place = place.Place()

        # Get the string representation of the instance
        output = str(place)

        # Check the format of the string representation
        self.assertEqual(output, "[Place] [{}] {}".format(
            place.id, place.__dict__))

    def test_save(self):
        """Test the save method"""
        # Create a new Place instance
        place = place.Place()

        # Save the instance
        place.save()

        # Check that the updated_at attribute has been updated
        self.assertNotEqual(place.updated_at, place.created_at)
