#!/usr/bin/python3
"""Defines a locked class to restrict attribute creation."""


class LockedClass:
    """
    This class prevents the user from creating new attributes
    except for the 'first_name' attribute.

    Attributes:
        __slots__ (list of str): A list of allowed attribute names.
    """

    __slots__ = ["first_name"]
