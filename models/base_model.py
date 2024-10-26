#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

#Define Base for SQLAlchemy if DBSTorage is active
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    # SQLAlchemy columns (only if DBStorage is active)
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.timezone.utc)
    updated_at = Column(DateTime, nullable=False, default=datetime.timezone.utc)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model with SQLAlchemy compatibility"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = self.__class__.__name__
        return f'[{cls}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now(timezone.utc)  # timezone-aware datetime
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes current instance from storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format, excluding SQLAlchemy state"""
        dictionary = {key: (value if not isinstance(value, datetime)
                            else value.isoformat())
                    for key, value in self.__dict__.items()
                    if key != '_sa_instance_state'}
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
