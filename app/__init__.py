# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db

from dotenv import load_dotenv
load_dotenv()

from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from .routes import unix_values, underlying_candles, option_candles
        app.register_blueprint(unix_values)
        app.register_blueprint(underlying_candles)
        app.register_blueprint(option_candles)

    return app