#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ Test the HBNBCommand class """

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """ Test the quit command """
        command = HBNBCommand()
        command.do_quit('quit')
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """ Test the create command """
        command = HBNBCommand()
        command.do_create('User')
        self.assertIn('User', mock_stdout.getvalue()) # Adjust

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """ Test the show command """
        command = HBNBCommand()
        command.do_create('User')  # Create a user first
        command.do_show('User id')  # Replace 'id' with a valid id
        self.assertIn('** instance id missing **', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """ Test the destroy command """
        command = HBNBCommand()
        command.do_create('User')  # Create a user first
        command.do_destroy('User id')  # Replace 'id' with a valid id
        self.assertIn('** no instance found **', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """ Test the all command """
        command = HBNBCommand()
        command.do_create('User')
        command.do_all('User')
        self.assertIn('User', mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
    