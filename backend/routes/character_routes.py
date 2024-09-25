from flask import request, jsonify, Blueprint, session
from flask_restful import Resource, Api
from backend.models import db, Character, Feat, CharacterFeat, Spell, ClassProgression, Alignment, Background, RPGSystem
from backend.utils.calculation_service import CalculationService

character_bp = Blueprint('character', __name__, url_prefix='/api')
character_api = Api(character_bp)

calculation_service = CalculationService()

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

        if 'race_id' in data:
            character.race_id = data['race_id']

        if 'class_id' in data:
            character.class_id = data['class_id']

        if 'inventory' in data:
            character.inventory = data['inventory']

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
        user_id = session.get('user_id')
        if not user_id:
            return {"error": "Unauthorized access"}, 401

        # Fetch characters for the logged-in user
        characters = Character.query.filter_by(user_id=user_id).all()

        character_data = [character.to_dict() for character in characters]

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

        # Fetch RPG system
        rpg_system = RPGSystem.query.get(data.get('rpg_system_id'))
        if not rpg_system:
            return {"message": "RPG System not found"}, 404

        # Initialize default skills and saving throws for the RPG system
        default_skills = self.get_default_skills(rpg_system)
        default_saving_throws = self.get_default_saving_throws(rpg_system)

        # Initialize character with base stats
        new_character = Character(
            user_id=data.get('user_id'),
            rpg_system_id=data.get('rpg_system_id'),
            race_id=data.get('race_id'),
            level=1,
            health=1,  # Default starting health
            system_data={},  # Additional system-specific data
            name="Unnamed Character",  # Default name
            skills=default_skills,  # Initialize skills based on the RPG system
            saving_throws=default_saving_throws,  # Initialize saving throws
            proficiency_bonus=2,  # Default proficiency bonus for a level 1 character
            initiative=0,  # Initiative will be calculated based on ability scores later
        )
        
        db.session.add(new_character)
        db.session.commit()

        return new_character.to_dict(), 201

    def get_default_skills(self, rpg_system):
        """
        Fetch the default skills for the selected RPG system and map them to the character.
        This function assumes that the RPG system has a list of associated skills.
        """
        default_skills = {}
        for skill in rpg_system.skills:
            default_skills[skill.name] = {
                'ability': skill.associated_ability,
                'proficient': False,  # Default proficiency is False
                'bonus': 0  # No additional bonus at the start
            }
        return default_skills

    def get_default_saving_throws(self, rpg_system):
        """
        Fetch the default saving throws for the selected RPG system.
        In many RPG systems like D&D, saving throws are associated with ability scores.
        """
        default_saving_throws = {
            "Strength": {'proficient': False, 'bonus': 0},
            "Dexterity": {'proficient': False, 'bonus': 0},
            "Constitution": {'proficient': False, 'bonus': 0},
            "Intelligence": {'proficient': False, 'bonus': 0},
            "Wisdom": {'proficient': False, 'bonus': 0},
            "Charisma": {'proficient': False, 'bonus': 0},
        }
        return default_saving_throws


class UpdateCharacterClass(Resource):
    def post(self):
        # Get JSON data from the request
        data = request.get_json()

        # Find the character by ID
        character = Character.query.get_or_404(data.get('character_id'))

        # Assign the selected class_id to the character
        class_id = data.get('class_id')
        if not class_id:
            return {"message": "class_id is required"}, 400

        character.class_id = class_id

        # Commit the change to the database
        db.session.commit()

        # Return the updated character data
        return character.to_dict(), 200


    
class UpdateCharacterAbilityScores(Resource):
    def post(self):
        data = request.get_json()

        # Fetch character
        character = Character.query.get(data.get('character_id'))
        if not character:
            return {"message": "Character not found"}, 404

        # Update the ability scores
        character.ability_scores = data.get('ability_scores', {})

        db.session.commit()

        return character.to_dict(), 200

class CharacterFeats(Resource):
    def get(self, character_id):
        character = Character.query.get_or_404(character_id)

        # Fetch feats related to the character's class and race
        feats = Feat.query.filter_by(rpg_system_id=character.rpg_system_id).all()

        return {
            "feats": [feat.to_dict() for feat in feats]
        }

class UpdateCharacterFeats(Resource):
    def post(self):
        data = request.get_json()

        # Find the character by ID
        character = Character.query.get(data.get('character_id'))
        if not character:
            return {"message": "Character not found"}, 404

        # Update character's feats
        feat_ids = data.get('feat_ids', [])

        # Delete old feats
        CharacterFeat.query.filter_by(character_id=character.id).delete()

        # Add new feats
        for feat_id in feat_ids:
            new_feat = CharacterFeat(character_id=character.id, feat_id=feat_id)
            db.session.add(new_feat)

        db.session.commit()

        return character.to_dict(), 200
    
class UpdateCharacterSpells(Resource):
    def post(self):
        data = request.get_json()
        character_id = data.get('character_id')
        spell_ids = data.get('spell_ids')

        # Find the character
        character = Character.query.get_or_404(character_id)
        
        # Ensure spell_ids exist and are valid
        if not spell_ids or not isinstance(spell_ids, list):
            return {"message": "Invalid or missing spell IDs"}, 400

        # Fetch the corresponding spells from the database
        selected_spells = Spell.query.filter(Spell.id.in_(spell_ids)).all()

        if not selected_spells:
            return {"message": "No valid spells found"}, 404

        # Store selected spells in character system_data (or wherever you are storing the data)
        character.system_data = character.system_data or {}
        character.system_data['selected_spells'] = [spell.id for spell in selected_spells]

        db.session.commit()

        return {"message": "Spells updated successfully"}, 200

