import os

basedir = os.path.abspath(os.path.dirname(__file__))


PROJECT_NAME = 'fynd_assignment'
DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:wms_user@localhost:5432/imdb"
SQLALCHEMY_TRACK_MODIFICATIONS = False
