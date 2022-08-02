#!/usr/bin/env python3
"""A File storage class"""


class FileStorage:
    """
    A class representing a File Storage System

    """
    __file_path = 'file.json'
    __objects = None

    def all(self):
        return (self.__objects)
    
    @new.setter
    def new(self, obj):
        self.__objects[

