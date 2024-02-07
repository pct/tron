# app/controllers.py
from sanic import Blueprint, response
from app.models.user import User

api_blueprint = Blueprint('api')

@api_blueprint.route('/users', methods=['GET'])
async def list_users(request):
    users = User.all().serialize()
    return response.json({'users': users})

@api_blueprint.route('/users', methods=['POST'])
async def add_user(request):
    user_data = request.json
    user = User.create(**user_data)
    return response.json(user.serialize(), status=201)

