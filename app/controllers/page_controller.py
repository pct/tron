# app/controllers/page_controller.py
from sanic import response
from app.models.post import Post

from pprint import pprint

async def index(request):
    posts = await Post.all().values()
    #pprint(posts)
    return response.json(posts)

