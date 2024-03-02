#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if object is an inherited instance of a class.

    Args:
        obj: Object to check.
        a_class: Class to match type of obj to.
    Returns:
        True If obj is an inherited instance of a_class
        else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