class UpdateCharacterClassProgression(Resource):
    def post(self):
        data = request.get_json()
        character_id = data.get('character_id')
        level = data.get('level')  # New level provided

        # Find the character
        character = Character.query.get_or_404(character_id)

        if not character.class_id:
            return {"message": "Character does not have a class assigned"}, 400

        # Find the corresponding class progression for the character's class and new level
        class_progression = ClassProgression.query.filter_by(class_id=character.class_id, level=level).first()

        if not class_progression:
            return {"message": "Class progression not found for this level"}, 404

        # Update the character's progression based on the new level
        character.level = level

        
        db.session.commit()

        return {"message": "Class progression updated successfully"}, 200

class UpdateCharacterLevel(Resource):
    def post(self):
        data = request.get_json()
        character_id = data.get('character_id')
        new_level = data.get('level')

        # Find the character by ID
        character = Character.query.get_or_404(character_id)

        if not character.class_id:
            return {"message": "Character does not have a class assigned"}, 400

        # Update the character's level
        character.level = new_level

        # Find the corresponding class progression for the character's class and new level
        class_progression = ClassProgression.query.filter_by(class_id=character.class_id, level=new_level).first()

        if not class_progression:
            return {"message": "Class progression not found for this level"}, 404

        # Update the character's class progression
        character.class_progression_id = class_progression.id

        # Commit the changes
        db.session.commit()

        return {"message": "Character level and progression updated successfully", "character": character.to_dict()}, 200
    
class ClassProgressionResource(Resource):
    def get(self, class_id, level):
        # Query the class progression based on the class_id and level
        class_progression = ClassProgression.query.filter_by(class_id=class_id, level=level).first()

        if not class_progression:
            return {"message": "Class progression not found for this level"}, 404

        return class_progression.to_dict(), 200

class BackgroundsByRPGSystemResource(Resource):
    def get(self, rpg_system_id):
        # Query the backgrounds based on the provided RPG system ID
        backgrounds = Background.query.filter_by(rpg_system_id=rpg_system_id).all()
        
        if not backgrounds:
            return {"message": "No backgrounds found for this RPG system"}, 404
        
        return [background.to_dict() for background in backgrounds], 200

class AlignmentsByRPGSystemResource(Resource):
    def get(self, rpg_system_id):
        # Query the alignments based on the provided RPG system ID
        alignments = Alignment.query.filter_by(rpg_system_id=rpg_system_id).all()
        
        if not alignments:
            return {"message": "No alignments found for this RPG system"}, 404
        
        return [alignment.to_dict() for alignment in alignments], 200
    
class UpdateCharacterInventory(Resource):
    def post(self):
        data = request.get_json()
        character = Character.query.get_or_404(data['character_id'])

        # Update the inventory with the selected item IDs
        character.inventory = data.get('item_ids', [])
        db.session.commit()

        return {'message': 'Inventory updated successfully'}, 200


class UpdateCharacterBackground(Resource):
    def post(self):
        data = request.get_json()
        character_id = data.get('character_id')
        name = data.get('name')
        alignment_name = data.get('alignment')
        background_name = data.get('background')

        character = Character.query.get_or_404(character_id)

        # Update character name
        if name:
            character.name = name

        # Update alignment_id based on the alignment name
        if alignment_name:
            alignment = Alignment.query.filter_by(name=alignment_name).first()
            if alignment:
                character.alignment_id = alignment.id

        # Update background_id based on the background name
        if background_name:
            background = Background.query.filter_by(name=background_name).first()
            if background:
                character.background_id = background.id

        # Update physical features and other details
        character.physical_features = {
            "hair": data.get("description", {}).get("hair"),
            "skin": data.get("description", {}).get("skin"),
            "eyes": data.get("description", {}).get("eyes"),
            "height": data.get("description", {}).get("height"),
            "weight": data.get("description", {}).get("weight"),
            "age": data.get("description", {}).get("age"),
            "gender": data.get("description", {}).get("gender"),
            "traits": data.get("traits", []),
            "ideals": data.get("ideals", []),
            "bonds": data.get("bonds", []),
            "flaws": data.get("flaws", []),
            "organizations": data.get("organizations", []),
            "allies": data.get("allies", []),
            "enemies": data.get("enemies", []),
            "other": data.get("other", [])
        }

        # Commit the changes to the database
        db.session.commit()

        return {"message": "Character background updated successfully"}, 200
    
class CharacterCalculation(Resource):
    def get(self, character_id):
        # Fetch the character from the database
        character = Character.query.get_or_404(character_id)
        character_data = character.to_dict()

        # Use the CalculationService to apply the calculations
        calculation_service = CalculationService()
        calculated_character = calculation_service.calculate_dnd5e_stats(character_data)

        # Return the calculated data
        return calculated_character, 200






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
character_api.add_resource(UpdateCharacterAbilityScores, '/characters/update-ability-scores')
character_api.add_resource(CharacterFeats, '/characters/<int:character_id>/feats')
character_api.add_resource(UpdateCharacterFeats, '/characters/update-feats')
character_api.add_resource(UpdateCharacterSpells, '/characters/update-spells')
character_api.add_resource(UpdateCharacterClassProgression, '/characters/update-class-progression')
character_api.add_resource(ClassProgressionResource, '/class_progression/<int:class_id>/level/<int:level>')
character_api.add_resource(BackgroundsByRPGSystemResource, '/backgrounds/system/<int:rpg_system_id>')
character_api.add_resource(AlignmentsByRPGSystemResource, '/alignments/system/<int:rpg_system_id>')
character_api.add_resource(UpdateCharacterInventory, '/characters/update-items')
character_api.add_resource(UpdateCharacterBackground, '/characters/update-background')
character_api.add_resource(CharacterCalculation, '/characters/calculate/<int:character_id>')


