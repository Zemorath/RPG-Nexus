from flask import request, jsonify, Blueprint
from flask_restful import Resource, Api
from backend.models import db, RPGSystem
from backend.utils.decorators import admin_required

rpgsystem_bp = Blueprint('rpgsystem', __name__, url_prefix='/api')
rpgsystem_api = Api(rpgsystem_bp)

# List of all RPGs
class RPGSystemList(Resource):
    def get(self):
        rpg_systems = RPGSystem.query.all()
        return jsonify([rpg_system.to_dict() for rpg_system in rpg_systems])

# Details of specific RPG
class RPGSystemDetail(Resource):
    def get(self, rpg_system_id):
        rpg_system = RPGSystem.query.get_or_404(rpg_system_id)
        return rpg_system.to_dict()


# Create new RPG System
class RPGSystemCreate(Resource):
    @admin_required
    def post(self):
        data = request.get_json()

        new_rpg_system = RPGSystem(
            name=data.get('name'),
            description=data.get('description'),
            publisher=data.get('publisher'),
            edition=data.get('edition'),
            core_rulebook=data.get('core_rulebook'),
            genre=data.get('genre'),
            popularity=data.get('popularity', 0),
            default_settings=data.get('default_settings', {})
        )

        db.session.add(new_rpg_system)
        db.session.commit()
        return new_rpg_system.to_dict(), 201


# Update existing RPG
class RPGSystemUpdate(Resource):
    @admin_required
    def put(self, rpg_system_id):
        rpg_system = RPGSystem.query.get_or_404(rpg_system_id)
        data = request.get_json()

        rpg_system.name = data.get('name', rpg_system.name)
        rpg_system.description = data.get('description', rpg_system.description)
        rpg_system.publisher = data.get('publisher', rpg_system.publisher)
        rpg_system.edition = data.get('edition', rpg_system.edition)
        rpg_system.core_rulebook = data.get('core_rulebook', rpg_system.core_rulebook)
        rpg_system.genre = data.get('genre', rpg_system.genre)
        rpg_system.popularity = data.get('popularity', rpg_system.popularity)
        rpg_system.default_settings = data.get('default_settings', rpg_system.default_settings)

        db.session.commit()
        return rpg_system.to_dict(), 200

# Delete RPG
class RPGSystemDelete(Resource):
    @admin_required
    def delete(self, rpg_system_id):
        rpg_system = RPGSystem.query.get_or_404(rpg_system_id)
        db.session.delete(rpg_system)
        db.session.commit()
        return {"message": "RPG system deleted successfully"}, 200

# Search for RPG
class RPGSystemSearch(Resource):
    def get(self):
        name = request.args.get('name')
        genre = request.args.get('genre')
        publisher = request.args.get('publisher')

        query = RPGSystem.query
        if name:
            query = query.filter(RPGSystem.name.ilike(f'%{name}%'))
        if genre:
            query = query.filter_by(genre=genre)
        if publisher:
            query = query.filter_by(publisher=publisher)

        rpg_systems = query.all()
        return jsonify([rpg_system.to_dict() for rpg_system in rpg_systems])
    
# Get sorted RPG systems by popularity
class RPGSystemPopular(Resource):
    def get(self):
        rpg_systems = RPGSystem.query.order_by(RPGSystem.popularity.desc()).limit(10).all()
        return jsonify([rpg_system.to_dict() for rpg_system in rpg_systems])
    
class RPGSystemDefaultSettings(Resource):
    def get(self, rpg_system_id):
        rpg_system = RPGSystem.query.get_or_404(rpg_system_id)
        return jsonify(rpg_system.default_settings)


# RPG System Routes
rpgsystem_api.add_resource(RPGSystemList, '/rpgsystems')
rpgsystem_api.add_resource(RPGSystemDetail, '/rpgsystems/<int:rpg_system_id>')
rpgsystem_api.add_resource(RPGSystemCreate, '/rpgsystems/new')
rpgsystem_api.add_resource(RPGSystemUpdate, '/rpgsystems/<int:rpg_system_id>/update')
rpgsystem_api.add_resource(RPGSystemDelete, '/rpgsystems/<int:rpg_system_id>/delete')
rpgsystem_api.add_resource(RPGSystemSearch, '/rpgsystems/search')
rpgsystem_api.add_resource(RPGSystemPopular, '/rpgsystems/popular')
rpgsystem_api.add_resource(RPGSystemDefaultSettings, '/rpgsystems/<int:rpg_system_id>/default_settings')