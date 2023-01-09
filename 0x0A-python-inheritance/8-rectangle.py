#!/usr/bin/python3

""" Inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
	""" a class that defines a rectangle based on the
		inherited BaseGeometry
	"""
	def __init__(self, width, height):
		"""initializes new Rectangle"""
		self.integer_validator("width", width)
		self.__width = width
		self.integer_validator("height", height)
		self.__height = height
