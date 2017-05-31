from app import app
from flask import jsonify
from datetime import datetime
from app.models.base import mysql_db

@app.route('/', methods=['GET'])
def index():
    utc = datetime.utcnow()
    serverTime = datetime.now()
    message = {
        'status': 'OK',
        'utc_time': utc,
        'time': serverTime
    }
    return jsonify(message)

@app.before_request
def before_request():
    mysql_db.connect()

@app.after_request
def after_request(response):
    mysql_db.close()
    return response

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'code': 404,
            'message': 'Not Found: ',
    }
    res = jsonify(message)
    res.status_code = 404

    return res
