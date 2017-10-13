#dev
import os
_basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
UPLOAD_FOLDER = 'uploads/'
SECRET_KEY = 'dummy'
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}
