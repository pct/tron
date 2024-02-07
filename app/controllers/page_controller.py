# app/controllers/page_controller.py
from sanic import response
from app.models.post import Post

async def index(request):
    post = Post.find(1)
    return response.html('aaa')
    #return response.json(post.serialize())

