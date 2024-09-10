from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import JSON
from sqlalchemy_serializer import SerializerMixin
from . import db, bcrypt


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

    characters = db.relationship('Character', backref='user', lazy=True)
    managed_campaigns = db.relationship('Campaign', backref='gm_user', lazy=True)
    bookmarked_items = db.relationship('Item', secondary='user_bookmarked_items', backref='users', lazy=True)
    bookmarked_monsters = db.relationship('Monster', secondary='user_bookmarked_monsters', backref='users', lazy=True)
    bookmarked_npcs = db.relationship('NPC', secondary='user_bookmarked_npcs', backref='users', lazy=True)
    homebrew_items = db.relationship('HomebrewItem', back_populates='user', lazy=True)
    homebrew_skills = db.relationship('HomebrewSkill', back_populates='user', lazy=True)
    homebrew_npcs = db.relationship('HomebrewNPC', back_populates='user', lazy=True)
    notes = db.relationship('Note', backref='creator', lazy=True)

    serialize_rules = ('-characters.user', '-managed_campaigns.gm_user')

    def set_password(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)


user_bookmarked_items = db.Table('user_bookmarked_items',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True)
)

user_bookmarked_monsters = db.Table('user_bookmarked_monsters',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('monster_id', db.Integer, db.ForeignKey('monster.id'), primary_key=True)
)

user_bookmarked_npcs = db.Table('user_bookmarked_npcs',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('npc_id', db.Integer, db.ForeignKey('npc.id'), primary_key=True)
)


# Character table
class Character(db.Model, SerializerMixin):
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
    character_homebrew_items = db.relationship('CharacterHomebrewItem', back_populates='character')
    character_homebrew_skills = db.relationship('CharacterHomebrewSkill', back_populates='character')
    campaigns = db.relationship('Campaign', secondary='character_campaign', backref='characters')

    serialize_rules = ('-user.characters', '-skills.character', '-items.character', '-rpg_systems.character', '-races.character', '-classes.character')


