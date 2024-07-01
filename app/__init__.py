from flask import Flask
from app.api import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(api_blueprint)
    return app