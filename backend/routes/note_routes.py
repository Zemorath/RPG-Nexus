from flask import request, jsonify, session, Blueprint
from flask_restful import Resource, Api
from backend.models import db, Note, User

note_bp = Blueprint('note', __name__)
note_api = Api(note_bp)

# Note list
class NoteList(Resource):
    def get(self):
        notes = Note.query.all()
        return jsonify([note.to_dict() for note in notes])

# Details of specific note
class NoteDetail(Resource):
    def get(self, note_id):
        note = Note.query.get_or_404(note_id)
        return note.to_dict()

# Create new note
class NoteCreate(Resource):
    def post(self):
        data = request.get_json()

        new_note = Note(
            title=data.get('title'),
            content=data.get('content'),
            character_id=data.get('character_id'),
            campaign_id=data.get('campaign_id'),
            type=data.get('type'),
            tags=data.get('tags', []),
            created_by=session.get('user_id'),  # Assuming the user's ID is stored in the session
        )

        db.session.add(new_note)
        db.session.commit()
        return new_note.to_dict(), 201

# Update note
class NoteUpdate(Resource):
    def put(self, note_id):
        note = Note.query.get_or_404(note_id)
        data = request.get_json()

        note.title = data.get('title', note.title)
        note.content = data.get('content', note.content)
        note.type = data.get('type', note.type)
        note.tags = data.get('tags', note.tags)

        db.session.commit()
        return note.to_dict(), 200

# Delete note
class NoteDelete(Resource):
    def delete(self, note_id):
        note = Note.query.get_or_404(note_id)
        db.session.delete(note)
        db.session.commit()
        return {"message": "Note deleted successfully"}, 200

# Search note
class NoteSearch(Resource):
    def get(self):
        title = request.args.get('title')
        tags = request.args.getlist('tags')
        type = request.args.get('type')
        character_id = request.args.get('character_id')
        campaign_id = request.args.get('campaign_id')

        query = Note.query
        if title:
            query = query.filter(Note.title.ilike(f'%{title}%'))
        if tags:
            for tag in tags:
                query = query.filter(Note.tags.contains([tag]))
        if type:
            query = query.filter_by(type=type)
        if character_id:
            query = query.filter_by(character_id=character_id)
        if campaign_id:
            query = query.filter_by(campaign_id=campaign_id)

        notes = query.all()
        return jsonify([note.to_dict() for note in notes])

# Share note
class NoteShare(Resource):
    def post(self, note_id):
        note = Note.query.get_or_404(note_id)
        data = request.get_json()

        shared_with = data.get('shared_with')
        # Logic to share the note (e.g., adding to a shared_with field or sending a notification)

        note.shared_with.extend(shared_with)
        db.session.commit()

        return {"message": "Note shared successfully"}, 200

# Note Routes
note_api.add_resource(NoteList, '/notes')
note_api.add_resource(NoteDetail, '/notes/<int:note_id>')
note_api.add_resource(NoteCreate, '/notes/new')
note_api.add_resource(NoteUpdate, '/notes/<int:note_id>/update')
note_api.add_resource(NoteDelete, '/notes/<int:note_id>/delete')
note_api.add_resource(NoteSearch, '/notes/search')
note_api.add_resource(NoteShare, '/notes/<int:note_id>/share')