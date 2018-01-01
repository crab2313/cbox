import os

class Configuration:
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/cbox.db' % APPLICATION_DIR
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'test secret key, do not use it in production'