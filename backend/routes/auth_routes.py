from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

from flask import request, session
from flask_restful import Resource
from models import db, User

# User Registration
class UserSignup(Resource):
    
    def post(self):
        data = request.get_json()

        if data.get('username') is not None:
            new_user = User(
                username=data.get('username'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                age=data.get('age'),
                email=data.get('email'),
            )
            new_user._password_hash = data.get('password')
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return new_user.to_dict(), 201
        else:
            return {"message": "Entry could not be processed"}, 422

# User Login
class UserLogin(Resource):
    
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data.get('email')).first()

        if user and user.check_password(data.get('password')):
            session['user_id'] = user.id
            return user.to_dict(), 200
        else:
            return {"message": "Invalid credentials"}, 401


# Get user info | Delete User
class UserProfile(Resource):
    
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.to_dict()

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        
        user.username = data.get('username', user.username)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.age = data.get('age', user.age)
        user.email = data.get('email', user.email)
        
        if 'password' in data:
            user._password_hash = data['password']

        db.session.commit()
        return user.to_dict(), 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User account deleted successfully"}, 200


