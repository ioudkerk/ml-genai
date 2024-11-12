import os
from pathlib import Path

class Config:
    # Get database path from environment variable or use default
    DB_PATH = os.environ.get('DNA_DB_PATH', 
                           os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                           'data', 'stats.db'))
    
    HOST = os.environ.get('FLASK_HOST', '127.0.0.1')
    PORT = int(os.environ.get('FLASK_PORT', 5000))
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
    
    # Ensure the directory exists
    @classmethod
    def init_db_path(cls):
        db_dir = os.path.dirname(cls.DB_PATH)
        Path(db_dir).mkdir(parents=True, exist_ok=True)
