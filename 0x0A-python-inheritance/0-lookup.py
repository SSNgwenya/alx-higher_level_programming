#!/usr/bin/python3
"""Describes an object attribute lookup function."""

def lookup(obj):
    """Returns a list of object's available attributes."""
    return (dir(obj))
