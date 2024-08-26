from flask import request, jsonify, session
from flask_restful import Resource
from models import db, Monster, HomebrewMonster, User
from utils.decorators import admin_required

# Monster list
class MonsterList(Resource):
    def get(self):
        monsters = Monster.query.all()
        return jsonify([monster.to_dict() for monster in monsters])

# Specific monster details
class MonsterDetail(Resource):
    def get(self, monster_id):
        monster = Monster.query.get_or_404(monster_id)
        return monster.to_dict()

# Create new monster
class MonsterCreate(Resource):
    @admin_required
    def post(self):
        data = request.get_json()

        new_monster = Monster(
            name=data.get('name'),
            description=data.get('description'),
            rpg_system_id=data.get('rpg_system_id'),
            size=data.get('size'),
            type=data.get('type'),
            hit_points=data.get('hit_points'),
            armor_class=data.get('armor_class'),
            challenge_rating=data.get('challenge_rating'),
            abilities=data.get('abilities', {}),
            actions=data.get('actions', {}),
            legendary_actions=data.get('legendary_actions', {}),
        )

        db.session.add(new_monster)
        db.session.commit()
        return new_monster.to_dict(), 201

# Update a monster
class MonsterUpdate(Resource):
    @admin_required
    def put(self, monster_id):
        monster = Monster.query.get_or_404(monster_id)
        data = request.get_json()

        monster.name = data.get('name', monster.name)
        monster.description = data.get('description', monster.description)
        monster.size = data.get('size', monster.size)
        monster.type = data.get('type', monster.type)
        monster.hit_points = data.get('hit_points', monster.hit_points)
        monster.armor_class = data.get('armor_class', monster.armor_class)
        monster.challenge_rating = data.get('challenge_rating', monster.challenge_rating)
        monster.abilities = data.get('abilities', monster.abilities)
        monster.actions = data.get('actions', monster.actions)
        monster.legendary_actions = data.get('legendary_actions', monster.legendary_actions)

        db.session.commit()
        return monster.to_dict(), 200

# Delete a monster
class MonsterDelete(Resource):
    @admin_required
    def delete(self, monster_id):
        monster = Monster.query.get_or_404(monster_id)
        db.session.delete(monster)
        db.session.commit()
        return {"message": "Monster deleted successfully"}, 200


# List homebrew monsters
class HomebrewMonsterList(Resource):
    def get(self):
        homebrew_monsters = HomebrewMonster.query.all()
        return jsonify([monster.to_dict() for monster in homebrew_monsters])

# Create homebrew
class HomebrewMonsterCreate(Resource):
    def post(self):
        data = request.get_json()

        new_homebrew_monster = HomebrewMonster(
            user_id=session.get('user_id'),  # Assuming the user's ID is stored in the session
            name=data.get('name'),
            description=data.get('description'),
            rpg_system_id=data.get('rpg_system_id'),
            size=data.get('size'),
            type=data.get('type'),
            hit_points=data.get('hit_points'),
            armor_class=data.get('armor_class'),
            challenge_rating=data.get('challenge_rating'),
            abilities=data.get('abilities', {}),
            actions=data.get('actions', {}),
            legendary_actions=data.get('legendary_actions', {}),
        )

        db.session.add(new_homebrew_monster)
        db.session.commit()
        return new_homebrew_monster.to_dict(), 201

# Update homebrew
class HomebrewMonsterUpdate(Resource):
    def put(self, homebrew_monster_id):
        homebrew_monster = HomebrewMonster.query.get_or_404(homebrew_monster_id)
        if homebrew_monster.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        data = request.get_json()

        homebrew_monster.name = data.get('name', homebrew_monster.name)
        homebrew_monster.description = data.get('description', homebrew_monster.description)
        homebrew_monster.size = data.get('size', homebrew_monster.size)
        homebrew_monster.type = data.get('type', homebrew_monster.type)
        homebrew_monster.hit_points = data.get('hit_points', homebrew_monster.hit_points)
        homebrew_monster.armor_class = data.get('armor_class', homebrew_monster.armor_class)
        homebrew_monster.challenge_rating = data.get('challenge_rating', homebrew_monster.challenge_rating)
        homebrew_monster.abilities = data.get('abilities', homebrew_monster.abilities)
        homebrew_monster.actions = data.get('actions', homebrew_monster.actions)
        homebrew_monster.legendary_actions = data.get('legendary_actions', homebrew_monster.legendary_actions)

        db.session.commit()
        return homebrew_monster.to_dict(), 200

# Delete homebrew
class HomebrewMonsterDelete(Resource):
    def delete(self, homebrew_monster_id):
        homebrew_monster = HomebrewMonster.query.get_or_404(homebrew_monster_id)
        if homebrew_monster.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        db.session.delete(homebrew_monster)
        db.session.commit()
        return {"message": "Homebrew monster deleted successfully"}, 200

# Search monsters
class MonsterSearch(Resource):
    def get(self):
        name = request.args.get('name')
        type = request.args.get('type')
        size = request.args.get('size')
        rpg_system_id = request.args.get('rpg_system_id')

        query = Monster.query
        if name:
            query = query.filter(Monster.name.ilike(f'%{name}%'))
        if type:
            query = query.filter_by(type=type)
        if size:
            query = query.filter_by(size=size)
        if rpg_system_id:
            query = query.filter_by(rpg_system_id=rpg_system_id)

        monsters = query.all()
        return jsonify([monster.to_dict() for monster in monsters])

# Favorite/Bookmark Monster
class MonsterBookmark(Resource):
    def post(self, monster_id):
        user_id = session.get('user_id')
        monster = Monster.query.get_or_404(monster_id)

        # Logic to add monster to the user's bookmarks
        # Assuming there's a relationship `bookmarked_monsters` on the User model
        user = User.query.get_or_404(user_id)
        if monster not in user.bookmarked_monsters:
            user.bookmarked_monsters.append(monster)
            db.session.commit()
            return {"message": "Monster bookmarked successfully"}, 200
        else:
            return {"message": "Monster already bookmarked"}, 400

# List bookmarked
class ListBookmarkedMonsters(Resource):
    def get(self):
        user_id = session.get('user_id')
        user = User.query.get_or_404(user_id)
        return jsonify([monster.to_dict() for monster in user.bookmarked_monsters])
