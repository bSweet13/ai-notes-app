from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from config import config
from app.models import db
from app.routes import HealthCheck

migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)
    
    # Register resources
    api.add_resource(HealthCheck, '/health')
    
    return app
