from peewee import *
from base import BaseModel

class State(BaseModel):
    name = CharField(max_length=128, null=False)
