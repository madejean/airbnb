from peewee import *
from base import BaseModel
from state import State

class City(BaseModel):
    name = CharField(max_length=128, null=False)
    state = ForeignKeyField(State, related_name = "cities", on_delete='CASCADE')

    def to_hash(self):
        data = {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'state_id': self.state.id
        }
        return data
