from os import environ


class Config:
    """Set Flask configuration vars from .env file."""


    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database

    # The ssqllite document db.
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///../model.db'

    # The local myssql db.
    # SQLALCHEMY_DATABASE_URI = 'mysql://zebro:ag12982846@192.168.176.1:3306/zebro'

    # The Fatality board host db.
    SQLALCHEMY_DATABASE_URI = 'mysql://zebro:ag12982846@192.168.0.107:3306/zebro'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
