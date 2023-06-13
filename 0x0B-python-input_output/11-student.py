#!/usr/bin/python3
""" Defines a Student class"""


class Student:
    """ Student class"""

    def __init__(self, first_name, last_name, age):
        """ Constructor of the Student class

        Attrs:
            first_name (str): first name of Student
            last_name (str): last name of Student
            age (int): age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Prepers the instance for JSON serialization"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
