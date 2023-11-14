#!/usr/bin/python3
"""A Square Module Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str special method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    # Size Setter
    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size with validation"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method"""
        if args is None and len(args) != 0:
            attributesList = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if attributesList[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, attributesList[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)
