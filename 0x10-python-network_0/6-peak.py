#!/usr/bin/python3
"""
Module: 6-peak.py

Description:
This module defines a function `find_peak` to find a peak
in a list of unsorted integers.
"""


def find_peak_recursive(arr, start, end):
    """
    Recursively find a peak in a sublist of unsorted integers.
    """
    if start == end:
        return arr[start]

    middle = (start + end) // 2
    if arr[middle] > arr[middle + 1]:
        return find_peak_recursive(arr, start, middle)
    else:
        return find_peak_recursive(arr, middle + 1, end)


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers
    using a divide-and-conquer approach.
    """
    if not list_of_integers:
        # Empty list, no peak
        return None

    list_len = len(list_of_integers)

    if list_len == 1 or list_of_integers[0] >= list_of_integers[1]:
        # List with one element or first element is a peak
        return list_of_integers[0]

    if list_of_integers[list_len - 1] >= list_of_integers[list_len - 2]:
        # Last element is a peak
        return list_of_integers[list_len - 1]

    # Find peak in the middle
    return find_peak_recursive(list_of_integers, 0, list_len - 1)
