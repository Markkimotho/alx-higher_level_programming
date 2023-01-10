#!/usr/bin/python

"""Module that defines a class called Student"""
import json

class Student:
	"""a new class called Student"""

	def __init__(self, first_name, last_name, age):
		"""Initializes new Student"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	
	def to_json(self);
		"""Returns dict representation of Student"""
		return self.__dict__
