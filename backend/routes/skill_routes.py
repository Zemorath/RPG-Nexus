from flask import request, jsonify, session
from flask_restful import Resource
from models import db, NPC, HomebrewNPC, User, Skill


# Create new skill
class SkillCreate(Resource):
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
        skills = Skill.query.filter(Skill.system_data['rpg_system_id'].astext == str(rpg_system_id)).all()
        return jsonify([skill.to_dict() for skill in skills])

