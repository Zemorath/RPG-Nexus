from flask import request, jsonify, session
from flask_restful import Resource
from models import db, Race, User, Campaign, CharacterRace

# List all races
class RaceList(Resource):
    def get(self):
        races = Race.query.all()
        return jsonify([race.to_dict() for race in races])

# Details of specific race
class RaceDetail(Resource):
    def get(self, race_id):
        race = Race.query.get_or_404(race_id)
        return race.to_dict()

# Create new Race
class RaceCreate(Resource):
    def post(self):
        data = request.get_json()

        new_race = Race(
            name=data.get('name'),
            description=data.get('description'),
            size=data.get('size'),
            speed=data.get('speed'),
            languages=data.get('languages'),
            vision_type=data.get('vision_type'),
            natural_weapons=data.get('natural_weapons'),
            favored_class=data.get('favored_class'),
        )

        db.session.add(new_race)
        db.session.commit()
        return new_race.to_dict(), 201

# Update Race
class RaceUpdate(Resource):
    def put(self, race_id):
        race = Race.query.get_or_404(race_id)
        data = request.get_json()

        race.name = data.get('name', race.name)
        race.description = data.get('description', race.description)
        race.size = data.get('size', race.size)
        race.speed = data.get('speed', race.speed)
        race.languages = data.get('languages', race.languages)
        race.vision_type = data.get('vision_type', race.vision_type)
        race.natural_weapons = data.get('natural_weapons', race.natural_weapons)
        race.favored_class = data.get('favored_class', race.favored_class)

        db.session.commit()
        return race.to_dict(), 200

# Delete Race
class RaceDelete(Resource):
    def delete(self, race_id):
        race = Race.query.get_or_404(race_id)
        db.session.delete(race)
        db.session.commit()
        return {"message": "Race deleted successfully"}, 200

# Search Races
class RaceSearch(Resource):
    def get(self):
        name = request.args.get('name')
        size = request.args.get('size')
        speed = request.args.get('speed')
        favored_class = request.args.get('favored_class')

        query = Race.query
        if name:
            query = query.filter(Race.name.ilike(f'%{name}%'))
        if size:
            query = query.filter_by(size=size)
        if speed:
            query = query.filter_by(speed=speed)
        if favored_class:
            query = query.filter_by(favored_class=favored_class)

        races = query.all()
        return jsonify([race.to_dict() for race in races])

# List Races by RPG
class RaceByRPGSystem(Resource):
    def get(self, rpg_system_id):
        races = Race.query.filter_by(rpg_system_id=rpg_system_id).all()
        return jsonify([race.to_dict() for race in races])

# Get Races associated with campaign
class RaceByCampaign(Resource):
    def get(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        rpg_system_id = campaign.rpg_system_id
        races = Race.query.filter_by(rpg_system_id=rpg_system_id).all()
        return jsonify([race.to_dict() for race in races])

# List unique race traits
class RaceTraitsList(Resource):
    def get(self):
        traits = Race.query.with_entities(Race.natural_weapons, Race.size, Race.vision_type).distinct().all()
        return jsonify([{"natural_weapons": t[0], "size": t[1], "vision_type": t[2]} for t in traits])

# Race by character
class RaceByCharacter(Resource):
    def get(self, character_id):
        character_races = CharacterRace.query.filter_by(character_id=character_id).all()
        races = [character_race.race.to_dict() for character_race in character_races]
        return jsonify(races)
