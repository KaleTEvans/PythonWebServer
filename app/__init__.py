# app/__init__.py
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db

from dotenv import load_dotenv
load_dotenv()

from .config import Config

def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config)

    connection_string = os.environ.get('AZURE_SQL_CONNECTION_STRING')

    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from .routes import home_page, unix_values, underlying_candles, option_candles
        app.register_blueprint(home_page)
        app.register_blueprint(unix_values)
        app.register_blueprint(underlying_candles)
        app.register_blueprint(option_candles)

    return app