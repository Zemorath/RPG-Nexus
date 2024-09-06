from flask import request, jsonify, session, Blueprint
from flask_restful import Resource, Api
from models import db, Campaign, Character, User, NPC, Monster, character_campaign

campaign_bp = Blueprint('campaign', __name__)
campaign_api = Api(campaign_bp)

# Show all campaigns a user's character is a part of
class CampaignList(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return {"message": "User not logged in"}, 401

        user = User.query.get_or_404(user_id)

        campaigns = Campaign.query.join(character_campaign).join(Character).filter(Character.user_id == user.id).all()
        return jsonify([campaign.to_dict() for campaign in campaigns])

# Get details of a specific campaign
class CampaignDetail(Resource):
    def get(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        return campaign.to_dict()

# Create a new campaign
class CampaignCreate(Resource):
    def post(self):
        data = request.get_json()
        new_campaign = Campaign(
            name=data.get('name'),
            description=data.get('description'),
            rpg_system_id=data.get('rpg_system_id'),
            status=data.get('status', 'Active'),
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            player_count=data.get('player_count', 0),
            gm_id=data.get('gm_id'),
            world_setting=data.get('world_setting'),
            house_rules=data.get('house_rules', ''),
        )
        db.session.add(new_campaign)
        db.session.commit()
        return new_campaign.to_dict(), 201

# Update campaign
class CampaignUpdate(Resource):
    def put(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        data = request.get_json()

        campaign.name = data.get('name', campaign.name)
        campaign.description = data.get('description', campaign.description)
        campaign.status = data.get('status', campaign.status)
        campaign.end_date = data.get('end_date', campaign.end_date)
        campaign.player_count = data.get('player_count', campaign.player_count)
        campaign.world_setting = data.get('world_setting', campaign.world_setting)
        campaign.house_rules = data.get('house_rules', campaign.house_rules)

        db.session.commit()
        return campaign.to_dict(), 200

# Delete a campaign
class CampaignDelete(Resource):
    def delete(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        db.session.delete(campaign)
        db.session.commit()
        return {"message": "Campaign deleted successfully"}, 200

# Add character to campaign
class CampaignAddCharacter(Resource):
    def post(self, campaign_id):
        data = request.get_json()
        character_id = data.get('character_id')
        campaign = Campaign.query.get_or_404(campaign_id)

        if character_id not in [char.id for char in campaign.characters]:
            campaign.characters.append(Character.query.get(character_id))
            db.session.commit()
        return {"message": "Character added to campaign"}, 200

# Remove character from campaign
class CampaignRemoveCharacter(Resource):
    def delete(self, campaign_id, character_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        character = Character.query.get_or_404(character_id)

        if character in campaign.characters:
            campaign.characters.remove(character)
            db.session.commit()
        return {"message": "Character removed from campaign"}, 200

# Session logs
class CampaignSessionLogs(Resource):
    def get(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        return jsonify(campaign.session_logs)

# Add session log
class CampaignAddSessionLog(Resource):
    def post(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        data = request.get_json()

        campaign.session_logs.append({
            "date": data.get('date'),
            "log": data.get('log')
        })
        db.session.commit()
        return {"message": "Session log added"}, 200

# Update house rules
class CampaignHouseRules(Resource):
    def put(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        data = request.get_json()

        campaign.house_rules = data.get('house_rules')
        db.session.commit()
        return {"message": "House rules updated"}, 200

# Search campaigns
class CampaignSearch(Resource):
    def get(self):
        name = request.args.get('name')
        rpg_system_id = request.args.get('rpg_system_id')
        status = request.args.get('status')

        query = Campaign.query
        if name:
            query = query.filter(Campaign.name.ilike(f'%{name}%'))
        if rpg_system_id:
            query = query.filter_by(rpg_system_id=rpg_system_id)
        if status:
            query = query.filter_by(status=status)

        campaigns = query.all()
        return jsonify([campaign.to_dict() for campaign in campaigns])

# List NPCs
class CampaignNPCList(Resource):
    def get(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        return jsonify([npc.to_dict() for npc in campaign.npcs])

# Add NPC
class CampaignAddNPC(Resource):
    def post(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        data = request.get_json()

        npc_id = data.get('npc_id')
        npc = NPC.query.get_or_404(npc_id)

        if npc not in campaign.npcs:
            campaign.npcs.append(npc)
            db.session.commit()
            return {"message": "NPC added to campaign"}, 201
        else:
            return {"message": "NPC already exists in this campaign"}, 400

# Remove NPC
class CampaignRemoveNPC(Resource):
    def delete(self, campaign_id, npc_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        npc = NPC.query.get_or_404(npc_id)

        if npc in campaign.npcs:
            campaign.npcs.remove(npc)
            db.session.commit()
            return {"message": "NPC removed from campaign"}, 200
        else:
            return {"message": "NPC not found in this campaign"}, 404

# List monsters in campaign
class CampaignMonsterList(Resource):
    def get(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        return jsonify([monster.to_dict() for monster in campaign.monsters])

# Add Monster
class CampaignAddMonster(Resource):
    def post(self, campaign_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        data = request.get_json()

        monster_id = data.get('monster_id')
        monster = Monster.query.get_or_404(monster_id)

        if monster not in campaign.monsters:
            campaign.monsters.append(monster)
            db.session.commit()
            return {"message": "Monster added to campaign"}, 201
        else:
            return {"message": "Monster already exists in this campaign"}, 400

# Remove Monster
class CampaignRemoveMonster(Resource):
    def delete(self, campaign_id, monster_id):
        campaign = Campaign.query.get_or_404(campaign_id)
        monster = Monster.query.get_or_404(monster_id)

        if monster in campaign.monsters:
            campaign.monsters.remove(monster)
            db.session.commit()
            return {"message": "Monster removed from campaign"}, 200
        else:
            return {"message": "Monster not found in this campaign"}, 404

# Campaign Routes
campaign_api.add_resource(CampaignList, '/campaigns')
campaign_api.add_resource(CampaignDetail, '/campaigns/<int:campaign_id>')
campaign_api.add_resource(CampaignCreate, '/campaigns/new')
campaign_api.add_resource(CampaignUpdate, '/campaigns/<int:campaign_id>/update')
campaign_api.add_resource(CampaignDelete, '/campaigns/<int:campaign_id>/delete')
campaign_api.add_resource(CampaignAddCharacter, '/campaigns/<int:campaign_id>/characters/add')
campaign_api.add_resource(CampaignRemoveCharacter, '/campaigns/<int:campaign_id>/characters/<int:character_id>/remove')
campaign_api.add_resource(CampaignSessionLogs, '/campaigns/<int:campaign_id>/logs')
campaign_api.add_resource(CampaignAddSessionLog, '/campaigns/<int:campaign_id>/logs/add')
campaign_api.add_resource(CampaignHouseRules, '/campaigns/<int:campaign_id>/house_rules')
campaign_api.add_resource(CampaignSearch, '/campaigns/search')
campaign_api.add_resource(CampaignNPCList, '/campaigns/<int:campaign_id>/npcs')
campaign_api.add_resource(CampaignAddNPC, '/campaigns/<int:campaign_id>/npcs/add')
campaign_api.add_resource(CampaignRemoveNPC, '/campaigns/<int:campaign_id>/npcs/<int:npc_id>/remove')
campaign_api.add_resource(CampaignMonsterList, '/campaigns/<int:campaign_id>/monsters')
campaign_api.add_resource(CampaignAddMonster, '/campaigns/<int:campaign_id>/monsters/add')
campaign_api.add_resource(CampaignRemoveMonster, '/campaigns/<int:campaign_id>/monsters/<int:monster_id>/remove')
