from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)

modus = Modus(app)
modus.init_app(app)

app.config['DEBUG'] = True
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.sqlite3'

db = SQLAlchemy(app)
