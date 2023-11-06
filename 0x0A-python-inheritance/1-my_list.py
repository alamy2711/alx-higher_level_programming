#!/usr/bin/python3

"""This code defines a custom list class called MyList,
which inherits from the built-in list class.
It includes a method for printing the list in sorted order."""


class MyList(list):
    """Provides sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
