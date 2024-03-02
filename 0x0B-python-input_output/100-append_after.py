#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.

    Args:
        filename: Nname of the file.
        search_string: String to search for within the file.
        new_string: String to insert.
    """
    t = ""
    with open(filename) as b:
        for i in b:
            t += i
            if search_string in i:
                t += new_string
    with open(filename, "g") as g:
        g.write(t)
