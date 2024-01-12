#!/usr/bin/python3
import unittest
from models import city


class TestCity(unittest.TestCase):

    def test_init(self):
        """Test the __init__ method"""
        # Create a new City instance
        city = city.City()

        # Check the attributes of the new instance
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str(self):
        """Test the __str__ method"""
        # Create a new City instance
        city = city.City()

        # Get the string representation of the instance
        output = str(city)

        # Check the format of the string representation
        self.assertEqual(output, "[City] [{}] {}".format(
            city.id, city.__dict__))
