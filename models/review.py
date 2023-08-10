#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""defines Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class holds review info"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
