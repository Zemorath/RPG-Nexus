from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config import Config
from flask_cors import CORS
from sqlalchemy import MetaData
import os

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=naming_convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(
        __name__,
        instance_path=os.path.join(os.path.abspath(os.curdir), 'instance')
    )
    
    # Enable CORS for external access
    CORS(app)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import and register blueprints
    from routes.campaign_routes import campaign_bp
    app.register_blueprint(campaign_bp)

    from routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    from routes.character_routes import character_bp
    app.register_blueprint(character_bp)

    from routes.class_routes import class_bp
    app.register_blueprint(class_bp)

    from routes.item_routes import item_bp
    app.register_blueprint(item_bp)

    from routes.monster_routes import monster_bp
    app.register_blueprint(monster_bp)

    from routes.note_routes import note_bp
    app.register_blueprint(note_bp)

    from routes.npc_routes import npc_bp
    app.register_blueprint(npc_bp)

    from routes.race_routes import race_bp
    app.register_blueprint(race_bp)

    from routes.rpgsystem_routes import rpgsystem_bp
    app.register_blueprint(rpgsystem_bp)

    from routes.skill_routes import skill_bp
    app.register_blueprint(skill_bp)

    from routes.utility_routes import utility_bp
    app.register_blueprint(utility_bp)

    return app
