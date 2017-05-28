import os

AIRBNB_ENV = os.environ.get('AIRBNB_ENV')


if AIRBNB_ENV == 'production':
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 3000
    DATABASE = {
        "host": '158.69.77.113',
        "user": 'airbnb_user_prod',
        "database": 'airbnb_prod',
        "port": 3306,
        "charset": 'utf8',
        "password": os.environ.get('AIRBNB_DATABASE_PWD_PROD'),
    }

elif AIRBNB_ENV == "development":
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE = {
        "host": '158.69.77.113',
        "user": 'airbnb_user_dev',
        "database": 'airbnb_dev',
        "port": 3306,
        "charset": "utf8",
        "password": os.environ.get('AIRBNB_DATABASE_PWD_DEV'),
    }
