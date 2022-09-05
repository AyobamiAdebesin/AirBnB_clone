#!/usr/bin/python3
""" A base model for all objects of the project"""
import uuid
import cmd
from datetime import datetime
from models import storage


class BaseModel:
    """
    A class that defines all common attributes/methods for
    other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialiazes the Base model atributes"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """A string representation of the Base Model"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__
        of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return (new_dict)
