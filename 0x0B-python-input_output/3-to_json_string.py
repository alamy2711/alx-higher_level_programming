#!/usr/bin/python3

"""This code defines a function for converting a Python object
to a JSON string using the json module."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object as a string."""
    return json.dumps(my_obj)
