print('init file')
from flask import Flask
from confiig_pkg.config import Config
from flask_sqlalchemy import SQLAlchemy

#intializing flask app with flask instance
app = Flask(__name__)

#loading the configurations
app.config.from_object(Config)

#connection is done with the database
db = SQLAlchemy(app)





