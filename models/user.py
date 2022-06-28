#!/usr/bin/python3
""" Module User """
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a subclass of BaseModel """
    id = ""
    password = ""
    first_name = ""
    last_name = ""
