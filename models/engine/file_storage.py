#!/usr/bin/env python3
"""A File storage class"""
import json

class FileStorage:
    """
    A class representing a File Storage System

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return (self.__objects)
    
    def new(self, obj):
        pass

    def save(self):
        """
        Serializes __objects to the JSON file path: __file_path
        """
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
