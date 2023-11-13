#!/usr/bin/python3
"""Base class"""


class Base:
    """This class represents a base class with a shared ID counter."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
