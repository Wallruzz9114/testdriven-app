import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from project.api.users import users_blueprint

# Instanciate database
db = SQLAlchemy()


def create_app(script_info=None):
    # Instanciate the app
    app = Flask(__name__)
    # Set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # Set up extensions
    db.init_app(app)
    # Register blueprints
    app.register_blueprint(users_blueprint)
    # Shell contextfor flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app
