#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""defines State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class holds states data"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
