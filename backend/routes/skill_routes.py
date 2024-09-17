from flask import request, jsonify, session, Blueprint
from flask_restful import Resource, Api
from backend.models import db, NPC, HomebrewNPC, User, Skill, HomebrewSkill
from backend.utils.decorators import admin_required

skill_bp = Blueprint('skill', __name__)
skill_api = Api(skill_bp)

# Create new skill
class SkillCreate(Resource):
    @admin_required
    def post(self):
        data = request.get_json()

        new_skill = Skill(
            name=data.get('name'),
            description=data.get('description'),
            associated_ability=data.get('associated_ability'),
            skill_category=data.get('skill_category'),
            difficulty_class=data.get('difficulty_class'),
            requires_training=data.get('requires_training', False),
            system_data=data.get('system_data', {}),
        )

        db.session.add(new_skill)
        db.session.commit()
        return new_skill.to_dict(), 201

# Update skill
class SkillUpdate(Resource):
    @admin_required
    def put(self, skill_id):
        skill = Skill.query.get_or_404(skill_id)
        data = request.get_json()

        skill.name = data.get('name', skill.name)
        skill.description = data.get('description', skill.description)
        skill.associated_ability = data.get('associated_ability', skill.associated_ability)
        skill.skill_category = data.get('skill_category', skill.skill_category)
        skill.difficulty_class = data.get('difficulty_class', skill.difficulty_class)
        skill.requires_training = data.get('requires_training', skill.requires_training)
        skill.system_data = data.get('system_data', skill.system_data)

        db.session.commit()
        return skill.to_dict(), 200

# Delete Skill
class SkillDelete(Resource):
    @admin_required
    def delete(self, skill_id):
        skill = Skill.query.get_or_404(skill_id)
        db.session.delete(skill)
        db.session.commit()
        return {"message": "Skill deleted successfully"}, 200


# List all skills
class SkillList(Resource):
    def get(self):
        skills = Skill.query.all()
        return jsonify([skill.to_dict() for skill in skills])
    
# Get details of specific skill
class SkillDetail(Resource):
    def get(self, skill_id):
        skill = Skill.query.get_or_404(skill_id)
        return skill.to_dict()

# Search skills
class SkillSearch(Resource):
    def get(self):
        name = request.args.get('name')
        associated_ability = request.args.get('associated_ability')
        skill_category = request.args.get('skill_category')
        rpg_system_id = request.args.get('rpg_system_id')

        query = Skill.query
        if name:
            query = query.filter(Skill.name.ilike(f'%{name}%'))
        if associated_ability:
            query = query.filter_by(associated_ability=associated_ability)
        if skill_category:
            query = query.filter_by(skill_category=skill_category)
        if rpg_system_id:
            query = query.filter(Skill.system_data['rpg_system_id'].astext == str(rpg_system_id))

        skills = query.all()
        return jsonify([skill.to_dict() for skill in skills])

# List skills by rpg system
class SkillByRPGSystem(Resource):
    def get(self, rpg_system_id):
        skills = Skill.query.filter_by(rpg_system_id=rpg_system_id).all()
        return jsonify([skill.to_dict() for skill in skills])

# Bulk import skills
class BulkImportSkills(Resource):
    def post(self):
        data = request.get_json()

        # Assuming the data contains a list of skills
        for skill_data in data['skills']:
            new_skill = Skill(
                name=skill_data.get('name'),
                description=skill_data.get('description'),
                associated_ability=skill_data.get('associated_ability'),
                skill_category=skill_data.get('skill_category'),
                difficulty_class=skill_data.get('difficulty_class'),
                requires_training=skill_data.get('requires_training', False),
                system_data=skill_data.get('system_data', {}),
            )
            db.session.add(new_skill)
        
        db.session.commit()
        return {"message": "Skills imported successfully"}, 201

# List homebrew skills
class HomebrewSkillList(Resource):
    def get(self):
        homebrew_skills = HomebrewSkill.query.all()
        return jsonify([skill.to_dict() for skill in homebrew_skills])
    
