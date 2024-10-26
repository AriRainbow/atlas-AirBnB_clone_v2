#!/usr/bin/python3
"""DBStorage Module for HBNB project """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    """ Database storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the DBStorage """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
        )

        if os.getenv('HBNB_ENV') == 'test':
            self.drop_all()

    def all(self, cls=None):
        """ Queries all objects in the database of a specified class """
        classes = [State, City]  # Add any additional classes here
        results = {}

        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                results[f"{type(obj).__name__}.{obj.id}"] = obj
        else:
            for class_type in classes:
                for obj in self.__session.query(class_type).all():
                    results[f"{type(obj).__name__}.{obj.id}"] = obj
        
        return results
    def new(self, obj):
        """ Adds a new object to the current session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes in the current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the current session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables and session """
        from models.city import City  # Import all classes inheriting Base
        from models.state import State
        
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def drop_all(self):
        """ Drops all tables in the database """
        Base.metadata.drop_all(self.__engine)
