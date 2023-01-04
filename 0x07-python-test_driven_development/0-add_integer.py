#!/usr/bin/python3

"""
A module with a function that adds two functions

"""

def add_integer(a, b=98):
	""" A function that adds two integers and/or floats
	
	Args:
		a: first number
		b: second number
	
	Returns:
		The sum of the two integers and/or floats passed
	
	Raises:
		TypeError: If a or b are not ints and/or floats
	"""

	if not isinstance(a, int) and not isinstance(a, float):
		raise TypeError("a must be an integer")
	if not isinstance(b, int) and not isinstance(b, float):
		raise TypeError("b must be an integer")
	
	a = int(a)
	b = int(b)

	return (a + b)

