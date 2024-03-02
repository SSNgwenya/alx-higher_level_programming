#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance or inherited instance of a class.

    Args:
        obj: Object to check.
        a_class: Class to match type of obj to.
    Returns:
        True If obj is an instance or inherited instance a_class
        else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
