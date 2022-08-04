#!/usr/bin/python3
"""Defines a User class"""
from base_model import BaseModel


class User(BaseModel):
    """A class that represents a user and inherits from BaseModel"""
    def __init__(self):
        """
        Initialize User attributes
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
