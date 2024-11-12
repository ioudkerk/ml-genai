from flask import Flask
from config.settings import Config
from app.database import init_db
from app.routes import register_routes

def create_app():
    """Application factory function"""
    app = Flask(__name__)
    
    # Initialize configuration
    Config.init_db_path()
    
    # Initialize database
    init_db()
    
    # Register routes
    register_routes(app)
    
    return app
