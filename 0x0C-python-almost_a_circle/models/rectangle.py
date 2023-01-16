#!/usr/bin/python3
"""Module with Rectangle class that
adopts the base's functionality
"""

import json
from models.base import Base


class Rectangle(Base):
    """Rectangle class that defines a rectangular
    shape and inherits Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class
        super().__init__(attributes): inherits Base functionality
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """It is a string representaion of the the instance"""
        return "[{}] ({}) {}/{} - {}/{}".format(
                                                type(self).__name__,
                                                self.id, self.x,
                                                self.y,
                                                self.width,
                                                self.height)

    @property
    def width(self):
        """Getter function that privately defines the width attribute
        Return:
            self.__width or width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter function that defines the value of width attribute
        Args:
            value: value to be set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function that privately defines the width attribute
        Return:
            self.__height or height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter function that defines the value of height attribute
        Args:
            value: value to be set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function that privately defines the x attribute
        Return:
            self.__x or x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter function that defines the value of x attribute
        Args:
            value: value to be set
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function that privately defines the width attribute
        Return:
            self.__y or y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter function that defines the value of y attribute
        Args:
            value: value to be set
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """In stdout it represents width, height, a and y
        as a symbol #
        """
        rectangle = ""
        hash_symbol = "#"
        print("\n" * self.y, end="")

        for i in range(self.__height):
            rectangle += (" " * self.x) + (hash_symbol * self.__width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """assigns key/value argument to attributes
           kwargs is skipped if args is not empty
        Args:
            *args -  variable number of no-keyword args
            **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Return a dictionary representation of a rectangle"""
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
        }
