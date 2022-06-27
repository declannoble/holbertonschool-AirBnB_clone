#!/usr/bin/python3
"""
Contains FileStorage class
"""


import json


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
        """
        deserializes JSON file to __objects
        """
