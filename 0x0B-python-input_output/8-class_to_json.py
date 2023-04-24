#!/usr/bin/python3
"""module: returns the dict description with data structure"""


def class_to_json(obj):
  """returns dictionary description
  Args:
      @obj: object passed
      
  Returns: the dict in data structure
  """
  return obj.__dict__
