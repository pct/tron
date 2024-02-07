from masoniteorm.models import Model

class Post(Model):
    """A simple blog post model."""
    __fillable__ = ['title', 'content']  # Fields that can be mass assigned
    __dates__ = ['created_at', 'updated_at', 'deleted_at']  # Handle datetime conversion and soft deletes

