#!/usr/bin/python3
''' user defination inherited from basemodel'''

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_nanme = ""
