from peewee import *
from base import BaseModel
from hashlib import md5

class User(BaseModel):
    email = CharField(null=False, unique=True, max_length=128)
    password = CharField(null=False)
    first_name = CharField(null=False)
    last_name = CharField(null=False)
    is_admin = BooleanField(default=False)

    def set_password(self, clear_password):
        m = md5()
        m.update(clear_password)
        return m.hexdigest()

    def to_hash(self):
        data = {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin
        }
        return data
