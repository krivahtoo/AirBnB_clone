#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""defines User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class holds users data"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
