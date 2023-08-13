#!/usr/bin/python3
"""Unittest for City model"""
import unittest
from datetime import datetime, timedelta

from models.city import City


class TestCity(unittest.TestCase):
    """test City object"""

    def test_datetime1(self):
        """test created_at if of datetime type"""
        city = City()

        self.assertIs(type(city.created_at), datetime)

    def test_datetime2(self):
        """test updated_at if of datetime type"""
        city = City()

        self.assertIs(type(city.updated_at), datetime)

    def test_datetime3(self):
        """test updated_at is less than datetime.now()"""
        city = City()

        self.assertLess(city.updated_at, datetime.now())

    def test_datetime4(self):
        """test updated_at time"""
        city = City()

        self.assertGreater(
            city.updated_at,
            (datetime.now() - timedelta(seconds=2))
        )
