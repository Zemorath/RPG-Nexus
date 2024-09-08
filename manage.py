# manage.py

from backend import create_app, db
from flask_migrate import Migrate
import os

app = create_app()  # Create your Flask app from backend/app.py
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()
