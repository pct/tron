# server.py
from sanic import Sanic
from config.database import init_orm
from config.routes import bp

app = Sanic('tron')

app.blueprint(bp)

@app.listener('before_server_start')
async def setup_db(app, loop):
    await init_orm()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

