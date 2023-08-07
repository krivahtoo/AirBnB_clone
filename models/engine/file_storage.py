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
    """ This is a file class """

    __file_path = ""
    __objects = {}

