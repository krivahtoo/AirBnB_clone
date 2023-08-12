#!/usr/bin/python3
"""Unittest for User model"""
from datetime import datetime
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test User"""

    def test_str(self):
        """test __str__ method"""
        obj = {
            'id': 'd0ef8146-4664-4de5-8e89-096d667b728e',
            'created_at': '2017-09-28T21:11:14.333852',
            'updated_at': '2017-09-28T21:11:14.963058',
            'email': 'airbnb2@mail.com',
            'first_name': 'John',
            'password': 'root',
        }
        user = User(**obj)

        self.assertEqual(
            str(user),
            '[User] ({}) {}'.format(user.id, user.__dict__)
        )

    def test_to_dict(self):
        """test to_dict method"""
        obj = {
            '__class__': 'User',
            'id': 'd0ef8146-4663-4de5-8e89-096d667b728e',
            'created_at': '2017-09-28T21:11:14.333852',
            'updated_at': '2017-09-28T21:11:14.963058',
            'email': 'airbnb2@mail.com',
            'first_name': 'John',
            'password': 'root',
        }
        user = User(**obj)

        self.assertEqual(
            obj,
            user.to_dict()
        )

    def test_created_at(self):
        """test created_at attribute"""
        obj = {
            '__class__': 'User',
            'id': 'd0ef8146-4663-4de5-8e89-096d667b728e',
            'created_at': '2017-09-28T21:11:14.333852',
            'updated_at': '2017-09-28T21:11:14.963058',
            'email': 'airbnb2@mail.com',
            'first_name': 'John',
            'password': 'root',
        }
        user = User(**obj)

        self.assertEqual(
            datetime(2017, 9, 28, 21, 11, 14, 333852),
            user.created_at
        )

    def test_updated_at(self):
        """test updated_at attribute"""
        obj = {
            '__class__': 'User',
            'id': 'd0ef8146-4663-4de5-8e89-096d667b728e',
            'created_at': '2017-09-28T21:11:14.333852',
            'updated_at': '2017-09-28T21:11:14.963058',
            'email': 'airbnb2@mail.com',
            'first_name': 'John',
            'password': 'root',
        }
        user = User(**obj)

        self.assertEqual(
            datetime(2017, 9, 28, 21, 11, 14, 963058),
            user.updated_at
        )
