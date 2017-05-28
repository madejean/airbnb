from peewee import *
import config as cfg
from app.models.base import *
from app.models.user import User
from app.models.state import State
from app.models.city import City
from app.models.place import Place
from app.models.place_book import PlaceBook
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenities


mysql_db = MySQLDatabase(database=cfg.DATABASE['database'], host=cfg.DATABASE['host'], port=cfg.DATABASE['port'], user=cfg.DATABASE['user'], password=cfg.DATABASE['password'], charset=cfg.DATABASE['charset'])

def create_tables():
    mysql_db.connect()
    mysql_db.create_tables([BaseModel, User, State, City, Place, PlaceBook, Amenity, PlaceAmenities])
