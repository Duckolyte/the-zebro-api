from os import environ
try:
    import config_properties as properties
except ImportError:
    pass


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
    # SQLALCHEMY_DATABASE_URI = ''

    # The Fatality board host db.
    SQLALCHEMY_DATABASE_URI = properties.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = properties.SQLALCHEMY_TRACK_MODIFICATIONS


