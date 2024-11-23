from flask import Flask
import sys
import os

# Create basic Flask app first
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_123')

# Basic error handling
@app.errorhandler(500)
def server_error(e):
    return {"error": "Internal Server Error", "message": str(e)}, 500

@app.errorhandler(404)
def not_found(e):
    return {"error": "Not Found", "message": str(e)}, 404

# Test routes
@app.route('/')
def home():
    return {"message": "Hello from Flask!"}

@app.route('/test')
def test():
    return {"status": "working"}

# For Vercel
application = app

# For local testing
if __name__ == '__main__':
    app.run(debug=True)