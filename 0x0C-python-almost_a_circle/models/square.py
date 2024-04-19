#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Starts a new Square.

        Args:
            size: Size of the new Square.
            x: "x" coordinate of the new Square.
            y: "y" coordinate of the new Square.
            id: Identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Sets the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square.

        Args:
            *args: New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs: New key pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for ar in args:
                if i == 0:
                    if ar is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = ar
                elif i == 1:
                    self.size = ar
                elif i == 2:
                    self.x = ar
                elif i == 3:
                    self.y = ar
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
