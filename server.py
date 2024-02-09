# server.py
from sanic import Sanic
#from config.database import DB
from tortoise import Tortoise
from config.routes import bp

app = Sanic('tron')

app.blueprint(bp)

async def init_orm():
    await Tortoise.init(
        db_url='mysql://root@127.0.0.1:3306/tron',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()

@app.listener('before_server_start')
async def setup_db(app, loop):
    await init_orm()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

