import unittest
from models import state

class TestState(unittest.TestCase):

    def test_init(self):
        """Test the __init__ method"""
        # Create a new State instance
        state = state.State()

        # Check the attributes of the new instance
        self.assertEqual(state.name, "")

    def test_str(self):
        """Test the __str__ method"""
        # Create a new State instance
        state = state.State()

        # Get the string representation of the instance
        output = str(state)

        # Check the format of the string representation
        self.assertEqual(output, "[State] [{}] {}".format(
            state.id, state.__dict__))

    def test_save(self):
        """Test the save method"""
        # Create a new State instance
        state = state.State()

        # Save the instance
        state.save()

        # Check that the updated_at attribute has been updated
        self.assertNotEqual(state.updated_at, state.created_at)
