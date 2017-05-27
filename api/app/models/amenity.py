from peewee import *
from base import BaseModel

class Amenity(BaseModel):
    name = CharField(max_length=128, null=False)
