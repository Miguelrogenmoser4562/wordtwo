from flask import Flask
from .routes import app

def create_app():
    not_app = Flask(__name__)
    not_app.register_blueprint(app)
    return not_app