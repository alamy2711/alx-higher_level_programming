#!/usr/bin/python3

"""This code defines a function for reading and printing
the contents of a text file."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