# Create new homebrew skill
class HomebrewSkillCreate(Resource):
    def post(self):
        data = request.get_json()

        new_homebrew_skill = HomebrewSkill(
            user_id=session.get('user_id'),  # Assuming the user's ID is stored in the session
            name=data.get('name'),
            description=data.get('description'),
            associated_ability=data.get('associated_ability'),
            skill_category=data.get('skill_category'),
            difficulty_class=data.get('difficulty_class'),
            requires_training=data.get('requires_training', False),
            system_data=data.get('system_data', {}),
        )

        db.session.add(new_homebrew_skill)
        db.session.commit()
        return new_homebrew_skill.to_dict(), 201

# Update homebrew
class HomebrewSkillUpdate(Resource):
    def put(self, homebrew_skill_id):
        homebrew_skill = HomebrewSkill.query.get_or_404(homebrew_skill_id)
        if homebrew_skill.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        data = request.get_json()

        homebrew_skill.name = data.get('name', homebrew_skill.name)
        homebrew_skill.description = data.get('description', homebrew_skill.description)
        homebrew_skill.associated_ability = data.get('associated_ability', homebrew_skill.associated_ability)
        homebrew_skill.skill_category = data.get('skill_category', homebrew_skill.skill_category)
        homebrew_skill.difficulty_class = data.get('difficulty_class', homebrew_skill.difficulty_class)
        homebrew_skill.requires_training = data.get('requires_training', homebrew_skill.requires_training)
        homebrew_skill.system_data = data.get('system_data', homebrew_skill.system_data)

        db.session.commit()
        return homebrew_skill.to_dict(), 200

# Delete homebrew
class HomebrewSkillDelete(Resource):
    def delete(self, homebrew_skill_id):
        homebrew_skill = HomebrewSkill.query.get_or_404(homebrew_skill_id)
        if homebrew_skill.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        db.session.delete(homebrew_skill)
        db.session.commit()
        return {"message": "Homebrew skill deleted successfully"}, 200

# Export homebrew
class HomebrewSkillExport(Resource):
    def get(self, homebrew_skill_id):
        homebrew_skill = HomebrewSkill.query.get_or_404(homebrew_skill_id)
        if homebrew_skill.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        # Return the skill data as JSON for export
        return jsonify(homebrew_skill.to_dict())

# Import homebrew
class HomebrewSkillImport(Resource):
    def post(self):
        data = request.get_json()

        imported_skill = HomebrewSkill(
            user_id=session.get('user_id'),
            name=data.get('name'),
            description=data.get('description'),
            associated_ability=data.get('associated_ability'),
            skill_category=data.get('skill_category'),
            difficulty_class=data.get('difficulty_class'),
            requires_training=data.get('requires_training', False),
            system_data=data.get('system_data', {}),
        )

        db.session.add(imported_skill)
        db.session.commit()
        return imported_skill.to_dict(), 201

# Skill Management Routes
skill_api.add_resource(SkillList, '/skills')
skill_api.add_resource(SkillDetail, '/skills/<int:skill_id>')
skill_api.add_resource(SkillCreate, '/skills/new')
skill_api.add_resource(SkillUpdate, '/skills/<int:skill_id>/update')
skill_api.add_resource(SkillDelete, '/skills/<int:skill_id>/delete')
skill_api.add_resource(SkillSearch, '/skills/search')
skill_api.add_resource(SkillByRPGSystem, '/skills/rpgsystem/<int:rpg_system_id>')
skill_api.add_resource(BulkImportSkills, '/skills/import')
skill_api.add_resource(HomebrewSkillList, '/homebrew/skills')
skill_api.add_resource(HomebrewSkillCreate, '/homebrew/skills/new')
skill_api.add_resource(HomebrewSkillUpdate, '/homebrew/skills/<int:homebrew_skill_id>/update')
skill_api.add_resource(HomebrewSkillDelete, '/homebrew/skills/<int:homebrew_skill_id>/delete')
skill_api.add_resource(HomebrewSkillExport, '/homebrew/skills/<int:homebrew_skill_id>/export')
skill_api.add_resource(HomebrewSkillImport, '/homebrew/skills/import')