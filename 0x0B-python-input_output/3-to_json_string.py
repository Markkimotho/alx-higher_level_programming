#!/usr/bin/python3

""" Module returning JSON rep of a object"""
import json

def to_json_string(my_obj):
	"""This  function will return the JSON representaion 
		of an object(string)
	"""
	return json.dumps(my_obj)

