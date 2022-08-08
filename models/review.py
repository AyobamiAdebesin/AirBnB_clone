#!/usr/bin/python3
"""Defines a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class that represents a review and inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
