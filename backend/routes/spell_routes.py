from flask import request, jsonify, Blueprint
from flask_restful import Resource, Api
from backend.models import db, Spell, ClassProgression, Character, Class, ClassSpell

spell_bp = Blueprint('spell', __name__)
spell_api = Api(spell_bp)

# class SpellsByClassAndLevel(Resource):
#     def get(self, class_id, level):
#         # Find the class to get the RPG system ID
#         character_class = Class.query.get_or_404(class_id)
#         rpg_system_id = character_class.rpg_system_id

#         # Fetch all spells that belong to the same RPG system and whose level is <= the selected level
#         available_spells = Spell.query.filter_by(rpg_system_id=rpg_system_id).filter(Spell.level <= level).all()

#         return jsonify([spell.to_dict() for spell in available_spells])


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

        character = Character.query.get_or_404(character_id)
        character.system_data['selected_spells'] = spell_ids
        db.session.commit()

        return {"message": "Spells updated successfully"}
    
class ForcePowerTrees(Resource):
    def get(self):
        # Fetch only spells that have a force_power_tree
        force_trees = Spell.query.filter(Spell.force_power_tree.isnot(None)).all()
        return jsonify([spell.to_dict() for spell in force_trees])
    
# class PurchaseForceTree(Resource):
#     def post(self):
#         data = request.get_json()
#         character_id = data.get('character_id')
#         tree_id = str(data.get('tree_id'))  # Store as string for easier JSON handling
#         xp_cost = data.get('xp_cost')

#         character = Character.query.get_or_404(character_id)

#         # Check if character has enough XP
#         if character.experience_points < xp_cost:
#             return {"message": "Insufficient XP"}, 400

#         # Deduct XP and add the tree to system_data's purchased trees
#         character.experience_points -= xp_cost
#         system_data = character.system_data or {}
        
#         # Ensure the "purchased_trees" key exists
#         if "purchased_trees" not in system_data:
#             system_data["purchased_trees"] = {}

#         # Add the tree to purchased_trees without any nodes selected yet
#         if tree_id not in system_data["purchased_trees"]:
#             system_data["purchased_trees"][tree_id] = []

#         character.system_data = system_data
#         db.session.commit()

#         return {"message": "Tree purchased successfully", "remaining_xp": character.experience_points}



# Spell Routes
spell_api.add_resource(SpellsByClassAndLevel, '/spells/class/<int:class_id>/level/<int:level>')
spell_api.add_resource(AllSpells, '/spells/all')
spell_api.add_resource(UpdateCharacterSpells, '/characters/update-spells')
spell_api.add_resource(ForcePowerTrees, '/force-trees')
# spell_api.add_resource(PurchaseForceTree, '/characters/<int:character_id>/purchase-tree')

