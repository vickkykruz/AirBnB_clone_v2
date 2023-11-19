#!/usr/bin/python3

"""

User Module

This module contains the User class, which inherits from the
BaseModel class. It defines a User object with 'email', 'password',
'first_name', and 'last_name' attributes to represent user information.

Classes:
    - User: Inherits from BaseModel and represents a user.

Attributes:
    - email (str): The email address of the user.
    - password (str): The password of the user.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.

Usage:
    To use this module, create instances of the User class to represent
    different users and set their 'email', 'password', 'first_name', and
    'last_name' attributes accordingly.

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class

    This class represents a user and inherits from the BaseModel class.
    It stores user information, including the user's 'email', 'password',
    'first_name', and 'last_name'.

    Attributes:
    - email (str): The email address of the user.
    - password (str): The password associated with the user's account.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.

    Usage:
    Create instances of the User class to represent individual users and set
    their attributes to store user-specific information.

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
