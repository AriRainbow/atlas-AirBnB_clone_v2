#!/usr/bin/python3
"""This module defines a User class for the database model."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Users.
        email (sqlalchemy String): The user's email address (cannot be null).
        password (sqlalchemy String): The user's password (cannot be null).
        first_name (sqlalchemy String): The user's first name (nullable).
        last_name (sqlalchemy String): The user's last name (nullable).
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    # Places relationship attribute
    places = relationship('Place', backref='user', cascade='all, delete')
