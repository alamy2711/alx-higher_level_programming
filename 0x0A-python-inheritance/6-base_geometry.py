#!/usr/bin/python3

"""This code defines a base geometry class called BaseGeometry
with an unimplemented area method."""


class BaseGeometry:
    """Represents basic geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
