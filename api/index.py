from flask import Flask
from website import create_app

# Create the Flask app
app = create_app()
app.secret_key = '12@#!_#SD'

# Add a base route handler
@app.route('/')
def home():
    return {"message": "Flask API is running"}

# Add your test route
@app.route('/test')
def test():
    return {"status": "working"}

# This is required for Vercel
app.debug = False

# Handle all routes
@app.route('/<path:path>')
def catch_all(path):
    return {"message": f"Route '{path}' not found"}, 404