#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    # amenity_ids = []

    reviews = relationship('Review', backref='place',
                           cascade='delete, all, delete-orphan')

    @property
    def reviews(self):
        ''' Returns the list of Review instances
        with place_id equals to current Place.id'''
        review = models.storage.all('Review').values()
        review_list = []
        for reviews in review:
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
