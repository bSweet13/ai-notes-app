from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    from app.routes import HealthCheck
    api.add_resource(HealthCheck, '/health')
    
    return app
