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
        with self.assertRaises(SystemExit):
            command.do_quit('quit')
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """ Test the create command """
        command = HBNBCommand()
        command.do_create('User')
        output = mock_stdout.getvalue().strip()  # Get the output
        self.assertTrue(output)  # Check that output is not empty

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """ Test the show command """
        command = HBNBCommand()
        instance_id = command.do_create('User')  # Create a user first
        command.do_show(instance_id)  # Use the actual instance ID
        self.assertIn('User', mock_stdout.getvalue())
        # Check for the instance name in the output

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout): 
        """ Test the destroy command """
        command = HBNBCommand()
        instance_id = command.do_create('User')  # Create a user first
        command.do_destroy(instance_id)  # Use the actual instance ID
        self.assertIn('** no instance found **', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """ Test the all command """
        command = HBNBCommand()
        instance_id = command.do_create('User')  # Create a user
        command.do_all('User')  # Retrieve all instances
        self.assertIn('User', mock_stdout.getvalue())
        # Check for the instance name in the output


if __name__ == "__main__":
    unittest.main()
