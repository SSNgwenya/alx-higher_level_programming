#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of a given class.

    Args:
        obj: Object to check.
        a_class: Class to match type of obj to.
    Returns:
        True if obj is exactly an instance of a_class
        else - False.
    """
    if type(obj) == a_class:
        return True
    return False
