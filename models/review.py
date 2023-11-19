#!/usr/bin/python3

"""

Review Module

This module contains the Review class, which inherits from the BaseModel class.
It defines a Review object with 'place_id', 'user_id', and 'text' attributes to
represent a user's review of a place.

Classes:
    - Review: Inherits from BaseModel and represents a user's
    review of a place.

Attributes:
    - place_id (str): The ID of the place being reviewed.
    - user_id (str): The ID of the user who wrote the review.
    - text (str): The content of the review.

Usage:
    To use this module, create instances of the Review class to represent
    different reviews and set their 'place_id', 'user_id', and 'text'
    attributes accordingly.

"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                place_id - place ID
    """
    place_id = ""
    user_id = ""
    text = ""
