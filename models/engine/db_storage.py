#!/usr/bin/python3

""" This module define a class to mange the database storage for hbnb clone"""

import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ This is a class Database storage using mysql db and sqlalchemy module"""
    
    __session = None
    __engine = None
    __objects = {}
    
    classList = [User, State, City, Place, Amenity, Review]
    
    def __init__(self):
        """ This is a method that initialze the engine """
        
        dialect = "mysql"
        drived = "mysqldb"
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        user = os.getenv("HBNB_MYSQL_USER", default="hbnb_dev")
        password = os.getenv("HBNB_MYSQL_PWD", default="hbnb_dev_pwd")
        database = os.getenv("HBNB_MYSQL_DB", default="hbnb_dev_db")
        is_test = os.getenv("HBNB_ENV")
        
        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'.format(
            dialect,
            drived,
            user,
            password,
            host,
            database),
            pool_pre_ping=True
        )
        
        if is_test == "test":
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """ This is a session that quaries the current db session """
        
        self.__objects = {}
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            qury = self.__session.query(cls)
            for obj in qury:
                key = '{}.{}'.format(
                    obj.__class__.__name__,
                    obj.id)
                self.__objects[key] = obj
        else:
            for cla in self.classList:
                qury = self.__session.query(cla)
                for obj in qury:
                    key = "{}.{}".format(
                        obj.__class__.__name__,
                        obj.id)
                    
        return self.__objects
    
    def new(self, obj):
        """This method add an object to the current db session"""
        
        self.__session.add(obj)
        
    def delete(self, obj=None):
        """ This is a method that delete from the current db session """
        
        if obj is not None:
            self.__session.delete(obj)
            
    def save(self):
        """ This is a method that save(commit) the changes"""
        
        self.__session.commit()
        
    def reload(self):
        """This is a method that reload the session """
        
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
        
    def close(self):
        """ This is a method that close the current session"""
        
        self.__session.close()