#!/usr/bin/python3
"""The Unittest of State classe"""

import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Methods and instances test"""

    s = State()

    def test_class_exists(self):
        """Class existance test"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), res)

    def test_user_inheritance(self):
        """Inheritance test"""
        self.assertIsInstance(self.s, State)

    def testHasAttributes(self):
        """Attributes existance check"""
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        """attributestype verification"""
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
