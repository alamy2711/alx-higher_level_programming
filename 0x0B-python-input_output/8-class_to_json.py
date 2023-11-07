#!/usr/bin/python3

"""This code defines a function for converting a Python class object
to a JSON dictionary."""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
