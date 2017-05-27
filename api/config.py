import os

name = os.environ.get('AIRBNB_ENV');

if name == 'development':
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE = {
        'host': '158.69.77.113',
        'user': 'airbnb_user_dev',
        'database': 'airbnb_dev',
        'port': 3306,
        'charset': 'utf8',
        'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV')
    }

elif name == 'production':
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 3000
    DATABASE = {
        'host': '158.69.77.113',
        'user': 'airbnb_prod',
        'database': 'airbnb_prod',
        'port': 3306,
        'charset': 'utf8',
        'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD')
     }
