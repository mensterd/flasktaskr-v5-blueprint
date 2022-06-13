import os

# Grab the folder where this script lives
p = os.path.dirname(__file__)
basedir = os.path.abspath(p)

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'myprecious'
# DEBUG = True

# Define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# The database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
