#!/usr/bin/python3

""" Module that inherits from int """

class MyInt(int):
    """This class rebels and inverts the == and != operators """
    
    def __eq__(self, value):
        """overrides == with != """
        return self.real != value

    def __ne__(self, value):
        """override != with == """
        return self.real == value
