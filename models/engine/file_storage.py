#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is a file storgae class
    Author: Peter Ekwere

"""
import sys
import json
import os
from models.base_model import BaseModel
sys.path.append("..")

if __name__ == "__main__":
    """ do not run directly """


class FileStorage:
    """ This is the FileStorage class"""

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ Returns the dictionary of the objects """
        return self.__objects

    def new(self, obj):
        """ This function sets the object in the dictionary with its id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes objects to json file """
        new_dict = {}

        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(self.__file_path, mode='a', encoding="utf-8") as a_file:
            json.dump(new_dict, a_file)
    
    def reload(self):
        """ Deserializes objects to json file """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding="utf-8") as a_file:
                serialized_dict = json.load(a_file)
                for 
