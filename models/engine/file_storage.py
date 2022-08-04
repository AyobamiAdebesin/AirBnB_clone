#!/usr/bin/python3
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
        """
        Add a new element; obj, to the self.__objects dictionary
        obj : obj is a class instance
        """
        obj_id = obj.__class__.__name__ + "." + obj.id
        self.__objects[obj_id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file path: __file_path
        """
        # Create a dict to store as value, the dictionary representation
        # of the class instance (obj).
        json_object = {}
        for key, obj in self.__objects.items():
            json_object[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(json_object, f)

        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                json_object = json.load(f)
            # Loop through the json_object keys to extract the "__class__"
            # attribute and use the value to create instances
            for key, value, in json_object.items():
                self.new(BaseModel(**value))
                # class_name = json_object[key]['__class__']
                # object_dict = json_object[key]
                # self.__objects[key] = self.new(BaseModel(**object_dict))
        except FileNotFoundError:
            pass
