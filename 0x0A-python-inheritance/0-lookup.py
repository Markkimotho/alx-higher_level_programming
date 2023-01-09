#!/usr/bin/python3

""" A module with a function returning attributes and methods """

def lookup(obj):
	""" 
	This function returns the list of available attributes and methods of an object 
	"""
	return dir(obj)
