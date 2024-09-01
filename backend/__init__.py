
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from .config import Config
from flask_cors import CORS



db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    
    app = Flask(
        __name__,
        static_url_path='',
        static_folder='../client/build',
        template_folder='../client/build'
    )

    CORS(app)
    app.config.from_object(config_class)

    
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import and register blueprints
    from backend.routes.campaign_routes import campaign_bp
    app.register_blueprint(campaign_bp)

    from backend.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    from backend.routes.character_routes import character_bp
    app.register_blueprint(character_bp)

    from backend.routes.class_routes import class_bp
    app.register_blueprint(class_bp)

    from backend.routes.item_routes import item_bp
    app.register_blueprint(item_bp)

    from backend.routes.monster_routes import monster_bp
    app.register_blueprint(monster_bp)

    from backend.routes.note_routes import note_bp
    app.register_blueprint(note_bp)

    from backend.routes.npc_routes import npc_bp
    app.register_blueprint(npc_bp)

    from backend.routes.race_routes import race_bp
    app.register_blueprint(race_bp)

    from backend.routes.rpgsystem_routes import rpgsystem_bp
    app.register_blueprint(rpgsystem_bp)

    from backend.routes.skill_routes import skill_bp
    app.register_blueprint(skill_bp)

    from backend.routes.utility_routes import utility_bp
    app.register_blueprint(utility_bp)

    return app
