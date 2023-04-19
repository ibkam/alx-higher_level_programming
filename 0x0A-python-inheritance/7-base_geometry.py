#!/usr/bin/python3
"""
A class BaseGeometry
"""


class BaseGeometry:
        """ a public instance method area"""
        def area(self):
            raise Exception("area() is not implemented")
    
        """ a public instance method integer_validator"""
        def integer_validator(self, name, value):
        """ integer validator"""
        
        Args:
            name (sring): a string
            value (int): the intager values
              
      """
        if type(value) != int:
        raise TypeError( "{} must be an integer".format(name))
        
        if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
