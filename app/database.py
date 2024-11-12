import sqlite3
import json
from contextlib import contextmanager
from typing import Optional
from config.settings import Config

@contextmanager
def get_db_connection():
    """Context manager for database connections"""
    conn = None
    try:
        conn = sqlite3.connect(Config.DB_PATH)
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        if conn:
            conn.close()

def init_db():
    """Initialize database with required tables"""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.executescript('''
            BEGIN;
            CREATE TABLE IF NOT EXISTS api_stats
                (status TEXT PRIMARY KEY, count INTEGER);
            CREATE TABLE IF NOT EXISTS dna_cache
                (dna TEXT PRIMARY KEY, result BOOLEAN, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
            INSERT OR IGNORE INTO api_stats (status, count) VALUES ('mutant', 0);
            INSERT OR IGNORE INTO api_stats (status, count) VALUES ('human', 0);
            COMMIT;
        ''')

def update_stats(status: str) -> None:
    """Update statistics for DNA checks"""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("UPDATE api_stats SET count = count + 1 WHERE status = ?", (status,))
        conn.commit()

def check_cache(dna: list) -> Optional[bool]:
    """Check if DNA sequence exists in cache"""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT result FROM dna_cache WHERE dna = ?", (json.dumps(dna),))
        result = c.fetchone()
        return result[0] if result else None

def update_cache(dna: list, is_mutant: bool) -> None:
    """Update cache with new DNA sequence result"""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute(
            "INSERT OR REPLACE INTO dna_cache (dna, result) VALUES (?, ?)", 
            (json.dumps(dna), is_mutant)
        )
        conn.commit()

def get_dna_stats():
    """Get DNA statistics from database"""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT status, count FROM api_stats")
        return dict(c.fetchall())
