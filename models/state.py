#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.city import City
        
        __tablename__ == "states"
        
        name = Column(
            String(128),
            nullable=False)
        
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete")
    else:
        name = ""
        
        @property
        def cities(self):
            """ This is a method that return all cities with state
            """
            from models import storage
            
            listCities = []
            for key, obj in storage.all().items():
                if "City" in key:
                    if obj.state_id == self.id:
                        listCities.append(obj)

            return listCities