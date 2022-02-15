from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .config import Config

load_dotenv()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, resources={r'/api/start_survey': {"origins": "*"}})
    return app
