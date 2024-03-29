#!/usr/bin/python3
"""The Unit test of class review"""

import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Methods and instances test"""

    r = Review()

    def test_class_exists(self):
        """Class existance test"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.r)), res)

    def test_user_inheritance(self):
        """Inheritance test"""
        self.assertIsInstance(self.r, Review)

    def testHasAttributes(self):
        """attributes existance check"""
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        self.assertTrue(hasattr(self.r, 'id'))
        self.assertTrue(hasattr(self.r, 'created_at'))
        self.assertTrue(hasattr(self.r, 'updated_at'))

    def test_types(self):
        """Attributes type verification"""
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.user_id, str)
        self.assertIsInstance(self.r.text, str)
        self.assertIsInstance(self.r.id, str)
        self.assertIsInstance(self.r.created_at, datetime.datetime)
        self.assertIsInstance(self.r.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
