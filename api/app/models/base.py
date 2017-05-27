from peewee import *
import config as cfg
from datetime import datetime

mysql_db = MySQLDatabase(database=cfg.DATABASE['database'], host=cfg.DATABASE['host'], port=cfg.DATABASE['port'], user=cfg.DATABASE['user'], password=cfg.DATABASE['password'], charset=cfg.DATABASE['charset'])
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
