# config/routes.py
from sanic import Blueprint
from app.controllers.page_controller import index

bp = Blueprint('page')

bp.add_route(index, '/')

