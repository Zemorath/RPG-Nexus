# app.py
from __init__ import create_app  # Import your factory function
from flask import jsonify

app = create_app()

# Add a simple route to test
@app.route('/test')
def test():
    return jsonify({'message': 'API is working!'})

@app.route('/db_check')
def db_check():
    return jsonify({"database": app.config['SQLALCHEMY_DATABASE_URI']})


if __name__ == "__main__":
    app.run(port=5555, debug=True)
