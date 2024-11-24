# api/index.py
from flask import Flask
from website import create_app

app = create_app()

# Handle WSGI requirements for Vercel
app.secret_key = '12@#!_#SD'

# Add error handling
@app.errorhandler(500)
def server_error(e):
    return {"error": "Internal server error"}, 500

@app.errorhandler(404)
def not_found(e):
    return {"error": "Resource not found"}, 404

# Add a health check endpoint
@app.route('/api/health')
def health_check():
    return {"status": "healthy"}