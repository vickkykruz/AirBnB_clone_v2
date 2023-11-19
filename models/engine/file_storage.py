#!/usr/bin/python3

"""
FileStorage Module

This module contains the FileStorage class for serializing
instances to a JSON file and deserializing JSON files.

Attributes:
    - __file_path (str): Path to the JSON file for data storage.
    - __objects (dict): Dictionary to store objects by <class name>.id.

Classes:
    - FileStorage: Manages object serialization and deserialization.
    - all(self): Returns all stored objects.
    - new(self, obj): Adds a new object to storage.
    - save(self): Serializes objects to a JSON file.
    - reload(self): Deserializes JSON file back into objects.

Usage:
    To use this module, create a FileStorage instance
    and call its methods for object manipulation and persistence.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """ This class serializes instances to a JSON file and
        deserializes JSON file to instances

            __file_path: path to the JSON file
            __objects: store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        # print(FileStorage.__objects)

    def save(self):
        """ serializes __objects to the JSON file """

        cls_dict = FileStorage.__objects
        obj_dict = {obj: cls_dict[obj].to_dict() for obj in cls_dict.keys()}
        with open(FileStorage.__file_path, mode="w", encoding="utf8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        filename = FileStorage.__file_path

        if os.path.exists(filename):
            with open(filename, mode="r", encoding="utf8") as f:
                objdict = json.load(f)
                for key, value in objdict.items():
                    FileStorage.__objects[key] = \
                        eval(value["__class__"])(**value)
        else:
            pass
