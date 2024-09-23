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

    characters = db.relationship('Character', back_populates='user', lazy=True)
    managed_campaigns = db.relationship('Campaign', back_populates='gm_user', lazy=True)
    bookmarked_items = db.relationship('Item', secondary='user_bookmarked_items', back_populates='users', lazy=True)
    bookmarked_monsters = db.relationship('Monster', secondary='user_bookmarked_monsters', back_populates='users', lazy=True)
    bookmarked_npcs = db.relationship('NPC', secondary='user_bookmarked_npcs', back_populates='users', lazy=True)
    homebrew_items = db.relationship('HomebrewItem', back_populates='user', lazy=True)
    homebrew_skills = db.relationship('HomebrewSkill', back_populates='user', lazy=True)
    homebrew_npcs = db.relationship('HomebrewNPC', back_populates='user', lazy=True)
    notes = db.relationship('Note', back_populates='creator', lazy=True)

    serialize_rules = ('-characters.user', '-managed_campaigns.gm_user', '-bookmarked_items.users', '-bookmarked_monsters.users', '-bookmarked_npcs.users', '-homebrew_items.user', '-homebrew_skills.user', '-homebrew_npcs.user', '-notes.creator')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'is_admin': self.is_admin
        }

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

class Character(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    background_id = db.Column(db.Integer, db.ForeignKey('background.id'), nullable=True)
    alignment_id = db.Column(db.Integer, db.ForeignKey('alignment.id'), nullable=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=True)
    level = db.Column(db.Integer, nullable=False)
    health = db.Column(db.Integer, nullable=True)
    experience_points = db.Column(db.Integer, nullable=True)
    alignment = db.Column(db.String(20), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    inventory_weight_limit = db.Column(db.Integer, nullable=True)
    status_effects = db.Column(db.JSON, nullable=True)
    last_active = db.Column(db.DateTime, nullable=True)
    system_data = db.Column(db.JSON, nullable=True)
    physical_features = db.Column(db.JSON, nullable=True)
    ability_scores = db.Column(db.JSON, nullable=True)
    inventory = db.Column(db.JSON, nullable=True)  # List of item IDs

    # Relationships to other tables
    race = db.relationship('Race', back_populates='characters')
    character_class = db.relationship('Class', back_populates='characters')
    skills = db.relationship('CharacterSkill', back_populates='character', lazy=True, cascade="all, delete-orphan")
    feats = db.relationship('CharacterFeat', back_populates='character', lazy=True, cascade="all, delete-orphan")
    spell_slots = db.relationship('SpellSlot', back_populates='character', lazy=True, cascade="all, delete-orphan")

    rpg_system = db.relationship('RPGSystem', back_populates='characters')
    background = db.relationship('Background', back_populates='characters')
    alignment = db.relationship('Alignment', back_populates='characters')
    character_homebrew_items = db.relationship('CharacterHomebrewItem', back_populates='character')
    character_homebrew_skills = db.relationship('CharacterHomebrewSkill', back_populates='character')
    campaigns = db.relationship('Campaign', secondary='character_campaign', back_populates='characters')
    user = db.relationship('User', back_populates='characters')

    serialize_rules = ('-background.characters', '-alignment.characters', '-user.characters', '-skills.character', '-items.character', '-rpg_systems.character', '-race.characters', '-character_class.characters', '-character_homebrew_items.character', '-character_homebrew_skills.character', '-campaigns.characters', '-progressions.character')

    def to_dict(self):
        class_progression = None
        if self.character_class:
            class_progression = ClassProgression.query.filter_by(class_id=self.character_class.id, level=self.level).first()

        inventory_items = []
        if self.inventory:
            # Fetch all item objects corresponding to the IDs stored in the inventory
            inventory_items = Item.query.filter(Item.id.in_(self.inventory)).all()

        return {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'health': self.health,
            'experience_points': self.experience_points,
            'alignment': self.alignment,
            'description': self.description,
            'inventory_weight_limit': self.inventory_weight_limit,
            'inventory': [item.to_dict() for item in inventory_items],
            'status_effects': self.status_effects,
            'last_active': self.last_active,
            'system_data': self.system_data,
            'physical_features': self.physical_features,
            'ability_scores': self.ability_scores,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            },
            'background': self.background.to_dict() if self.background else None,
            'alignment': self.alignment.to_dict() if self.alignment else None,
            'race': {
                'id': self.race.id if self.race else None,
                'name': self.race.name if self.race else None
            },
            'class': {
                'id': self.character_class.id if self.character_class else None,
                'name': self.character_class.name if self.character_class else None,
                'progression': class_progression.to_dict() if class_progression else None
            },
            'user': {
                'id': self.user.id,
                'username': self.user.username
            }
        }




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
    race_features = db.Column(db.JSON, nullable=True)

    rpg_system = db.relationship('RPGSystem', back_populates='races', lazy=True)
    characters = db.relationship('Character', back_populates='race', lazy=True)

    serialize_rules = ('-characters.race', '-rpg_system.races')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'size': self.size,
            'speed': self.speed,
            'languages': self.languages,
            'vision_type': self.vision_type,
            'natural_weapons': self.natural_weapons,
            'favored_class': self.favored_class,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }



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

    characters = db.relationship('Character', back_populates='character_class', lazy=True)
    rpg_system = db.relationship('RPGSystem', back_populates='classes', lazy=True)
    spells = db.relationship('ClassSpell', back_populates='character_class', lazy=True)
    progressions = db.relationship('ClassProgression', back_populates='character_class', lazy=True)

    serialize_rules = ('-characters.character_class', '-rpg_system.classes')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'hit_die': self.hit_die,
            'primary_ability': self.primary_ability,
            'armor_proficiencies': self.armor_proficiencies,
            'weapon_proficiencies': self.weapon_proficiencies,
            'spellcasting': self.spellcasting,
            'subclass_options': self.subclass_options,
            'resource_tracking': self.resource_tracking,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            },
            'progressions': [progression.to_dict() for progression in self.progressions]
        }
    


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

    characters = db.relationship('CharacterSkill', back_populates='skill', lazy=True)
    rpg_system = db.relationship('RPGSystem', back_populates='skills', lazy=True)

    serialize_rules = ('-characters.skill', '-rpg_system.skills')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'associated_ability': self.associated_ability,
            'skill_category': self.skill_category,
            'difficulty_class': self.difficulty_class,
            'requires_training': self.requires_training,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }


