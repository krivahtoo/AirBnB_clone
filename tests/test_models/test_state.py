#!/usr/bin/python3
"""Unittest for State model"""
from datetime import datetime, timedelta
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """test State object"""

    def test_datetime1(self):
        """test created_at if of datetime type"""
        state = State()

        self.assertIs(type(state.created_at), datetime)

    def test_datetime2(self):
        """test updated_at if of datetime type"""
        state = State()

        self.assertIs(type(state.updated_at), datetime)

    def test_datetime3(self):
        """test updated_at is less than datetime.now()"""
        state = State()

        self.assertLess(state.updated_at, datetime.now())

    def test_datetime4(self):
        """test updated_at time"""
        state = State()

        self.assertGreater(
            state.updated_at,
            (datetime.now() - timedelta(seconds=2))
        )
