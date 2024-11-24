from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/api/test')
def test():
    return {"status": "API is working"}