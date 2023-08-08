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


class FileStorage(BaseModel):
    """ This is the FileStorage class"""

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ Returns the dictionary of the objects """
        return self.__objects

    def new(self, obj):
        """ This function sets the object in the dictionary with its id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        __objects[key] = obj

    def save(self):
        """ serializes objects to json file """
        new_list = []

        for key, obj in self.__objects:
            new_list.append({'key': key, 'object': obj.to_dict()})
        json_string = json.dumps(new_list)

        with open(self.__file_path, mode='w', encoding="utf-8") as a_file:
            a_file.write(json_string)
    
    def reload(self):
        """ Deserializes objects to json file """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding="utf-8") as a_file:
                json_string = a_file.read()

            json_dict = json.loads(json_string)
            return json_dict
