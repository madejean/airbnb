from peewee import *
from base import BaseModel
import config as cfg
from place import Place
from amenity import Amenity

mysql_db = MySQLDatabase(database=cfg.DATABASE['database'], host=cfg.DATABASE['host'], port=cfg.DATABASE['port'], user=cfg.DATABASE['user'], password=cfg.DATABASE['password'], charset=cfg.DATABASE['charset'])

class PlaceAmenities(BaseModel):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    class Meta:
        database = mysql_db
