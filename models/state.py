#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state',
                          cascade='delete, all, delete-orphan')

    @property
    def cities(self):
        ''' Returns the list of City instances with state_id equals State.id'''
        cities = []
        for city in FileStorage.__objects.get('City', {}).values():
            if city['state_id'] == self.id:
                cities.append(City(**city))
        return cities
