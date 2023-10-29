#!/usr/bin/python3
"""
This is the module for the Square class.
"""


class Square:
    """
    This is the Square class.
    """

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

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square
        """

        return self.__size**2

    def size(self):
        """
        Returns the size of the square.

        Returns:
            int: The size of the square
        """

        return self.__size

    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value
