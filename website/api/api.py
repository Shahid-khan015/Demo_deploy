# /website/api/api.py
from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/data')
def get_data():
    return jsonify({"message": "This is an API response"})
