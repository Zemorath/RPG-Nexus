from functools import wraps
from flask import request, jsonify, session
from models import User

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id is None:
            return jsonify({"message": "Unauthorized access"}), 401
        
        user = User.query.get(user_id)
        if user is None or not user.is_admin:
            return jsonify({"message": "Admin access required"}), 403
        
        return f(*args, **kwargs)
    return decorated_function
