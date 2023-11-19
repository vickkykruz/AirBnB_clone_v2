#!/usr/bin/python3

"""
State Module

This module contains the State class, which inherits from the
BaseModel class. It defines a State object with a 'name' attribute
to represent the name of a state.

Classes:
    - State: Inherits from BaseModel and represents a state.

Attributes:
    - name (str): The name of the state.

Usage:
    To use this module, create instances of the State class to represent
    different states and set their 'name' attribute accordingly.

"""


from models.base_model import BaseModel


class State(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                name - holds the name of the state
    """
    name = ""
