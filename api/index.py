from flask import Flask
from website import create_app

app = create_app()
app.secret_key = '12@#!_#SD'

# Add error handlers
@app.errorhandler(404)
def not_found_error(error):
    return {"error": "Not Found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal Server Error"}, 500