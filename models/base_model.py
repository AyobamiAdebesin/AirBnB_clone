#!/usr/bin/env python3
""" A base model for all objects of the project"""
import uuid
import cmd
import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods for
    other classes
    """

    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at


