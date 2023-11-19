#!/usr/bin/python3
"""
    City Module

This module contains the City class, which inherits from the BaseModel class.
It defines a City object with 'name' and 'state_id' attributes to store the
name of the city and the associated state's ID.

Classes:
    - City: Inherits from BaseModel and represents a city.

Attributes:
    - state_id (str): The ID of the state to which the city belongs.
    - name (str): The name of the city.

Usage:
    To use this module, create instances of the City
    class to represent different cities and set their
    'state_id' and 'name' attributes accordingly.

"""


from models.base_model import BaseModel


class City(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                name - holds the name of the city
                state_id - state id
    """
    state_id = ""
    name = ""
