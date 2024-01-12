import unittest
from models import base_model


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test the __init__ method"""
        # Create a new BaseModel instance
        model = base_model.BaseModel()

        # Check the attributes of the new instance
        self.assertEqual(model.id, str(uuid.uuid4()))
        self.assertEqual(model.created_at, datetime.now())
        self.assertEqual(model.updated_at, model.created_at)

    def test_setattr(self):
        """Test the __setattr__ method"""
        # Create a new BaseModel instance
        model = base_model.BaseModel()

        # Set the value of an attribute
        model.name = "John Doe"

        # Check the value of the attribute
        self.assertEqual(model.name, "John Doe")

        # Try to set the value of an attribute to an invalid type
        with self.assertRaises(AttributeError):
            model.name = 12345

    def test_str(self):
        """Test the __str__ method"""
        # Create a new BaseModel instance
        model = base_model.BaseModel()

        # Get the string representation of the instance
        output = str(model)

        # Check the format of the string representation
        self.assertEqual(output, "[BaseModel] [{}] {}".format(
            model.id, model.__dict__))

    def test_save(self):
        """Test the save method"""
        # Create a new BaseModel instance
        model = base_model.BaseModel()

        # Save the instance
        model.save()

        # Check that the updated_at attribute has been updated
        self.assertNotEqual(model.updated_at, model.created_at)
