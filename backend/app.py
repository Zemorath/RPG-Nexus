from flask import Flask
from models import db, User, Character, Campaign, RPGSystem, Item, Skill, Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rpg_nexus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return "Welcome to RPG Nexus!"

if __name__ == '__main__':
    app.run(debug=True)
