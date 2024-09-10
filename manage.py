from flask import current_app
from flask.cli import with_appcontext
from flask_migrate import Migrate
from backend import create_app, db
from backend.models import User, Character, Race, Class, CharacterClass, Skill, CharacterSkill, HomebrewSkill, CharacterHomebrewSkill, Item, CharacterItem, HomebrewItem, CharacterHomebrewItem, RPGSystem, CharacterRPGSystem, Campaign, Note, Monster, HomebrewMonster, CampaignMonster, NPC, HomebrewNPC, CampaignNPC  # Add all your models here

app = create_app()
migrate = Migrate(app, db)

@app.cli.command("list-tables")
@with_appcontext
def list_tables():
    engine = db.get_engine()
    inspector = db.inspect(engine)
    print(inspector.get_table_names())

if __name__ == '__main__':
    app.run()