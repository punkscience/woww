# config.py

# Enable Flask's debugging features. Should be False in production
DEBUG = True
SECRET_KEY = 'Secret key goes here'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = True