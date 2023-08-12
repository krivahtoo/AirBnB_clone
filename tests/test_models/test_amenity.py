#!/usr/bin/python3
"""Unittest for Amenity model"""
import unittest
from datetime import datetime, timedelta

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test Amenity object"""

    def test_datetime1(self):
        am = Amenity()

        self.assertIs(type(am.created_at), datetime)

    def test_datetime2(self):
        am = Amenity()

        self.assertIs(type(am.updated_at), datetime)

    def test_datetime3(self):
        am = Amenity()

        self.assertLess(am.updated_at, datetime.now())

    def test_datetime4(self):
        am = Amenity()

        self.assertGreater(
            am.updated_at,
            (datetime.now() - timedelta(seconds=2))
        )
