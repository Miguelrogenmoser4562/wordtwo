from flask import Flask
from .routes import app

def create_app():
    not_app = Flask(__name__, template_folder='/wordtwo/templates')
    not_app.register_blueprint(app)
    return not_app