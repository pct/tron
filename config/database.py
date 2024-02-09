from tortoise import Tortoise

async def init_orm():
    await Tortoise.init(
        db_url='mysql://root@127.0.0.1:3306/tron',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()

