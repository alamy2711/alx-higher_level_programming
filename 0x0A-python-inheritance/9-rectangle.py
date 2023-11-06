#!/usr/bin/python3

"""This code defines a class Rectangle that inherits from BaseGeometry,
a previously defined class."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry as a base class."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of a Rectangle
        for print() and str()."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
