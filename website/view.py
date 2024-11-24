# website/view.py
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return {"message": "Welcome to the home page"}
