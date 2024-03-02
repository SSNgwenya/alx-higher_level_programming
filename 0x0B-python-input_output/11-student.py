#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name: First name of the student.
            last_name: Last name of the student.
            age: Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs: Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student.

        Args:
            json: Value/Key pairs to replace attributes with.
        """
        for x, i in json.items():
            setattr(self, x, i)
