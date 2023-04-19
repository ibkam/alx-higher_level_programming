#!/usr/bin/python3
"""
    inherits from BaseGeometry
"""

BaseGeomerty = __import__("7-base_geometry.py").BaseGeometry

class Rectangle(BaseGeometry):
    """
    instantiation of a rectangle
    """
    
    def __init__(self, width, height):
        self.integer_validator("width, width)
        self.integer_validator("height, height)
        
        self.__width = width
        self.__height = height
