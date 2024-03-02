# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db

from dotenv import load_dotenv
load_dotenv()

from .config import Config

def create_app():
    app = Flask(__name__)
    print(Config.connect_str)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from .routes import unix_values
        app.register_blueprint(unix_values)

    return app