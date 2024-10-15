import os

from flask import Flask
from app.infrastructure import database
from app.config import Config

#Import blueprints
from app.entrypoints.api.entrypoints import movies_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    database.init_app(app)

    app.register_blueprint(movies_bp)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
