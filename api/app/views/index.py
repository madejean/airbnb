from app import app
from flask_json import FlaskJSON, JsonError, json_response, as_json
from datetime import datetime
from app.models.base import mysql_db

@app.route('/', methods=['GET'])
def index():
    utc = datetime.utcnow()
    serverTime = datetime.now()
    return json_response(status="OK", utc_time=utc, time=serverTime)

@app.before_request
def before_request():
    mysql_db.connect()

@app.after_request
def after_request(response):
    mysql_db.close()
    return response

@app.errorhandler(404)
def not_found():
    return json_response(status="404", message="not found")
