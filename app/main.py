import os
from flask import Flask
# from flask_cors import CORS


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World  !</p>"