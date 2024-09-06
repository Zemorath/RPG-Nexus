from flask import request, jsonify, session, Blueprint
from flask_restful import Resource, Api
from models import db, Class, CharacterClass, Campaign
from utils.decorators import admin_required

class_bp = Blueprint('class', __name__)
class_api = Api(class_bp)

# List all classes
class ClassList(Resource):
    def get(self):
        classes = Class.query.all()
        return jsonify([cls.to_dict() for cls in classes])

# Get Details of specific class
class ClassDetail(Resource):
    def get(self, class_id):
        cls = Class.query.get_or_404(class_id)
        return cls.to_dict()

# Create new Class
class ClassCreate(Resource):
    @admin_required
    def post(self):
        data = request.get_json()

        new_class = Class(
            name=data.get('name'),
            description=data.get('description'),
            hit_die=data.get('hit_die'),
            primary_ability=data.get('primary_ability'),
            armor_proficiencies=data.get('armor_proficiencies'),
            weapon_proficiencies=data.get('weapon_proficiencies'),
            spellcasting=data.get('spellcasting'),
            subclass_options=data.get('subclass_options'),
            resource_tracking=data.get('resource_tracking'),
        )

        db.session.add(new_class)
        db.session.commit()
        return new_class.to_dict(), 201

# Update class
class ClassUpdate(Resource):
    @admin_required
    def put(self, class_id):
        cls = Class.query.get_or_404(class_id)
        data = request.get_json()

        cls.name = data.get('name', cls.name)
        cls.description = data.get('description', cls.description)
        cls.hit_die = data.get('hit_die', cls.hit_die)
        cls.primary_ability = data.get('primary_ability', cls.primary_ability)
        cls.armor_proficiencies = data.get('armor_proficiencies', cls.armor_proficiencies)
        cls.weapon_proficiencies = data.get('weapon_proficiencies', cls.weapon_proficiencies)
        cls.spellcasting = data.get('spellcasting', cls.spellcasting)
        cls.subclass_options = data.get('subclass_options', cls.subclass_options)
        cls.resource_tracking = data.get('resource_tracking', cls.resource_tracking)

        db.session.commit()
        return cls.to_dict(), 200

# Delete class
class ClassDelete(Resource):
    @admin_required
    def delete(self, class_id):
        cls = Class.query.get_or_404(class_id)
        db.session.delete(cls)
        db.session.commit()
        return {"message": "Class deleted successfully"}, 200

# Search class
class ClassSearch(Resource):
    def get(self):
        name = request.args.get('name')
        primary_ability = request.args.get('primary_ability')
        spellcasting = request.args.get('spellcasting')

        query = Class.query
        if name:
            query = query.filter(Class.name.ilike(f'%{name}%'))
        if primary_ability:
            query = query.filter_by(primary_ability=primary_ability)
        if spellcasting:
            query = query.filter_by(spellcasting=spellcasting)

        classes = query.all()
        return jsonify([cls.to_dict() for cls in classes])

# List classes by RPG
class ClassByRPGSystem(Resource):
    def get(self, rpg_system_id):
        classes = Class.query.filter_by(rpg_system_id=rpg_system_id).all()
        return jsonify([cls.to_dict() for cls in classes])

# Get classes for character
class ClassByCharacter(Resource):
    def get(self, character_id):
        character_classes = CharacterClass.query.filter_by(character_id=character_id).all()
        classes = [character_class.char_class.to_dict() for character_class in character_classes]
        return jsonify(classes)

# Unique class ability
class ClassAbilitiesList(Resource):
    def get(self):
        abilities = Class.query.with_entities(Class.primary_ability).distinct().all()
        return jsonify([{"primary_ability": a[0]} for a in abilities])

# List subclasses
class SubclassOptions(Resource):
    def get(self, class_id):
        cls = Class.query.get_or_404(class_id)
        if cls.subclass_options:
            return jsonify(cls.subclass_options)
        else:
            return {"message": "No subclass options available"}, 404

# List classes by difficulty
class ClassByDifficulty(Resource):
    def get(self, difficulty_level):
        classes = Class.query.filter_by(difficulty_level=difficulty_level).all()
        return jsonify([cls.to_dict() for cls in classes])

# Class Management Routes
class_api.add_resource(ClassList, '/classes')
class_api.add_resource(ClassDetail, '/classes/<int:class_id>')
class_api.add_resource(ClassCreate, '/classes/new')
class_api.add_resource(ClassUpdate, '/classes/<int:class_id>/update')
class_api.add_resource(ClassDelete, '/classes/<int:class_id>/delete')
class_api.add_resource(ClassSearch, '/classes/search')
class_api.add_resource(ClassByRPGSystem, '/classes/rpgsystem/<int:rpg_system_id>')
class_api.add_resource(ClassByCharacter, '/classes/character/<int:character_id>')
class_api.add_resource(ClassAbilitiesList, '/classes/abilities')
class_api.add_resource(SubclassOptions, '/classes/<int:class_id>/subclass_options')
class_api.add_resource(ClassByDifficulty, '/classes/difficulty/<string:difficulty_level>')