import os
from datetime import timedelta
from flask_session import Session

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    
    SESSION_TYPE = 'filesystem'  # Store sessions in the file system, could also be 'redis' or 'memcached'
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # Keep the session alive for 7 days
    SESSION_COOKIE_HTTPONLY = True  # Make the cookie HTTP-only for security
    SESSION_COOKIE_SAMESITE = 'Lax'  # Helps prevent CSRF attacks
    SESSION_COOKIE_SECURE = False
    # Construct absolute path for the SQLite database
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "..", "instance", "rpg_nexus.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(dev=Config)
