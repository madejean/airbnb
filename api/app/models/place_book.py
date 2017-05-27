from peewee import *
from base import BaseModel

class PlaceBook(BaseModel):
    place = ForeignKeyField(Place)
    user = ForeignKeyField(User)
    is_validated = BooleanField(default=False)
    date_start = DateTimeField(null=False)
    number_nights = IntegerField(default=1)
