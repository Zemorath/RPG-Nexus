from flask import request, jsonify, Blueprint
from flask_restful import Resource, Api
from backend.models import db, Spell, Character, Class, ClassSpell, RPGSystem
from sqlalchemy.orm.attributes import flag_modified

spell_bp = Blueprint('spell', __name__)
spell_api = Api(spell_bp)


class SpellsByClassAndLevel(Resource):
    def get(self, class_id, level):
        # Find the class to ensure it exists
        character_class = Class.query.get_or_404(class_id)
        
        # Fetch all spells for the given class and whose level is <= the selected level
        available_spells = db.session.query(Spell).join(ClassSpell).filter(
            ClassSpell.class_id == class_id,
            Spell.level <= level
        ).all()

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
        remaining_karma = data.get("remaining_karma")

        character = Character.query.get_or_404(character_id)

        old_spells = character.system_data.get("selected_spells", [])
        print(f"Old spell list: {old_spells}")
        print(f"New spell list to save: {spell_ids}")

        character.system_data['selected_spells'] = spell_ids
        flag_modified(character, "system_data")

        if remaining_karma is not None:
            character.experience_points = remaining_karma
            print(f"Updated Karma: {character.experience_points}")
        db.session.commit()
        print("Data committed successfully.")

        return {"message": "Spells updated successfully"}
    
class ForcePowerTrees(Resource):
    def get(self):
        # Fetch only spells that have a force_power_tree
        force_trees = Spell.query.filter(Spell.force_power_tree.isnot(None)).all()
        return jsonify([spell.to_dict() for spell in force_trees])
    
# Fetch all spells specifically for Shadowrun
class ShadowrunSpells(Resource):
    def get(self):
        shadowrun_system = RPGSystem.query.filter_by(name="Shadowrun").first()
        if not shadowrun_system:
            return jsonify({"error": "Shadowrun system not found"}), 404

        shadowrun_spells = Spell.query.filter(Spell.rpg_system_id == shadowrun_system.id).all()
        return jsonify([spell.to_dict() for spell in shadowrun_spells])
    
class CallOfCthulhuSpells(Resource):
    def get(self):
        coc_system = RPGSystem.query.filter_by(name="Call of Cthulhu").first()
        if not coc_system:
            return jsonify({"error": "Call of Cthulhu system not found"}), 404

        coc_spells = Spell.query.filter(Spell.rpg_system_id == coc_system.id).all()
        return jsonify([spell.to_dict() for spell in coc_spells])


# Spell Routes
spell_api.add_resource(SpellsByClassAndLevel, '/spells/class/<int:class_id>/level/<int:level>')
spell_api.add_resource(AllSpells, '/spells/all')
spell_api.add_resource(UpdateCharacterSpells, '/characters/update-spells')
spell_api.add_resource(ForcePowerTrees, '/force-trees')
spell_api.add_resource(ShadowrunSpells, '/spells/shadowrun')
spell_api.add_resource(CallOfCthulhuSpells, '/spells/callofcthulhu')

