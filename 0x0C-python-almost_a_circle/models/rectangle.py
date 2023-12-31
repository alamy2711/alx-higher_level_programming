#!/usr/bin/python3
"""A rectangle Module Class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # WIDTH Getter and Setter
    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # HEIGHT Getter and Setter
    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # X Getter and Setter
    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x with validation"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Y Getter and Setter
    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y with validation"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Area Method
    def area(self):
        """Calculate and return area"""
        return self.__width * self.__height

    # Display Method
    def display(self):
        """Display the rectangle"""
        for k in range(self.__y):
            print()

        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    # __str__ Method
    def __str__(self):
        """str Special method"""
        strRectangle = "[Rectangle] "
        strId = "({}) ".format(self.id)
        strXY = "{}/{} - ".format(self.x, self.y)
        strWidthHeight = "{}/{}".format(self.width, self.height)

        return strRectangle + strId + strXY + strWidthHeight

    # Update Method
    def update(self, *args, **kwargs):
        """Update method"""
        if args is not None and len(args) is not 0:
            attributesList = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributesList[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dectionary method"""
        attributesList = ["id", "width", "height", "x", "y"]
        dictionary = {}

        for key in attributesList:
            dictionary[key] = getattr(self, key)

        return dictionary
