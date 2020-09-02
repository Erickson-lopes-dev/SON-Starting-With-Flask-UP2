from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.sqlite3'

db = SQLAlchemy(app)
