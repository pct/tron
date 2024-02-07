from sanic import Sanic
from orator import DatabaseManager, Model
from orator.orm import belongs_to, has_many
import yaml

app = Sanic(__name__)

# Load Orator database configuration
with open('config/database.yml', 'r') as db_config_file:
    db_config = yaml.load(db_config_file, Loader=yaml.FullLoader)

db = DatabaseManager(db_config['databases'])
Model.set_connection_resolver(db)

# Import and register blueprints
from app.controllers import api_blueprint
app.blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

