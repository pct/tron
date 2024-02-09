from tortoise import Tortoise, fields
from tortoise.models import Model

class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    content = fields.TextField()
