import unittest
from unittest.mock import patch
from io import StringIO
from models import console

class TestConsole(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """Test the do_EOF method"""
        cmd = console.HBNBCommand()
        self.assertTrue(cmd.do_EOF(""))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """Test the do_quit method"""
        cmd = console.HBNBCommand()
        self.assertTrue(cmd.do_quit(""))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test the emptyline method"""
        cmd = console.HBNBCommand()
        cmd.emptyline()
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Test the do_create method"""
        cmd = console.HBNBCommand()
        cmd.do_create("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test the do_show method"""
        cmd = console.HBNBCommand()
        cmd.do_show("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """Test the do_destroy method"""
        cmd = console.HBNBCommand()
        cmd.do_destroy("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """Test the do_all method"""
        cmd = console.HBNBCommand()
        cmd.do_all("")
        self.assertEqual(mock_stdout.getvalue(), "[]\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        """Test the do_update method"""
        cmd = console.HBNBCommand()
        cmd.do_update("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        """Test the do_count method"""
        cmd = console.HBNBCommand()
        cmd.do_count("")
        self.assertEqual(mock_stdout.getvalue(), "0\n")

if __name__ == '__main__':
    unittest.main()
