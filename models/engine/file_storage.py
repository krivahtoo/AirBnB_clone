#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is a file storgae class
    Author: Peter Ekwere

"""
import sys
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

