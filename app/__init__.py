import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt 

db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()

def create_app(config_filename=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
  
    @app.route("/")
    def hello():
        return "Hello, World!"
    
    return app