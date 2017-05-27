from peewee import *
from base import BaseModel

class City(BaseModel):
    name = CharField(max_length=128, null=False)
    state = ForeignKeyField(State, related_name = "cities", on_delete='CASCADE')
