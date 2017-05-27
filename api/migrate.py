from peewee import *
import config as cfg
from app.models.base import mysql_db

def create_tables():
    mysql_db.connect()
    mysql_db.create_tables([BaseModel, User, State, City, Place, PlaceBook, Amenity, PlaceAmenities])
