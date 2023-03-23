#!/usr/bin/python3
''' This module defines a database storage'''
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from models.base_model import BaseModel, Base


class DBStorage:
    ''' class that defines a database storage '''
    __engine = None
    __session = None
    classes = {'User': User, 'State': State, 'Amenity': Amenity, 'Place': Place,
    'Review': Review, 'City': City}
	
    def __init__(self):
        ''' Instatiates attributes '''
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        hbnb_dev = os.getenv('HBNB_ENV')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        if hbnb_dev == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' Query on the current database session all objects 
        depending on class name
        '''
        cls = classes.get(cls, None)
        if cls == None:
            self.__session.query(cls).all()
        else:
            dictionary = {}
            query = self.__session.query(cls).all()
            for objects in query:
                dictionary[objects.__class__.__name__ + '.' + objects.id] = objects
            return dictionary

    def new(self, obj):
        ''' adds the object to the current database session '''
        self.__session.add(obj)

    def save(self):
        ''' commits all changes to the database session '''
        self.__session.commit()

    def delete(self, obj=None):
        ''' delete from the current database session obj if not None '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        ''' creates all tables in the database'''
        #Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)
