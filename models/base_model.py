#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        kwargs = kwargs if kwargs else {}
        if not kwargs or 'id' not in kwargs:
            kwargs['id'] = str(uuid.uuid4())
        if not kwargs or 'created_at' not in kwargs:
            kwargs['created_at'] = datetime.now().isoformat()
            kwargs['updated_at'] = kwargs['created_at']

        self.__set_attributes(kwargs)

    def __set_attributes(self, attr_dict):
        """
        Sets the attributes of a model instance
        based on **kwargs or default values
        """
        attr_dict_new = {}
        for attr, value in attr_dict.items():
            if attr in ['created_at', 'updated_at']:
                if not isinstance(value, datetime):
                    attr_dict_new[attr] = datetime.strptime(
                        attr_dict[attr], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                attr_dict_new[attr] = value
        for attr, value in attr_dict_new.items():
            if attr == '__class__':
                continue
            setattr(self, attr, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the model instance"""
        obj_to_dict = {**self.__dict__, '__class__': self.__class__.__name__}
        obj_to_dict['created_at'] = obj_to_dict['created_at'].isoformat()
        obj_to_dict['updated_at'] = obj_to_dict['updated_at'].isoformat()
        return obj_to_dict
