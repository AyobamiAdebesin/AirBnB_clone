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
        return (FileStorage.__objects)

    def new(self, obj):
        """
        Add a new element; obj, to the self.__objects dictionary
        obj : obj is a class instance
        """
        obj_id = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file path: __file_path
        """
        # Create a dict to store as value, the dictionary representation
        # of the class instance (obj).
        json_object = {}
        for key, obj in FileStorage.__objects.items():
            json_object[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(json_object, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.city import City
        class_dict = {
                "BaseModel": BaseModel, "User": User,
                "Amenity": Amenity, "State": State, "Review": Review,
                "Place": Place, "City": City}
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                json_object = json.load(f)
            # Loop through the json_object keys to extract the "__class__"
            # attribute and use the value to create instances
            for key, value, in json_object.items():
                class_name = value['__class__']
                if class_name in class_dict:
                    model_name = class_dict.get(class_name)
                    self.new(model_name(**value))
                # class_name = json_object[key]['__class__']
                # object_dict = json_object[key]
                # self.__objects[key] = self.new(BaseModel(**object_dict))
        except FileNotFoundError:
            pass
