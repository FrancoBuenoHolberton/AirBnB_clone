#!/usr/bin/python3
""" Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initialize Review class """
        super()._i_init__(**kwargs)