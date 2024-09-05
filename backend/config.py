import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///rpg_nexus.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # Only enable this for development

config_by_name = dict(dev=Config)
