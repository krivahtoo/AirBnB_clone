#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""defines Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class holds place info"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
