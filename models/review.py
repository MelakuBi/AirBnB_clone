#!/usr/bin/python3


from models.base_model import BaseModel


''' this is class defination for review
with attributes : 
    place_id
    user_id
    text '''

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
