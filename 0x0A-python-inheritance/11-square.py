#!/usr/bin/python3

""" A module defining a Rectangle subclass Square"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):

	""" A class representing a square 
	that has inherited a Rectangle class
	"""
	
	def __init__(self, size):
	"""initialized a new square"""

		super().__init__(size, size)
		self.__size = size

	def __str__(self):
	"""
		returns the representation of the instance/object
	"""
		return "[Square] {:d}/{:d}".format(self.__size, self.__size)
