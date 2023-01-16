#!/usr/bin/python3
"""module that defines a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits the functionalities of
    Rectangle and Base Classes respectively"""
    def __init__(self, size, x=0, y=0, id=None):
        """Method/ Function that initializes an instance
        of the class/ object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method/ Function that returns the string representation
        of the instance of the class/ object
        """
        return "[{}] ({}) {}/{} - {}".format(
                                            type(self).__name__,
                                            self.id,
                                            self.x,
                                            self.y,
                                            self.width)

    @property
    def size(self):
        """Getter function that creates and returns
        a private attribute width
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter function that sets the values of the attributes
        width and height
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns key/value argument to attributes
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
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns the dictionary representation of a square object"""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.width,
                'y': self.y
        }
