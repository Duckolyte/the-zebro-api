from os import environ


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///../model.db'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:ag12982846@192.168.176.1:3306/zebro'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
