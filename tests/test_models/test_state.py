#!/usr/bin/python3
"""Test the State class with MySQL database storage."""
import MySQLdb
import os
from unittest import TestCase
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test the State class."""

    def __init__(self, *args, **kwargs):
        """Initialize the State test case."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test the type of State name attribute."""
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestStateDB(TestCase):
    """Test State class with database storage."""

    def setUp(self):
        """Set up MySQL connection for tests."""
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Close connection after test."""
        self.db.close()
    
    def test_create_state(self):
        """Test creating a State in the database."""
        # Count the initial number of states
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Create a new state
        new_state = State(name="TestState")
        new_state.save()

        # Check the count again
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Assert the count increased by 1
        self.assertEqual(final_count, initial_count + 1)