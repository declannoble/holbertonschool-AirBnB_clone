#!/usr/bin/python3
"""
Contains FileStorage class
"""


import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes them back to instances
    """
    # path to the JSON file
    __file_path = "file.json"
    # dictionary to store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file path
        """
        jsonObject = {}
        for key in self.__objects:
            jsonObject[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(jsonObject, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
