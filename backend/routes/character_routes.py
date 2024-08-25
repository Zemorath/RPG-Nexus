from flask import request, jsonify
from flask_restful import Resource
from models import db, Character, CharacterRace, CharacterClass, CharacterSkill, CharacterItem

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
