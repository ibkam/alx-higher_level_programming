#!/usr/bin/python3
"""module: class student"""

class Student():
	"""Rep a new class student"""
	def __init__(self, first_name, last_name, age):
		"""initialize a new student
		Args:
			@first_name: the first name of the student
			@last_name: the last name of the student
			@age: the age of the student
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		
	def to_json(self, attrs=None):
		"""get dictionary rep of the student
		If attrs is a list of strings,
		only attribute names contained in this list must be retrieved.
		Otherwise, all attributes must be retrieved.
		
		Args:
			@attrs(list): the attributes rep
			
		"""
		if (type(attrs) == list and
				all(type(ele) == str for ele in attrs)):
			return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
		return self.__dict__
