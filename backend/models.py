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
    
# ---------------------------------------------------------------
# Character table
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    health = db.Column(db.Integer, nullable=True)
    experience_points = db.Column(db.Integer, nullable=True)
    alignment = db.Column(db.String(20), nullable=True)
    background = db.Column(db.String(100), nullable=True)
    inventory_weight_limit = db.Column(db.Integer, nullable=True)
    status_effects = db.Column(db.JSON, nullable=True)
    last_active = db.Column(db.DateTime, nullable=True)
    system_data = db.Column(db.JSON, nullable=True)

    # Relationships to other tables
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
    size = db.Column(db.String(20), nullable=True)
    speed = db.Column(db.Integer, nullable=True)
    languages = db.Column(db.String(255), nullable=True)
    vision_type = db.Column(db.String(50), nullable=True)
    natural_weapons = db.Column(db.String(255), nullable=True)
    favored_class = db.Column(db.String(50), nullable=True)
    
    characters = db.relationship('CharacterRace', backref='race', lazy=True)

class CharacterRace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)
    system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False) 

    # System-specific race attributes
    race_data = db.Column(db.JSON, nullable=True)  # This can include traits, bonuses, etc. 

# ---------------------------------------------------------------
# Class table and the related join
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    hit_die = db.Column(db.String(10), nullable=True)
    primary_ability = db.Column(db.String(50), nullable=True)
    armor_proficiencies = db.Column(db.String(255), nullable=True)
    weapon_proficiencies = db.Column(db.String(255), nullable=True)
    spellcasting = db.Column(db.Boolean, nullable=True)
    subclass_options = db.Column(db.JSON, nullable=True)
    resource_tracking = db.Column(db.JSON, nullable=True)
    
    characters = db.relationship('CharacterClass', backref='char_class', lazy=True)


class CharacterClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    # System-specific class attributes
    system_data = db.Column(db.JSON, nullable=True)  # This can include hit dice, spellcasting abilities, etc.  


# ---------------------------------------------------------------
# Skill table and the related join table
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    associated_ability = db.Column(db.String(50), nullable=True)
    skill_category = db.Column(db.String(50), nullable=True)
    difficulty_class = db.Column(db.Integer, nullable=True)
    requires_training = db.Column(db.Boolean, nullable=True)
    
    characters = db.relationship('CharacterSkill', backref='skill', lazy=True)

class CharacterSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

    # System-specific skill attributes
    system_data = db.Column(db.JSON, nullable=True)  # This can include things like proficiency bonuses, effects, etc.


# ---------------------------------------------------------------
# Item Table and the related join table
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    rarity = db.Column(db.String(50), nullable=True)
    cost = db.Column(db.Integer, nullable=True)
    damage_type = db.Column(db.String(50), nullable=True)
    durability = db.Column(db.Integer, nullable=True)
    enchantment_level = db.Column(db.Integer, nullable=True)
    material = db.Column(db.String(50), nullable=True)
    slot_type = db.Column(db.String(50), nullable=True)
    
    characters = db.relationship('CharacterItem', backref='item', lazy=True)


class CharacterItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

    # System-specific item attributes
    system_data = db.Column(db.JSON, nullable=True)  # This can include things like magical properties, weight, etc.

# ---------------------------------------------------------------
# RPG System table and the related join table
class RPGSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    publisher = db.Column(db.String(100), nullable=True)
    edition = db.Column(db.String(50), nullable=True)
    core_rulebook = db.Column(db.String(255), nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    popularity = db.Column(db.Integer, nullable=True)
    default_settings = db.Column(db.JSON, nullable=True)
    
    characters = db.relationship('CharacterRPGSystem', backref='rpg_system', lazy=True)


class CharacterRPGSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    # Additional fields for categorizing or describing the system further
    ruleset_version = db.Column(db.String(20), nullable=True)

# ---------------------------------------------------------------
# General campaign and Note models
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    status = db.Column(db.String(20), nullable=True)  # Active, Paused, Completed
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    player_count = db.Column(db.Integer, nullable=True)  # Number of players
    gm_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Dungeon Master/Game Master
    session_logs = db.Column(db.JSON, nullable=True)  # Collection of session summaries/logs
    difficulty_level = db.Column(db.String(50), nullable=True)  # Beginner, Intermediate, Expert
    world_setting = db.Column(db.String(255), nullable=True)  # World or setting name
    house_rules = db.Column(db.Text, nullable=True)  # Custom rules for the campaign

    notes = db.relationship('Note', backref='campaign', lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=True)
    note_type = db.Column(db.String(50), nullable=True)  # Character Note, Campaign Note
    tags = db.Column(db.String(255), nullable=True)  # Comma-separated list of tags
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # User who created the note
    last_updated = db.Column(db.DateTime, nullable=True)  # Timestamp of last update
    shared_with = db.Column(db.JSON, nullable=True)  # List of user IDs with whom the note is shared
    related_entities = db.Column(db.JSON, nullable=True)  # References to related entities

# ---------------------------------------------------------------
# Monsters
class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    size = db.Column(db.String(20), nullable=True)  # Small, Medium, Large
    type = db.Column(db.String(50), nullable=True)  # Undead, Beast, Humanoid
    hit_points = db.Column(db.Integer, nullable=True)
    armor_class = db.Column(db.Integer, nullable=True)
    challenge_rating = db.Column(db.Float, nullable=True)  # For systems with CR or equivalent
    abilities = db.Column(db.JSON, nullable=True)  # System-specific abilities and traits
    actions = db.Column(db.JSON, nullable=True)  # Actions the monster can perform
    legendary_actions = db.Column(db.JSON, nullable=True)  # Legendary actions, if applicable

class HomebrewMonster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    size = db.Column(db.String(20), nullable=True)
    type = db.Column(db.String(50), nullable=True)
    hit_points = db.Column(db.Integer, nullable=True)
    armor_class = db.Column(db.Integer, nullable=True)
    challenge_rating = db.Column(db.Float, nullable=True)
    abilities = db.Column(db.JSON, nullable=True)
    actions = db.Column(db.JSON, nullable=True)
    legendary_actions = db.Column(db.JSON, nullable=True)

# Join table
class CampaignMonster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    monster_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=True)  # Link to master monster list
    homebrew_monster_id = db.Column(db.Integer, db.ForeignKey('homebrew_monster.id'), nullable=True)  # Link to homebrew monster


# ---------------------------------------------------------------
# NPCs
class NPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    role = db.Column(db.String(50), nullable=True)  # Merchant, Guard, Noble
    alignment = db.Column(db.String(20), nullable=True)  # Lawful Good, Chaotic Neutral
    abilities = db.Column(db.JSON, nullable=True)  # System-specific abilities and traits
    inventory = db.Column(db.JSON, nullable=True)  # Items or resources the NPC possesses
    motivations = db.Column(db.JSON, nullable=True)  # Motivations, goals, or quests related to the NPC

class HomebrewNPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    role = db.Column(db.String(50), nullable=True)
    alignment = db.Column(db.String(20), nullable=True)
    abilities = db.Column(db.JSON, nullable=True)
    inventory = db.Column(db.JSON, nullable=True)
    motivations = db.Column(db.JSON, nullable=True)

# Join table
class CampaignNPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    npc_id = db.Column(db.Integer, db.ForeignKey('npc.id'), nullable=True)  # Link to master NPC list
    homebrew_npc_id = db.Column(db.Integer, db.ForeignKey('homebrew_npc.id'), nullable=True)  # Link to homebrew NPC





