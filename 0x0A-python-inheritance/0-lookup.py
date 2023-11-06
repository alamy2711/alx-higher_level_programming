#!/usr/bin/python3

"""This code defines a function for retrieving an object's attributes."""


def lookup(obj):
    """Returns a list of the attributes available in the object."""
    return dir(obj)
