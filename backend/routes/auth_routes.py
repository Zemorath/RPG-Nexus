from flask import Blueprint, request, jsonify, session, make_response
from flask_restful import Resource, Api
from backend.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)
user_api = Api(auth_bp)


@auth_bp.route('/auth/test_session')
def test_session():
    if 'test_value' not in session:
        session['test_value'] = 0
    session['test_value'] += 1
    return jsonify({"test_value": session['test_value']})


# User Registration
class UserSignup(Resource):
    def post(self):
        data = request.get_json()
        password = data.get('password')
        if not password:
            return {"success": False, "message": "Password is required and cannot be empty."}, 400
        
        if data.get('username') is not None:
            new_user = User(
                username=data.get('username'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                age=data.get('age'),
                email=data.get('email'),
            )
            new_user.set_password(data.get('password'))
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return {"success": True, "user": new_user.to_dict()}, 201
        else:
            return {"success": False, "message": "Entry could not be processed"}, 422

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data.get('email')).first()

        if user and user.check_password(data.get('password')):
            session['user_id'] = user.id
            session.modified = True  # Ensure the session is saved
            # Return only basic user data to avoid recursion
            return {
                "success": True, 
                "user": {
                    "id": user.id, 
                    "username": user.username, 
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }
            }, 200
        else:
            return {"success": False, "message": "Invalid credentials"}, 401


# User Logout
class UserLogout(Resource):
    def delete(self):
        if not session['user_id']:
            return {"message": "Unauthorized access"}, 401
        else:
            session['user_id'] = None
            return {}, 204

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
            user.set_password(data['password'])

        db.session.commit()
        return user.to_dict(), 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User account deleted successfully"}, 200

# User authentication status
class UserAuthStatus(Resource):
    def get(self):
        user_id = session['user_id']
        # user_id = session.get('user_id')
        print(f"Session on auth status check: {session}")  # Use .get() to avoid KeyError
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            if user:
                return {"success": True, "user": user.to_dict()}, 200
            else:
                return {"success": False, "message": "User not found"}, 404
        else:
            return {"success": False, "message": "Unauthorized"}, 401



# Password reset request
class UserPasswordResetRequest(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        user = User.query.filter_by(email=email).first()

        if not user:
            return {"message": "Email not found"}, 404

        # Logic to send password reset email with token
        return {"message": "Password reset email sent"}, 200

class UserPasswordReset(Resource):
    def post(self, token):
        data = request.get_json()
        new_password = data.get('password')

        # Logic to verify token and reset password
        return {"message": "Password reset successful"}, 200

# Verification email
class UserSendVerification(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        user = User.query.filter_by(email=email).first()

        if not user:
            return {"message": "Email not found"}, 404

        # Logic to send verification email
        return {"message": "Verification email sent"}, 200

class UserVerifyAccount(Resource):
    def get(self, token):
        # Logic to verify account using token
        return {"message": "Account verified successfully"}, 200

# Update user settings
class UserSettings(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.settings

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.settings.update(data)
        db.session.commit()
        return {"message": "Settings updated"}, 200

# Auth Routes
user_api.add_resource(UserSignup, '/auth/register')
user_api.add_resource(UserLogin, '/auth/login')
user_api.add_resource(UserProfile, '/auth/profile/<int:user_id>')
user_api.add_resource(UserLogout, '/auth/logout')
user_api.add_resource(UserAuthStatus, '/auth/status')
user_api.add_resource(UserPasswordResetRequest, '/auth/password_reset_request')
user_api.add_resource(UserPasswordReset, '/auth/password_reset/<string:token>')
user_api.add_resource(UserSendVerification, '/auth/send_verification')
user_api.add_resource(UserVerifyAccount, '/auth/verify/<string:token>')
user_api.add_resource(UserSettings, '/auth/settings/<int:user_id>')
