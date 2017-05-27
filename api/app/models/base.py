from peewee import *
import config as cfg
from datetime import datetime

mysql_db = MySQLDatabase(cfg.DATABASE['database'], cfg.DATABASE['host'], cfg.DATABASE['port'], cfg.DATABASE['user'], cfg.DATABASE['password'])
datetime = "{:%Y/%m/%d %H:%M:%S}".format(datetime.now())

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    created_at = DateTimeField(default=datetime)
    updated_at = DateTimeField(default=datetime)
    def save(self, *args, **kwargs):
        self.updated_at = datetime
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = mysql_db
