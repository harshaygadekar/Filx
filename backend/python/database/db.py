import sqlite3
import logging
from pathlib import Path
from contextlib import contextmanager
from config import settings

logger = logging.getLogger(__name__)
DB_PATH = settings.db_path

def get_connection():
    """Get a database connection. Prefer using get_db_connection() context manager."""
    return sqlite3.connect(DB_PATH)

@contextmanager
def get_db_connection():
    """
    Context manager for database connections.
    Automatically handles connection cleanup and error rollback.

    Usage:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(...)
            conn.commit()
    """
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        yield conn
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f"Database error: {e}")
        raise
    finally:
        if conn:
            conn.close()

def init_db():
    # BUGFIX: Use context manager to ensure connection is closed
    with get_db_connection() as conn:
        cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT UNIQUE NOT NULL,
        filename TEXT NOT NULL,
        extension TEXT,
        size INTEGER,
        created TIMESTAMP,
        modified TIMESTAMP,
        mime_type TEXT,
        hash TEXT,
        indexed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        conditions TEXT,
        actions TEXT,
        enabled BOOLEAN DEFAULT 1,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        color TEXT DEFAULT '#3B82F6',
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS file_tags (
        file_id INTEGER NOT NULL,
        tag_id INTEGER NOT NULL,
        FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
        FOREIGN KEY(tag_id) REFERENCES tags(id) ON DELETE CASCADE,
        UNIQUE(file_id, tag_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        description TEXT,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS project_files (
        project_id INTEGER NOT NULL,
        file_id INTEGER NOT NULL,
        FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE,
        FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
        UNIQUE(project_id, file_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS organization_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operation TEXT NOT NULL,
        source_path TEXT,
        dest_path TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        reversible BOOLEAN DEFAULT 1
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS file_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_id INTEGER NOT NULL,
        key TEXT NOT NULL,
        value TEXT,
        FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
        UNIQUE(file_id, key)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_preferences (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS search_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        result_count INTEGER
    )
    ''')

        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_path ON files(path)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_extension ON files(extension)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_hash ON files(hash)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_file_tags_file ON file_tags(file_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_file_tags_tag ON file_tags(tag_id)')

        # Additional indexes for common query patterns
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_mime_type ON files(mime_type)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_size ON files(size)')

    logger.info(f"Database initialized at {DB_PATH}")

if __name__ == "__main__":
    init_db()
