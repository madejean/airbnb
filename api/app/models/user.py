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
