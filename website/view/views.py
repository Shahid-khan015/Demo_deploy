

# /website/view/views.py
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "Welcome to the homepage!"
