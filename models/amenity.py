#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""defines Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class holds amenity info"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
