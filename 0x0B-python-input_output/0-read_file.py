#!/usr/bin/python3

"""module that reads a text file in unicode and prints it out"""

def read_file(filename=""):
	"""This func prints the contents of a UTF-8 file to stdout"""
	with open(filename, encoding="utf-8") as f:
		print(f.read(), end="")
