# from flask import Flask, request, jsonify
# from flask_restful import Api, Resource
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from flask_migrate import Migrate
# from .config import Config

# def create_app():
#     app = Flask(__name__)
#     # applies CORS headers to all routes, enabling resources to be accessed
#     CORS(app)
#     app.config.from_object(Config)

#     with app.app_context():
#         from .routes import unix_values

#         app.register_blueprint(unix_values)

#         return app