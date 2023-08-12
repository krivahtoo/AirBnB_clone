#!/usr/bin/python3
"""Unittest for Review model"""
from datetime import datetime, timedelta
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """test Review object"""

    def test_datetime1(self):
        """test created_at if of datetime type"""
        review = Review()

        self.assertIs(type(review.created_at), datetime)

    def test_datetime2(self):
        """test updated_at if of datetime type"""
        review = Review()

        self.assertIs(type(review.updated_at), datetime)

    def test_datetime3(self):
        """test updated_at is less than datetime.now()"""
        review = Review()

        self.assertLess(review.updated_at, datetime.now())

    def test_datetime4(self):
        """test updated_at time"""
        review = Review()

        self.assertGreater(
            review.updated_at,
            (datetime.now() - timedelta(seconds=2))
        )
