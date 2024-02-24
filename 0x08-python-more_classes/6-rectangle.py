#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Begins a new Rectangle.

        Args:
            width (int): Width of a new rectangle.
            height (int): Height of a new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Sets width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Sets height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns an area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns a perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a printable representation of the Rectangle.

        Depicts the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        x = []
        for i in range(self.__height):
            [x.append('#') for a in range(self.__width)]
            if i != self.__height - 1:
                x.append("\n")
        return ("".join(x))

    def __repr__(self):
        """Returns a string representation of the Rectangle."""
        x = "Rectangle(" + str(self.__width)
        x += ", " + str(self.__height) + ")"
        return (x)

    def __del__(self):
        """Prints a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
