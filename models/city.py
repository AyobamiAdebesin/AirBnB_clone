#!/usr/bin/python3
"""Defines a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class that represents a city and inherits from BaseModel"""
    state_id = ""
    name = ""
