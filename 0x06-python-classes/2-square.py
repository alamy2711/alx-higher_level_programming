#!/usr/bin/python3
"""
This is the module for the Square class.
"""


class Square:
    def __init__(self, size=0):
        """
        Initializes the Square class.

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
