#!/usr/bin/python3

""" Module that writes an object to text file"""

import json

def save_to_json_file(my_obj, filename):

	"""The function writes an object to a text file using JSON format"""
	with open(filename, 'w') as f:
		json.dump(my_obj, f)
