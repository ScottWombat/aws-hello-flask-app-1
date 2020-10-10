import os
from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
  
    @app.route("/")
    def hello():
        return "Hello, World!"
    
    return app