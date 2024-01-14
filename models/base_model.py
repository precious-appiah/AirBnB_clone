#!/usr/bin/env python3
# base model from which all other classes inherit
"""This is the base model of our AirBnB Project"""

from datetime import datetime
import time
import uuid
from models import storage


class BaseModel():
    """This is the mother class that all our
    models will be inheriting from"""

    def __init__(self, *args, **kwargs):
        """initializes instances either from a dictionary
        or totally new"""
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now().isoformat()
            storage.new(self)

    def save(self):
        """updates the updated_at time and saves an instance
        to the storage file"""
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def __str__(self):
        """String represantion of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """Converts an instance to a dictionary object"""
        object_dict = self.__dict__
        object_dict['__class__'] = self.__class__.__name__
        return object_dict
