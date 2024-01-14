#!/usr/bin/python3
# this is our storage handling module

"""This is our storage handling module"""
import json
import os


class FileStorage():
    """Handles json conversion"""
    __path = 'storage_file.json'
    __objects = {}

    def all(self):
        """Returns objects"""
        return self.__objects

    def new(self, obj):
        """adds new object in the dictionary"""
        self.__objects[str(type(obj).__name__) + '.' + obj.id] = obj.__dict__

    def save(self):
        """serializes our objects dict to a json str"""
        with open(self.__path, 'w', encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Reloads objects from json file"""
        if os.path.isfile(self.__path):
            with open(self.__path, 'r') as f:
                self.__objects = json.load(f)
                return self.__objects
