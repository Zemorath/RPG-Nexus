from flask import request, jsonify, Blueprint
from flask_restful import Resource, Api
from backend.models import db, Spell, ClassProgression, Character, Class

spell_bp = Blueprint('spell', __name__)
spell_api = Api(spell_bp)

class SpellsByClassAndLevel(Resource):
    def get(self, class_id, level):
        # Find the class to get the RPG system ID
        character_class = Class.query.get_or_404(class_id)
        rpg_system_id = character_class.rpg_system_id

        # Fetch all spells that belong to the same RPG system and whose level is <= the selected level
        available_spells = Spell.query.filter_by(rpg_system_id=rpg_system_id).filter(Spell.level <= level).all()

        return jsonify([spell.to_dict() for spell in available_spells])



# Fetch all spells for a specific system
class AllSpells(Resource):
    def get(self):
        spells = Spell.query.all()
        return jsonify([spell.to_dict() for spell in spells])

# Update selected spells for a character
class UpdateCharacterSpells(Resource):
    def post(self):
        data = request.get_json()
        character_id = data.get('character_id')
        spell_ids = data.get('spell_ids')

        character = Character.query.get_or_404(character_id)
        character.system_data['selected_spells'] = spell_ids
        db.session.commit()

        return {"message": "Spells updated successfully"}

# Spell Routes
spell_api.add_resource(SpellsByClassAndLevel, '/spells/class/<int:class_id>/level/<int:level>')
spell_api.add_resource(AllSpells, '/spells/all')
spell_api.add_resource(UpdateCharacterSpells, '/characters/update-spells')
