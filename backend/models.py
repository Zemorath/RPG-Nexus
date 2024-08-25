from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    characters = db.relationship('Character', backref='user', lazy=True)
    campaigns = db.relationship('Campaign', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    # Relationships to join tables for skills, items, RPG systems, races, and classes
    skills = db.relationship('CharacterSkill', backref='character', lazy=True, cascade="all, delete-orphan")
    items = db.relationship('CharacterItem', backref='character', lazy=True, cascade="all, delete-orphan")
    rpg_systems = db.relationship('CharacterRPGSystem', backref='character', lazy=True, cascade="all, delete-orphan")
    races = db.relationship('CharacterRace', backref='character', lazy=True, cascade="all, delete-orphan")
    classes = db.relationship('CharacterClass', backref='character', lazy=True, cascade="all, delete-orphan")


# ---------------------------------------------------------------
# Race table and the related join
class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

class CharacterRace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)
    system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)  

# ---------------------------------------------------------------
# Class table and the related join
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    # Additional fields like hit dice, spellcasting ability, etc.

class CharacterClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)  


# ---------------------------------------------------------------
# Skill table and the related join table
class CharacterSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)  

# ---------------------------------------------------------------
# Item Table and the related join table
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

class CharacterItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

# ---------------------------------------------------------------
# RPG System table and the related join table
class RPGSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

class CharacterRPGSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

# ---------------------------------------------------------------
# General campaign and Note models
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    notes = db.relationship('Note', backref='campaign', lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=True)
