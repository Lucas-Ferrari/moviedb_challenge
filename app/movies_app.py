import os

from flask import Flask

from app.infrastructure.extensions import cache, db
from app.config import Config

#Import blueprints
from app.entrypoints.api.entrypoints import movies_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

    cache.init_app(app)

    app.register_blueprint(movies_bp)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
