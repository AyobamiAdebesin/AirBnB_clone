#!/usr/bin/env python3
""" A base model for all objects of the project"""
import uuid
import cmd
from datetime import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods for
    other classes
    """

    def __init__(
            """Initializes the attributes"""
            self, id=str(uuid.uuid4()), created_at=datetime.now(),
            updated_at=datetime.now()):

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """A string representation of the Base Model"""
        return '[BaseModel] ({}) {}'.format(self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__
        of the instance
        """
        new_dict = self.__dict__
        new_dict['__class__'] = 'BaseModel'
        new_dict['created_at'] = self.created.isoformat()
