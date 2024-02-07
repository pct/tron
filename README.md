# Tron (todo)

## Sanic framework with rails like orm

- Main: Sanic
- ORM: Masonite Orm
- Template: Jinja2

## Install

    $ pip install sanic masonite-orm PyYAML PyMySQL


## DB Migrate



## Doc

    from app.models.post import Post

    # Create a new post
    new_post = Post.create(title='My First Post', content='This is the content of my first post.')

    posts = Post.all()
    post = Post.find(1)

    # Update
    post.update(title='Updated Title', content='Updated content of the post.')

    # Delete a post
    post = Post.find(1)
    post.delete()

    # Soft delete, if SoftDeletesMixin is used
    post.soft_delete()