# Race table and the related join
class Race(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    size = db.Column(db.String(20), nullable=True)
    speed = db.Column(db.Integer, nullable=True)
    languages = db.Column(db.Text, nullable=True)
    vision_type = db.Column(db.String(50), nullable=True)
    natural_weapons = db.Column(db.Text, nullable=True)
    favored_class = db.Column(db.String(50), nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    characters = db.relationship('CharacterRace', backref='race', lazy=True)
    rpg_system = db.relationship('RPGSystem', backref=db.backref('races', lazy=True))

    serialize_rules = ('-characters.race', '-rpg_system.races')


class CharacterRace(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)
    system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    serialize_rules = ('-character.races', '-race.characters')

# class Character(db.Model, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
#     race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=True)  # Direct foreign key to Race
#     level = db.Column(db.Integer, nullable=False)
#     health = db.Column(db.Integer, nullable=True)
#     experience_points = db.Column(db.Integer, nullable=True)
#     alignment = db.Column(db.String(20), nullable=True)
#     background = db.Column(db.String(100), nullable=True)
#     inventory_weight_limit = db.Column(db.Integer, nullable=True)
#     status_effects = db.Column(db.JSON, nullable=True)
#     last_active = db.Column(db.DateTime, nullable=True)
#     system_data = db.Column(db.JSON, nullable=True)
#     physical_features = db.Column(db.JSON, nullable=True)

#     # Relationships to other tables
#     skills = db.relationship('CharacterSkill', backref='character', lazy=True, cascade="all, delete-orphan")
#     items = db.relationship('CharacterItem', backref='character', lazy=True, cascade="all, delete-orphan")
#     rpg_systems = db.relationship('CharacterRPGSystem', backref='character', lazy=True, cascade="all, delete-orphan")
#     classes = db.relationship('CharacterClass', backref='character', lazy=True, cascade="all, delete-orphan")
#     character_homebrew_items = db.relationship('CharacterHomebrewItem', back_populates='character')
#     character_homebrew_skills = db.relationship('CharacterHomebrewSkill', back_populates='character')
#     campaigns = db.relationship('Campaign', secondary='character_campaign', backref='characters')

#     serialize_rules = ('-user.characters', '-skills.character', '-items.character', '-rpg_systems.character')

# class Race(db.Model, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     size = db.Column(db.String(20), nullable=True)
#     speed = db.Column(db.Integer, nullable=True)
#     languages = db.Column(db.Text, nullable=True)
#     vision_type = db.Column(db.String(50), nullable=True)
#     natural_weapons = db.Column(db.Text, nullable=True)
#     favored_class = db.Column(db.String(50), nullable=True)
#     rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

#     rpg_system = db.relationship('RPGSystem', backref=db.backref('races', lazy=True))

#     serialize_rules = ('-characters.race', '-rpg_system.races')



# Class table and the related join
class Class(db.Model, SerializerMixin):
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
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    characters = db.relationship('CharacterClass', backref='char_class', lazy=True)
    rpg_system = db.relationship('RPGSystem', backref=db.backref('classes', lazy=True))

    serialize_rules = ('-characters.char_class', '-rpg_system.classes')


class CharacterClass(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    serialize_rules = ('-character.classes', '-char_class.characters')


# Skill table and the related join table
class Skill(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    associated_ability = db.Column(db.String(50), nullable=True)
    skill_category = db.Column(db.String(50), nullable=True)
    difficulty_class = db.Column(db.Integer, nullable=True)
    requires_training = db.Column(db.Boolean, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    characters = db.relationship('CharacterSkill', backref='skill', lazy=True)
    rpg_system = db.relationship('RPGSystem', backref=db.backref('skills', lazy=True))

    serialize_rules = ('-characters.skill', '-rpg_system.skills')


class CharacterSkill(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

    serialize_rules = ('-character.skills', '-skill.characters')


class HomebrewSkill(db.Model, SerializerMixin):
    __tablename__ = 'homebrew_skills'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    associated_ability = db.Column(db.String(50), nullable=False)
    skill_category = db.Column(db.String(50), nullable=True)
    difficulty_class = db.Column(db.Integer, nullable=True)
    requires_training = db.Column(db.Boolean, default=False)
    system_data = db.Column(JSON, nullable=True)

    # Relationships
    user = db.relationship('User', back_populates='homebrew_skills')
    character_homebrew_skills = db.relationship('CharacterHomebrewSkill', back_populates='homebrew_skill')

    serialize_rules = ('-user.homebrew_skills', '-character_homebrew_skills.homebrew_skill')


class CharacterHomebrewSkill(db.Model, SerializerMixin):
    __tablename__ = 'character_homebrew_skill'

    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    homebrew_skill_id = db.Column(db.Integer, db.ForeignKey('homebrew_skills.id'), nullable=False)

    character = db.relationship('Character', back_populates='character_homebrew_skills')
    homebrew_skill = db.relationship('HomebrewSkill', back_populates='character_homebrew_skills')

    serialize_rules = ('-character.character_homebrew_skills', '-homebrew_skill.character_homebrew_skills')


# Item Table and the related join table
class Item(db.Model, SerializerMixin):
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
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    characters = db.relationship('CharacterItem', backref='item', lazy=True)
    rpg_system = db.relationship('RPGSystem', backref=db.backref('items', lazy=True))

    serialize_rules = ('-characters.item', '-rpg_system.items')


class CharacterItem(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

    serialize_rules = ('-character.items', '-item.characters')


class HomebrewItem(db.Model, SerializerMixin):
    __tablename__ = 'homebrew_items'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    rarity = db.Column(db.String(50), nullable=True)
    cost = db.Column(db.Integer, nullable=True)
    damage_type = db.Column(db.String(50), nullable=True)
    durability = db.Column(db.Integer, nullable=True)
    enchantment_level = db.Column(db.Integer, nullable=True)
    material = db.Column(db.String(100), nullable=True)
    slot_type = db.Column(db.String(50), nullable=True)
    system_data = db.Column(JSON, nullable=True)

    user = db.relationship('User', back_populates='homebrew_items')
    character_homebrew_items = db.relationship('CharacterHomebrewItem', back_populates='homebrew_item')

    serialize_rules = ('-user.homebrew_items', '-character_homebrew_items.homebrew_item')


class CharacterHomebrewItem(db.Model, SerializerMixin):
    __tablename__ = 'character_homebrew_item'

    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    homebrew_item_id = db.Column(db.Integer, db.ForeignKey('homebrew_items.id'), nullable=False)

    character = db.relationship('Character', back_populates='character_homebrew_items')
    homebrew_item = db.relationship('HomebrewItem', back_populates='character_homebrew_items')

    serialize_rules = ('-character.character_homebrew_items', '-homebrew_item.character_homebrew_items')


# RPG System table and the related join table
class RPGSystem(db.Model, SerializerMixin):
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

    serialize_rules = ('-characters.rpg_system', '-classes.rpg_system', '-races.rpg_system', '-skills.rpg_system', '-items.rpg_system', '-monsters.rpg_system')


class CharacterRPGSystem(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    serialize_rules = ('-character.rpg_systems', '-rpg_system.characters')


# Campaign models
class Campaign(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    status = db.Column(db.String(20), nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    player_count = db.Column(db.Integer, nullable=True)
    gm_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    session_logs = db.Column(db.JSON, nullable=True)
    difficulty_level = db.Column(db.String(50), nullable=True)
    world_setting = db.Column(db.String(255), nullable=True)
    house_rules = db.Column(db.Text, nullable=True)

    notes = db.relationship('Note', backref='campaign', lazy=True)

    serialize_rules = ('-characters.campaign', '-gm_user.managed_campaigns')


# CharacterCampaign Join Table
character_campaign = db.Table('character_campaign',
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True),
    db.Column('campaign_id', db.Integer, db.ForeignKey('campaign.id'), primary_key=True)
)


# Note model
class Note(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=True)
    note_type = db.Column(db.String(50), nullable=True)
    tags = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    last_updated = db.Column(db.DateTime, nullable=True)
    shared_with = db.Column(db.JSON, nullable=True)
    related_entities = db.Column(db.JSON, nullable=True)

    serialize_rules = ('-creator.notes', '-campaign.notes', '-character.notes')


# Monsters
class Monster(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
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

    rpg_system = db.relationship('RPGSystem', backref=db.backref('monsters', lazy=True))

    serialize_rules = ('-rpg_system.monsters',)


class HomebrewMonster(db.Model, SerializerMixin):
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

    serialize_rules = ('-rpg_system.monsters', '-user.homebrew_monsters')


# Join table
class CampaignMonster(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    monster_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=True)  # Link to master monster list
    homebrew_monster_id = db.Column(db.Integer, db.ForeignKey('homebrew_monster.id'), nullable=True)  # Link to homebrew monster

    serialize_rules = ('-campaign.characters', '-monster.characters', '-homebrew_monster.characters')


# NPCs
class NPC(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    role = db.Column(db.String(50), nullable=True)  # Merchant, Guard, Noble
    alignment = db.Column(db.String(20), nullable=True)
    abilities = db.Column(db.JSON, nullable=True)
    inventory = db.Column(db.JSON, nullable=True)
    motivations = db.Column(db.JSON, nullable=True)

    serialize_rules = ('-rpg_system.npcs', '-campaign.characters')


class HomebrewNPC(db.Model, SerializerMixin):
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

    user = db.relationship('User', back_populates='homebrew_npcs')

    serialize_rules = ('-rpg_system.npcs', '-user.homebrew_npcs')


# Join table
class CampaignNPC(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    npc_id = db.Column(db.Integer, db.ForeignKey('npc.id'), nullable=True)  # Link to master NPC list
    homebrew_npc_id = db.Column(db.Integer, db.ForeignKey('homebrew_npc.id'), nullable=True)  # Link to homebrew NPC

    serialize_rules = ('-campaign.characters', '-npc.characters', '-homebrew_npc.characters')


__table_args__ = (
    db.CheckConstraint(
        'monster_id IS NOT NULL OR homebrew_monster_id IS NOT NULL',
        name='check_monster_or_homebrew_monster'
    ),
    db.CheckConstraint(
        'npc_id IS NOT NULL OR homebrew_npc_id IS NOT NULL',
        name='check_npc_or_homebrew_npc'
    ),
)
