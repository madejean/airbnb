from peewee import *
from base import BaseModel
from state import State

class City(BaseModel):
    name = CharField(max_length=128, null=False)
    state = ForeignKeyField(State, related_name = "cities", on_delete='CASCADE')
