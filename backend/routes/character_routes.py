from flask import request, jsonify, Blueprint, session
from flask_restful import Resource, Api
from backend.models import db, Character, CharacterSkill, CharacterItem

character_bp = Blueprint('character', __name__, url_prefix='/api')
character_api = Api(character_bp)

# List all characters
class CharacterList(Resource):
    def get(self):
        characters = Character.query.all()
        return jsonify([character.to_dict() for character in characters])

    def post(self):
        data = request.get_json()
        new_character = Character(
            name=data.get('name'),
            user_id=data.get('user_id'),
            rpg_system_id=data.get('rpg_system_id'),
            level=data.get('level'),
            health=data.get('health'),
            experience_points=data.get('experience_points'),
            alignment=data.get('alignment'),
            background=data.get('background'),
            inventory_weight_limit=data.get('inventory_weight_limit'),
            status_effects=data.get('status_effects', []),
            last_active=data.get('last_active'),
            system_data=data.get('system_data', {})
        )
        db.session.add(new_character)
        db.session.commit()
        return new_character.to_dict(), 201

# Character details
class CharacterDetail(Resource):
    def get(self, character_id):
        character = Character.query.get_or_404(character_id)
        return character.to_dict()

    def put(self, character_id):
        character = Character.query.get_or_404(character_id)
        data = request.get_json()

        character.name = data.get('name', character.name)
        character.level = data.get('level', character.level)
        character.health = data.get('health', character.health)
        character.experience_points = data.get('experience_points', character.experience_points)
        character.alignment = data.get('alignment', character.alignment)
        character.background = data.get('background', character.background)
        character.inventory_weight_limit = data.get('inventory_weight_limit', character.inventory_weight_limit)
        character.status_effects = data.get('status_effects', character.status_effects)
        character.last_active = data.get('last_active', character.last_active)
        character.system_data = data.get('system_data', character.system_data)

        db.session.commit()
        return character.to_dict(), 200

    def delete(self, character_id):
        character = Character.query.get_or_404(character_id)
        db.session.delete(character)
        db.session.commit()
        return {"message": "Character deleted successfully"}, 200

class UserCharacters(Resource):
    def get(self):
        user_id = session.get('user_id')  # Fetch user_id from session

        if not user_id:
            return {"error": "Unauthorized access"}, 401

        # Fetch characters for the logged-in user
        characters = Character.query.filter_by(user_id=user_id).all()

        # Prepare the character data
        character_data = [
            {
                "id": character.id,
                "name": character.name,
                "race": character.race.name if character.race else "Unknown",
                "class": character.character_class.name if character.character_class else "Unknown",
                "level": character.level,
                "rpg_system": character.rpg_system.name
            }
            for character in characters
        ]

        return {"characters": character_data}, 200

# Search characters
class SearchCharacters(Resource):
    def get(self):
        name = request.args.get('name')
        level = request.args.get('level')
        rpg_system_id = request.args.get('rpg_system_id')

        query = Character.query
        if name:
            query = query.filter(Character.name.ilike(f'%{name}%'))
        if level:
            query = query.filter_by(level=level)
        if rpg_system_id:
            query = query.filter_by(rpg_system_id=rpg_system_id)

        characters = query.all()
        return jsonify([character.to_dict() for character in characters])

# Level up character
class CharacterLevelUp(Resource):
    def post(self, character_id):
        character = Character.query.get_or_404(character_id)
        character.level += 1
        db.session.commit()
        return character.to_dict(), 200

# Filter characters by RPG system
class CharactersBySystem(Resource):
    def get(self, rpg_system_id):
        characters = Character.query.filter_by(rpg_system_id=rpg_system_id).all()
        return jsonify([character.to_dict() for character in characters])

# Clone character
class CharacterClone(Resource):
    def post(self, character_id):
        character = Character.query.get_or_404(character_id)
        cloned_character = Character(
            name=f"{character.name} (Clone)",
            user_id=character.user_id,
            rpg_system_id=character.rpg_system_id,
            level=character.level,
            health=character.health,
            experience_points=character.experience_points,
            alignment=character.alignment,
            background=character.background,
            inventory_weight_limit=character.inventory_weight_limit,
            status_effects=character.status_effects,
            system_data=character.system_data.copy()
        )
        db.session.add(cloned_character)
        db.session.commit()
        return cloned_character.to_dict(), 201

# Archive character
class CharacterArchive(Resource):
    def post(self, character_id):
        character = Character.query.get_or_404(character_id)
        character.archived = True
        db.session.commit()
        return {"message": "Character archived"}, 200

    def delete(self, character_id):
        character = Character.query.get_or_404(character_id)
        character.archived = False
        db.session.commit()
        return {"message": "Character unarchived"}, 200

# Export character
class CharacterExport(Resource):
    def get(self, character_id):
        character = Character.query.get_or_404(character_id)
        return jsonify(character.to_dict())

# Import character
class CharacterImport(Resource):
    def post(self):
        data = request.get_json()
        new_character = Character(**data)
        db.session.add(new_character)
        db.session.commit()
        return new_character.to_dict(), 201
    
class InitializeCharacter(Resource):
    def post(self):
        data = request.get_json()

        # Create a new character with the selected RPG system and race
        new_character = Character(
            user_id=data.get('user_id'),
            rpg_system_id=data.get('rpg_system_id'),
            race_id=data.get('race_id'),
            level=1,
            health=100,
            system_data={},
            name="Unnamed Character",
        )
        
        db.session.add(new_character)
        db.session.commit()

        return new_character.to_dict(), 201

class UpdateCharacterClass(Resource):
    def post(self):
        data = request.get_json()

        # Find the character by ID
        character = Character.query.get(data.get('character_id'))
        if not character:
            return {"message": "Character not found"}, 404

        # Assign the selected class_id directly
        character.class_id = data.get('class_id')
        
        db.session.commit()

        return character.to_dict(), 200




# Character Routes
character_api.add_resource(CharacterList, '/characters')
character_api.add_resource(CharacterDetail, '/characters/<int:character_id>')
character_api.add_resource(UserCharacters, '/characters/view')
character_api.add_resource(SearchCharacters, '/characters/search')
character_api.add_resource(CharacterLevelUp, '/characters/<int:character_id>/level_up')
character_api.add_resource(CharactersBySystem, '/characters/system/<int:rpg_system_id>')
character_api.add_resource(CharacterClone, '/characters/<int:character_id>/clone')
character_api.add_resource(CharacterArchive, '/characters/<int:character_id>/archive')
character_api.add_resource(CharacterExport, '/characters/<int:character_id>/export')
character_api.add_resource(CharacterImport, '/characters/import')
character_api.add_resource(InitializeCharacter, '/characters/initialize')
character_api.add_resource(UpdateCharacterClass, '/characters/update-class')