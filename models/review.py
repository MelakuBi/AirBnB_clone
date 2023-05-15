#!/usr/bin/python3
''' Review Class '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' this is class defination for review
    with attributes :
    place_id
    user_id
    text '''

    place_id = ""
    user_id = ""
    text = ""
