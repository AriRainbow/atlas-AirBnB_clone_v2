#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ The state class, contains cities and name """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    # For FileStorage
    @property
    def cities(self):
        """Getter attribute that returns the list of City instances with
        state_id equals to the current State.id, if storage engine 
        is not DBStorage. """
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
        return []
