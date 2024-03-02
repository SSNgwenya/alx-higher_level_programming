#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if a <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != a:
        i = triangles[-1]
        j = [1]
        for x in range(len(i) - 1):
            j.append(i[x] + i[x + 1])
        j.append(1)
        triangles.append(j)
    return triangles
