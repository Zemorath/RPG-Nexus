from flask import request, jsonify, session, Blueprint
from flask_restful import Resource, Api
from backend.models import db, NPC, HomebrewNPC, User
from backend.utils.decorators import admin_required

npc_bp = Blueprint('npc', __name__)
npc_api = Api(npc_bp)

# List NPCs
class NPCList(Resource):
    def get(self):
        npcs = NPC.query.all()
        return jsonify([npc.to_dict() for npc in npcs])

# Search NPCs
class NPCSearch(Resource):
    def get(self):
        name = request.args.get('name')
        role = request.args.get('role')
        alignment = request.args.get('alignment')
        rpg_system_id = request.args.get('rpg_system_id')

        query = NPC.query
        if name:
            query = query.filter(NPC.name.ilike(f'%{name}%'))
        if role:
            query = query.filter_by(role=role)
        if alignment:
            query = query.filter_by(alignment=alignment)
        if rpg_system_id:
            query = query.filter_by(rpg_system_id=rpg_system_id)

        npcs = query.all()
        return jsonify([npc.to_dict() for npc in npcs])

    
# Details of specific NPC
class NPCDetail(Resource):
    def get(self, npc_id):
        npc = NPC.query.get_or_404(npc_id)
        return npc.to_dict()

# Favorite/Bookmark NPC
class NPCBookmark(Resource):
    def post(self, npc_id):
        user_id = session.get('user_id')
        npc = NPC.query.get_or_404(npc_id)

        # Logic to add NPC to the user's bookmarks
        # Assuming there's a relationship `bookmarked_npcs` on the User model
        user = User.query.get_or_404(user_id)
        if npc not in user.bookmarked_npcs:
            user.bookmarked_npcs.append(npc)
            db.session.commit()
            return {"message": "NPC bookmarked successfully"}, 200
        else:
            return {"message": "NPC already bookmarked"}, 400

class ListBookmarkedNPCs(Resource):
    def get(self):
        user_id = session.get('user_id')
        user = User.query.get_or_404(user_id)
        return jsonify([npc.to_dict() for npc in user.bookmarked_npcs])

# Create NPC
class NPCCreate(Resource):
    @admin_required
    def post(self):
        data = request.get_json()

        new_npc = NPC(
            name=data.get('name'),
            description=data.get('description'),
            rpg_system_id=data.get('rpg_system_id'),
            role=data.get('role'),
            alignment=data.get('alignment'),
            abilities=data.get('abilities', {}),
            inventory=data.get('inventory', {}),
            motivations=data.get('motivations', {}),
        )

        db.session.add(new_npc)
        db.session.commit()
        return new_npc.to_dict(), 201

# Update NPC
class NPCUpdate(Resource):
    @admin_required
    def put(self, npc_id):
        npc = NPC.query.get_or_404(npc_id)
        data = request.get_json()

        npc.name = data.get('name', npc.name)
        npc.description = data.get('description', npc.description)
        npc.role = data.get('role', npc.role)
        npc.alignment = data.get('alignment', npc.alignment)
        npc.abilities = data.get('abilities', npc.abilities)
        npc.inventory = data.get('inventory', npc.inventory)
        npc.motivations = data.get('motivations', npc.motivations)

        db.session.commit()
        return npc.to_dict(), 200

# Delete NPC
class NPCDelete(Resource):
    @admin_required
    def delete(self, npc_id):
        npc = NPC.query.get_or_404(npc_id)
        db.session.delete(npc)
        db.session.commit()
        return {"message": "NPC deleted successfully"}, 200

# List Homebrew NPCs
class HomebrewNPCList(Resource):
    def get(self):
        homebrew_npcs = HomebrewNPC.query.all()
        return jsonify([npc.to_dict() for npc in homebrew_npcs])

# Create Homebrew NPC
class HomebrewNPCCreate(Resource):
    def post(self):
        data = request.get_json()

        new_homebrew_npc = HomebrewNPC(
            user_id=session.get('user_id'),  # Assuming the user's ID is stored in the session
            name=data.get('name'),
            description=data.get('description'),
            rpg_system_id=data.get('rpg_system_id'),
            role=data.get('role'),
            alignment=data.get('alignment'),
            abilities=data.get('abilities', {}),
            inventory=data.get('inventory', {}),
            motivations=data.get('motivations', {}),
        )

        db.session.add(new_homebrew_npc)
        db.session.commit()
        return new_homebrew_npc.to_dict(), 201

# Update homebrew
class HomebrewNPCUpdate(Resource):
    def put(self, homebrew_npc_id):
        homebrew_npc = HomebrewNPC.query.get_or_404(homebrew_npc_id)
        if homebrew_npc.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        data = request.get_json()

        homebrew_npc.name = data.get('name', homebrew_npc.name)
        homebrew_npc.description = data.get('description', homebrew_npc.description)
        homebrew_npc.role = data.get('role', homebrew_npc.role)
        homebrew_npc.alignment = data.get('alignment', homebrew_npc.alignment)
        homebrew_npc.abilities = data.get('abilities', homebrew_npc.abilities)
        homebrew_npc.inventory = data.get('inventory', homebrew_npc.inventory)
        homebrew_npc.motivations = data.get('motivations', homebrew_npc.motivations)

        db.session.commit()
        return homebrew_npc.to_dict(), 200

# Delete homebrew
class HomebrewNPCDelete(Resource):
    def delete(self, homebrew_npc_id):
        homebrew_npc = HomebrewNPC.query.get_or_404(homebrew_npc_id)
        if homebrew_npc.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        db.session.delete(homebrew_npc)
        db.session.commit()
        return {"message": "Homebrew NPC deleted successfully"}, 200
    
# Import NPCs
class NPCImport(Resource):
    def post(self):
        data = request.get_json()

        # Logic to import NPC from an external source or a file
        imported_npc = NPC(
            name=data.get('name'),
            description=data.get('description'),
            rpg_system_id=data.get('rpg_system_id'),
            role=data.get('role'),
            alignment=data.get('alignment'),
            abilities=data.get('abilities', {}),
            inventory=data.get('inventory', {}),
            motivations=data.get('motivations', {}),
        )

        db.session.add(imported_npc)
        db.session.commit()
        return imported_npc.to_dict(), 201

# NPC Routes
npc_api.add_resource(NPCList, '/npcs')
npc_api.add_resource(NPCDetail, '/npcs/<int:npc_id>')
npc_api.add_resource(NPCCreate, '/npcs/new')
npc_api.add_resource(NPCUpdate, '/npcs/<int:npc_id>/update')
npc_api.add_resource(NPCDelete, '/npcs/<int:npc_id>/delete')
npc_api.add_resource(NPCSearch, '/npcs/search')
npc_api.add_resource(HomebrewNPCList, '/homebrew/npcs')
npc_api.add_resource(HomebrewNPCCreate, '/homebrew/npcs/new')
npc_api.add_resource(HomebrewNPCUpdate, '/homebrew/npcs/<int:homebrew_npc_id>/update')
npc_api.add_resource(HomebrewNPCDelete, '/homebrew/npcs/<int:homebrew_npc_id>/delete')
npc_api.add_resource(NPCBookmark, '/npcs/<int:npc_id>/bookmark')
npc_api.add_resource(ListBookmarkedNPCs, '/npcs/bookmarks')
npc_api.add_resource(NPCImport, '/npcs/import')