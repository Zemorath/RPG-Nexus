from flask import request, jsonify, session, Blueprint
from flask_restful import Resource, Api
from backend.models import db, Item, User, HomebrewItem
from backend.utils.decorators import admin_required

item_bp = Blueprint('item', __name__)
item_api = Api(item_bp)

# List all items
class ItemList(Resource):
    def get(self):
        items = Item.query.all()
        return jsonify([item.to_dict() for item in items])

# Details of specific item
class ItemDetail(Resource):
    def get(self, item_id):
        item = Item.query.get_or_404(item_id)
        return item.to_dict()

# Create new item
class ItemCreate(Resource):
    @admin_required
    def post(self):
        data = request.get_json()

        new_item = Item(
            name=data.get('name'),
            description=data.get('description'),
            weight=data.get('weight'),
            rarity=data.get('rarity'),
            cost=data.get('cost'),
            damage_type=data.get('damage_type'),
            durability=data.get('durability'),
            enchantment_level=data.get('enchantment_level'),
            material=data.get('material'),
            slot_type=data.get('slot_type'),
            system_data=data.get('system_data', {}),
        )

        db.session.add(new_item)
        db.session.commit()
        return new_item.to_dict(), 201

# Update item
class ItemUpdate(Resource):
    @admin_required
    def put(self, item_id):
        item = Item.query.get_or_404(item_id)
        data = request.get_json()

        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.weight = data.get('weight', item.weight)
        item.rarity = data.get('rarity', item.rarity)
        item.cost = data.get('cost', item.cost)
        item.damage_type = data.get('damage_type', item.damage_type)
        item.durability = data.get('durability', item.durability)
        item.enchantment_level = data.get('enchantment_level', item.enchantment_level)
        item.material = data.get('material', item.material)
        item.slot_type = data.get('slot_type', item.slot_type)
        item.system_data = data.get('system_data', item.system_data)

        db.session.commit()
        return item.to_dict(), 200

# Delete an item
class ItemDelete(Resource):
    @admin_required
    def delete(self, item_id):
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted successfully"}, 200

# Search items
class ItemSearch(Resource):
    def get(self):
        name = request.args.get('name')
        rarity = request.args.get('rarity')
        material = request.args.get('material')
        rpg_system_id = request.args.get('rpg_system_id')

        query = Item.query
        if name:
            query = query.filter(Item.name.ilike(f'%{name}%'))
        if rarity:
            query = query.filter_by(rarity=rarity)
        if material:
            query = query.filter_by(material=material)
        if rpg_system_id:
            query = query.filter(Item.system_data['rpg_system_id'].astext == str(rpg_system_id))

        items = query.all()
        return jsonify([item.to_dict() for item in items])

# List items by RPG 
class ItemByRPGSystem(Resource):
    def get(self, rpg_system_id):
        items = Item.query.filter(Item.system_data['rpg_system_id'].astext == str(rpg_system_id)).all()
        return jsonify([item.to_dict() for item in items])

# Bookmark item
class ItemBookmark(Resource):
    def post(self, item_id):
        user_id = session.get('user_id')
        item = Item.query.get_or_404(item_id)

        # Assuming there's a relationship `bookmarked_items` on the User model
        user = User.query.get_or_404(user_id)
        if item not in user.bookmarked_items:
            user.bookmarked_items.append(item)
            db.session.commit()
            return {"message": "Item bookmarked successfully"}, 200
        else:
            return {"message": "Item already bookmarked"}, 400
        
# Unbookmark item
class ItemUnbookmark(Resource):
    def delete(self, item_id):
        user_id = session.get('user_id')
        item = Item.query.get_or_404(item_id)

        # Assuming there's a relationship `bookmarked_items` on the User model
        user = User.query.get_or_404(user_id)
        if item in user.bookmarked_items:
            user.bookmarked_items.remove(item)
            db.session.commit()
            return {"message": "Item unbookmarked successfully"}, 200
        else:
            return {"message": "Item not bookmarked"}, 400

# List Bookmarked items
class ListBookmarkedItems(Resource):
    def get(self):
        user_id = session.get('user_id')
        user = User.query.get_or_404(user_id)
        return jsonify([item.to_dict() for item in user.bookmarked_items])

# List homebrew
class HomebrewItemList(Resource):
    def get(self):
        homebrew_items = HomebrewItem.query.all()
        return jsonify([item.to_dict() for item in homebrew_items])

