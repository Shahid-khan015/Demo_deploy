from flask import Flask

def create_app():
    app = Flask(__name__)
    # Your app configuration and blueprints registration here
    return app

