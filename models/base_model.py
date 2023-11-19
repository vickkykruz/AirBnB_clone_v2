#!/usr/bin/python3

"""
Classes:
    - BaseModel: The base class for other classes.

Attributes:
    - id (str): A unique identifier for each instance.
    - created_at (datetime): The date and time when the instance is created.
    - updated_at (datetime): The date and time when
                             the instance is last updated.

Methods:
    - __init__(self, *args, **kwargs): Initializes a new instance.
    - __str__(self): Defines a custom string representation for the instance.
    - save(self): Updates the 'updated_at' attribute with the current datetime.
    - to_dict(self): Converts the instance to a dictionary
                      with formatted datetime values.

Usage:
    To use this module, create classes that inherit from BaseModel
    and make use of the common attributes and methods.
"""
from uuid import uuid4
from datetime import datetime

import models


class BaseModel():
    """ The Base Model class """
    def __init__(self, *args, **kwargs):
        """ This method initializes an instance """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'id':
                    self.id = value
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ This method defines a custom string method """
        clsName = self.__class__.__name__
        return f"[{clsName}] ({self.id}) {self.__dict__}"

    def save(self):
        """ This method updates the "updates_at" with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing
            all keys/values of __dict__ of the instance
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__

        if 'created_at' in result_dict \
                and isinstance(result_dict['created_at'], datetime):
            result_dict['created_at'] = result_dict['created_at'].isoformat()
        if 'updated_at' in result_dict \
                and isinstance(result_dict['updated_at'], datetime):
            result_dict['updated_at'] = result_dict['updated_at'].isoformat()

        return result_dict
