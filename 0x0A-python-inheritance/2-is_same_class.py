#!/usr/bin/python3
"""
This module defines the function is_same_class,
which checks if an object is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a given class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
