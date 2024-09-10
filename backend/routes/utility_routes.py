from flask import request, jsonify, Blueprint
from flask_restful import Resource, Api
from backend.models import (
    Character, 
    CharacterClass, 
    CharacterSkill, 
    CharacterItem, 
    RPGSystem, 
    Campaign,
    Note
)

utility_bp = Blueprint('utility', __name__)
utility_api = Api(utility_bp)


class DashboardData(Resource):
    def get(self, user_id):
        characters_count = Character.query.filter_by(user_id=user_id).count()
        campaigns_count = Campaign.query.filter_by(user_id=user_id).count()
        recent_activity = ...  # Logic to fetch recent activity
        return jsonify({
            "characters_count": characters_count,
            "campaigns_count": campaigns_count,
            "recent_activity": recent_activity
        })

class GlobalSearch(Resource):
    def get(self):
        query = request.args.get('query')
        characters = Character.query.filter(Character.name.ilike(f'%{query}%')).all()
        campaigns = Campaign.query.filter(Campaign.name.ilike(f'%{query}%')).all()
        notes = Note.query.filter(Note.title.ilike(f'%{query}%')).all()
        return jsonify({
            "characters": [character.to_dict() for character in characters],
            "campaigns": [campaign.to_dict() for campaign in campaigns],
            "notes": [note.to_dict() for note in notes]
        })


# Utility Routes
utility_api.add_resource(DashboardData, '/dashboard/<int:user_id>/data')
utility_api.add_resource(GlobalSearch, '/search')