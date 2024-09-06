import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    
    # Construct absolute path for the SQLite database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, '../instance/rpg_nexus.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(dev=Config)
