#!/usr/bin/python3
"""Unittest for Place model"""
from datetime import datetime, timedelta
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """test Place object"""

    def test_datetime1(self):
        """test created_at if of datetime type"""
        pl = Place()

        self.assertIs(type(pl.created_at), datetime)

    def test_datetime2(self):
        """test updated_at if of datetime type"""
        pl = Place()

        self.assertIs(type(pl.updated_at), datetime)

    def test_datetime3(self):
        """test updated_at is less than datetime.now()"""
        pl = Place()

        self.assertLess(pl.updated_at, datetime.now())

    def test_datetime4(self):
        """test updated_at time"""
        pl = Place()

        self.assertGreater(
            pl.updated_at,
            (datetime.now() - timedelta(seconds=2))
        )
