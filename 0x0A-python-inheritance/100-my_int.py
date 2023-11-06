#!/usr/bin/python3

"""This code defines a class MyInt that inherits from int
and redefines the == and != operators."""


class MyInt(int):
    """Inverts the behavior of == and != operators."""

    def __eq__(self, value):
        """Override the == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator with == behavior."""
        return self.real == value
