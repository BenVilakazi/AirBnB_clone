#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suite for Amenity"""

    def setUp(self):
        """Sets up the test case"""
        self.amenity = Amenity()

    def tearDown(self):
        """Cleans up after each test"""
        del self.amenity

    def test_instance(self):
        """Tests if amenity is an instance of Amenity"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Tests if amenity has the required attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
