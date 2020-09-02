from flask import Flask
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000

