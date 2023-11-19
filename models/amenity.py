#!/usr/bin/python3
"""
    Amenity Module

This module contains the Amenity class, which inherits
from the BaseModel class. It defines an Amenity object with a 'name'
attribute to store the name of the amenity.

Classes:
    - Amenity: Inherits from BaseModel and represents an amenity.

Attributes:
    - name (str): The name of the amenity.

Usage:
    To use this module, create instances of the Amenity class to represent
    different amenities and set their 'name' attribute accordingly.

"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                name - holds the name of the amenity
    """
    name = ""
