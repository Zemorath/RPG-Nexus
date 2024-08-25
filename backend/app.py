from flask import Flask
from flask_restful import Api
from routes.auth_routes import UserSignup, UserLogin, UserProfile
from routes.character_routes import CharacterList, CharacterDetail

app = Flask(__name__)
api = Api(app)

# Defined routes

# User Routes from auth_routes.py
api.add_resource(UserSignup, '/api/auth/register')
api.add_resource(UserLogin, '/api/auth/login')
api.add_resource(UserProfile, '/api/auth/profile/<int:user_id>')

# Character routes from character_routes.py
api.add_resource(CharacterList, '/api/characters')
api.add_resource(CharacterDetail, '/api/characters/<int:character_id>')



if __name__ == '__main__':
    app.run(debug=True)

