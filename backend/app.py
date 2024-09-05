import os
from backend import create_app

app = create_app()

# Set FLASK_ENV directly in app
os.environ['FLASK_ENV'] = 'development'

@app.route('/test')
def test():
    return {'message': 'API is working!'}

if __name__ == "__main__":
    app.run(port=5555, debug=True)
