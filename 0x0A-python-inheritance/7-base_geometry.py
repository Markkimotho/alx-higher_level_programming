#!/usr/bin/python3

class BaseGeometry:
	"""class that represents the base geometry"""

	def area(self):
		"""area method which isnt implemented"""
		raise Exception("area() is not implemented")
	def integer_validatot(self, name, value):
		"""validates the integer passed to be an integer"""
		if type(value) != int:
			raise TypeError("{} must be an integer".format(name))
		if value <= 0:
			raise ValueError("{} must be greater than 0".format(name))
