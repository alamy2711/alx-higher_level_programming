#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle

"""Test Module"""


class TestRectangle(unittest.TestCase):
    """Test the Rectangle class methods"""

    def setUp(self):
        """Set up method for test cases"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test id assignment"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_raises(self):
        """Test exception handling"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test display method"""
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 2)
        res1 = "####\n####\n####\n####\n####\n####\n"
        res2 = "##\n##\n"

        with patch("sys.stdout", new=StringIO()) as strOut:
            r1.display()
            self.assertEqual(res1, strOut.getvalue())

        with patch("sys.stdout", new=StringIO()) as strOut:
            r2.display()
            self.assertEqual(res2, strOut.getvalue())
