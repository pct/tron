# server.py
from sanic import Sanic
from config.database import DB
from config.routes import bp

app = Sanic('tron')
app.blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