# Create homebrew
class HomebrewItemCreate(Resource):
    def post(self):
        data = request.get_json()

        new_homebrew_item = HomebrewItem(
            user_id=session.get('user_id'),  # Assuming the user's ID is stored in the session
            name=data.get('name'),
            description=data.get('description'),
            weight=data.get('weight'),
            rarity=data.get('rarity'),
            cost=data.get('cost'),
            damage_type=data.get('damage_type'),
            durability=data.get('durability'),
            enchantment_level=data.get('enchantment_level'),
            material=data.get('material'),
            slot_type=data.get('slot_type'),
            system_data=data.get('system_data', {}),
        )

        db.session.add(new_homebrew_item)
        db.session.commit()
        return new_homebrew_item.to_dict(), 201

# Update homebrew
class HomebrewItemUpdate(Resource):
    def put(self, homebrew_item_id):
        homebrew_item = HomebrewItem.query.get_or_404(homebrew_item_id)
        if homebrew_item.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        data = request.get_json()

        homebrew_item.name = data.get('name', homebrew_item.name)
        homebrew_item.description = data.get('description', homebrew_item.description)
        homebrew_item.weight = data.get('weight', homebrew_item.weight)
        homebrew_item.rarity = data.get('rarity', homebrew_item.rarity)
        homebrew_item.cost = data.get('cost', homebrew_item.cost)
        homebrew_item.damage_type = data.get('damage_type', homebrew_item.damage_type)
        homebrew_item.durability = data.get('durability', homebrew_item.durability)
        homebrew_item.enchantment_level = data.get('enchantment_level', homebrew_item.enchantment_level)
        homebrew_item.material = data.get('material', homebrew_item.material)
        homebrew_item.slot_type = data.get('slot_type', homebrew_item.slot_type)
        homebrew_item.system_data = data.get('system_data', homebrew_item.system_data)

        db.session.commit()
        return homebrew_item.to_dict(), 200

# Delete homebrew
class HomebrewItemDelete(Resource):
    def delete(self, homebrew_item_id):
        homebrew_item = HomebrewItem.query.get_or_404(homebrew_item_id)
        if homebrew_item.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        db.session.delete(homebrew_item)
        db.session.commit()
        return {"message": "Homebrew item deleted successfully"}, 200

# Export homebrew
class HomebrewItemExport(Resource):
    def get(self, homebrew_item_id):
        homebrew_item = HomebrewItem.query.get_or_404(homebrew_item_id)
        if homebrew_item.user_id != session.get('user_id'):
            return {"message": "Unauthorized"}, 403

        # Return the item data as JSON for export
        return jsonify(homebrew_item.to_dict())

# Import homebrew
class HomebrewItemImport(Resource):
    def post(self):
        data = request.get_json()

        imported_item = HomebrewItem(
            user_id=session.get('user_id'),
            name=data.get('name'),
            description=data.get('description'),
            weight=data.get('weight'),
            rarity=data.get('rarity'),
            cost=data.get('cost'),
            damage_type=data.get('damage_type'),
            durability=data.get('durability'),
            enchantment_level=data.get('enchantment_level'),
            material=data.get('material'),
            slot_type=data.get('slot_type'),
            system_data=data.get('system_data', {}),
        )

        db.session.add(imported_item)
        db.session.commit()
        return imported_item.to_dict(), 201

# Item Management Routes
item_api.add_resource(ItemList, '/items')
item_api.add_resource(ItemDetail, '/items/<int:item_id>')
item_api.add_resource(ItemCreate, '/items/new')
item_api.add_resource(ItemUpdate, '/items/<int:item_id>/update')
item_api.add_resource(ItemDelete, '/items/<int:item_id>/delete')
item_api.add_resource(ItemSearch, '/items/search')
item_api.add_resource(ItemByRPGSystem, '/items/rpgsystem/<int:rpg_system_id>')
item_api.add_resource(ItemBookmark, '/items/<int:item_id>/bookmark')
item_api.add_resource(ItemUnbookmark, '/items/<int:item_id>/unbookmark')
item_api.add_resource(ListBookmarkedItems, '/items/bookmarks')
item_api.add_resource(HomebrewItemList, '/homebrew/items')
item_api.add_resource(HomebrewItemCreate, '/homebrew/items/new')
item_api.add_resource(HomebrewItemUpdate, '/homebrew/items/<int:homebrew_item_id>/update')
item_api.add_resource(HomebrewItemDelete, '/homebrew/items/<int:homebrew_item_id>/delete')
item_api.add_resource(HomebrewItemExport, '/homebrew/items/<int:homebrew_item_id>/export')
item_api.add_resource(HomebrewItemImport, '/homebrew/items/import')