class CharacterSkill(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

    character = db.relationship('Character', back_populates='skills')
    skill = db.relationship('Skill', back_populates='characters')

    serialize_rules = ('-character.skills', '-skill.characters')

    def to_dict(self):
        return {
            'id': self.id,
            'character': {
                'id': self.character.id,
                'name': self.character.name
            },
            'skill': {
                'id': self.skill.id,
                'name': self.skill.name
            }
        }
    


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

class Feat(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    associated_ability = db.Column(db.String(50), nullable=True)
    feat_category = db.Column(db.String(50), nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    # Relationship to characters through a join table
    characters = db.relationship('CharacterFeat', back_populates='feat', lazy=True)
    rpg_system = db.relationship('RPGSystem', back_populates='feats', lazy=True)

    serialize_rules = ('-characters.feat', '-rpg_system.feats')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'associated_ability': self.associated_ability,
            'feat_category': self.feat_category,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }
    
class CharacterFeat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    feat_id = db.Column(db.Integer, db.ForeignKey('feat.id'), nullable=False)

    character = db.relationship('Character', back_populates='feats')
    feat = db.relationship('Feat', back_populates='characters')


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
    type = db.Column(db.String(50), nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    rpg_system = db.relationship('RPGSystem', back_populates='items')
    users = db.relationship('User', secondary='user_bookmarked_items', back_populates='bookmarked_items', lazy=True)
    

    serialize_rules = ('-rpg_system.items', '-users.bookmarked_items')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'weight': self.weight,
            'rarity': self.rarity,
            'cost': self.cost,
            'damage_type': self.damage_type,
            'durability': self.durability,
            'enchantment_level': self.enchantment_level,
            'material': self.material,
            'slot_type': self.slot_type,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }


# class CharacterItem(db.Model, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
#     item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

#     character = db.relationship('Character', back_populates='items')
#     item = db.relationship('Item', back_populates='characters')

#     serialize_rules = ('-character.items', '-item.characters')

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'character': {
#                 'id': self.character.id,
#                 'name': self.character.name
#             },
#             'item': {
#                 'id': self.item.id,
#                 'name': self.item.name
#             }
#         }


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

    characters = db.relationship('Character', back_populates='rpg_system', lazy=True)
    races = db.relationship('Race', back_populates='rpg_system', lazy=True)
    classes = db.relationship('Class', back_populates='rpg_system', lazy=True)
    skills = db.relationship('Skill', back_populates='rpg_system', lazy=True)
    items = db.relationship('Item', back_populates='rpg_system', lazy=True)
    monsters = db.relationship('Monster', back_populates='rpg_system', lazy=True)
    feats = db.relationship('Feat', back_populates='rpg_system', lazy=True)
    spells = db.relationship('Spell', back_populates='rpg_system', lazy=True)
    backgrounds = db.relationship('Background', back_populates='rpg_system', lazy=True)
    alignments = db.relationship('Alignment', back_populates='rpg_system', lazy=True)

    serialize_rules = ('-characters.rpg_system', '-classes.rpg_system', '-races.rpg_system', '-skills.rpg_system', '-items.rpg_system', '-monsters.rpg_system', '-npcs.rpg_system', '-feats.rpg_system')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'publisher': self.publisher,
            'edition': self.edition,
            'core_rulebook': self.core_rulebook,
            'genre': self.genre,
            'popularity': self.popularity,
            'default_settings': self.default_settings
        }


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

    notes = db.relationship('Note', back_populates='campaign', lazy=True)
    gm_user = db.relationship('User', back_populates='managed_campaigns')
    characters = db.relationship('Character', secondary='character_campaign', back_populates='campaigns')

    serialize_rules = ('-characters.campaigns', '-gm_user.managed_campaigns', '-notes.campaign')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'player_count': self.player_count,
            'gm_user': {
                'id': self.gm_user.id,
                'username': self.gm_user.username
            } if self.gm_user else None,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }


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
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    last_updated = db.Column(db.DateTime, nullable=True)
    shared_with = db.Column(db.JSON, nullable=True)
    related_entities = db.Column(db.JSON, nullable=True)

    creator = db.relationship('User', back_populates='notes')
    campaign = db.relationship('Campaign', back_populates='notes')

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

    rpg_system = db.relationship('RPGSystem', back_populates='monsters')
    users = db.relationship('User', secondary='user_bookmarked_monsters', back_populates='bookmarked_monsters', lazy=True)

    serialize_rules = ('-rpg_system.monsters', '-users.bookmarked_monsters')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'size': self.size,
            'type': self.type,
            'hit_points': self.hit_points,
            'armor_class': self.armor_class,
            'challenge_rating': self.challenge_rating,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }

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

    users = db.relationship('User', secondary='user_bookmarked_npcs', back_populates='bookmarked_npcs', lazy=True)

    serialize_rules = ('-rpg_system.npcs', '-users.bookmarked_npcs')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'role': self.role,
            'alignment': self.alignment,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }


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

