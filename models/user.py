#!/usr/bin/python3
''' user defination inherited from basemodel'''

from base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_nanme = ""

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
