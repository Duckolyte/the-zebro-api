from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from application.utils.setup_db import setup_db

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        # Imports
        from application.routes import errors, missions

        # Reset tables.
        db.drop_all()
        db.create_all()

        # Seed random data into tables.
        # seeder = FlaskSeeder()
        # seeder.init_app(app, db)

        return app