class Spell(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    level = db.Column(db.Integer, nullable=False)  # Spell level (1-9 for D&D)
    school = db.Column(db.String(50), nullable=True)  # School of magic (e.g., Evocation, Necromancy)
    casting_time = db.Column(db.String(50), nullable=True)
    range = db.Column(db.String(50), nullable=True)
    duration = db.Column(db.String(50), nullable=True)
    components = db.Column(db.String(100), nullable=True)  # Verbal, Somatic, Material
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)

    # Relationships
    classes = db.relationship('ClassSpell', back_populates='spell', lazy=True, cascade="all, delete-orphan")
    rpg_system = db.relationship('RPGSystem', back_populates='spells', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'level': self.level,
            'school': self.school,
            'casting_time': self.casting_time,
            'range': self.range,
            'duration': self.duration,
            'components': self.components,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }

class ClassSpell(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    spell_id = db.Column(db.Integer, db.ForeignKey('spell.id'), nullable=False)

    # Relationships
    spell = db.relationship('Spell', back_populates='classes')
    character_class = db.relationship('Class', back_populates='spells')

    def to_dict(self):
        return {
            'class_id': self.class_id,
            'spell_id': self.spell_id,
            'spell': self.spell.to_dict()
        }

class SpellSlot(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    slots_available = db.Column(db.Integer, nullable=False)

    character = db.relationship('Character', back_populates='spell_slots')

    def to_dict(self):
        return {
            'class_id': self.class_id,
            'character_id': self.character_id,
            'level': self.level,
            'slots_available': self.slots_available
        }

class ClassProgression(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    available_spell = db.Column(db.JSON, nullable=True)

    character_class = db.relationship('Class', back_populates='progressions')

    def to_dict(self):
        return {
            'class_id': self.class_id,
            'level': self.level,
            'available_spell': self.available_spell
        }

class Background(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    proficiencies = db.Column(db.JSON, nullable=True)  # JSON for a list of proficiencies
    ability_score_increases = db.Column(db.JSON, nullable=True)  # JSON for ability score increases by system
    granted_feats = db.Column(db.JSON, nullable=True)  # JSON for feats granted by the background
    choosable_feats = db.Column(db.JSON, nullable=True)  # JSON for optional feats that can be chosen by the user
    equipment = db.Column(db.JSON, nullable=True)  # JSON for starting equipment
    languages = db.Column(db.JSON, nullable=True)  # JSON for languages known or learned
    background_features = db.Column(db.JSON, nullable=True)  # Special features unique to the background
    system_specific_data = db.Column(db.JSON, nullable=True)  # JSON field for system-specific information

    rpg_system = db.relationship('RPGSystem', back_populates='backgrounds', lazy=True)
    characters = db.relationship('Character', back_populates='background')

    serialize_rules = ('-rpg_system.backgrounds',)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'proficiencies': self.proficiencies,
            'ability_score_increases': self.ability_score_increases,
            'granted_feats': self.granted_feats,
            'choosable_feats': self.choosable_feats,
            'equipment': self.equipment,
            'languages': self.languages,
            'background_features': self.background_features,
            'system_specific_data': self.system_specific_data,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }

class Alignment(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rpg_system_id = db.Column(db.Integer, db.ForeignKey('rpg_system.id'), nullable=False)
    moral_axis = db.Column(db.String(20), nullable=True)  # "Good", "Neutral", "Evil", etc.
    ethical_axis = db.Column(db.String(20), nullable=True)  # "Lawful", "Neutral", "Chaotic", etc.
    system_specific_data = db.Column(db.JSON, nullable=True)  # JSON for system-specific alignment info

    rpg_system = db.relationship('RPGSystem', back_populates='alignments', lazy=True)
    characters = db.relationship('Character', back_populates='alignment')

    serialize_rules = ('-rpg_system.alignments',)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'moral_axis': self.moral_axis,
            'ethical_axis': self.ethical_axis,
            'system_specific_data': self.system_specific_data,
            'rpg_system': {
                'id': self.rpg_system.id,
                'name': self.rpg_system.name
            }
        }


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
