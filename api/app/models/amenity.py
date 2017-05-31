from peewee import *
from base import BaseModel

class Amenity(BaseModel):
    name = CharField(max_length=128, null=False)

    def to_hash(self):
        data = {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name
        }
        return data
