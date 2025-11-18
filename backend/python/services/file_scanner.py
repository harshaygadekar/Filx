import os
import hashlib
import logging
from pathlib import Path
from datetime import datetime
from mimetypes import guess_type
from typing import List, Dict, Optional
import sqlite3
from database.db import get_db_connection

logger = logging.getLogger(__name__)

class FileScanner:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    def get_file_hash(self, file_path: str, chunk_size: int = 8192) -> Optional[str]:
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(chunk_size), b""):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except (IOError, OSError, PermissionError):
            return None

    def get_file_info(self, file_path: str) -> Optional[Dict]:
        try:
            stat = os.stat(file_path)
            return {
                'path': file_path,
                'filename': os.path.basename(file_path),
                'extension': os.path.splitext(file_path)[1].lower(),
                'size': stat.st_size,
                'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'mime_type': guess_type(file_path)[0] or 'unknown',
            }
        except (IOError, OSError, PermissionError):
            return None

    def scan_folder(self, folder_path: str, recursive: bool = True) -> List[Dict]:
        files = []

        if not os.path.isdir(folder_path):
            return files

        try:
            for root, dirs, filenames in os.walk(folder_path):
                if not recursive:
                    dirs.clear()

                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    file_info = self.get_file_info(file_path)

                    if file_info:
                        file_info['hash'] = self.get_file_hash(file_path)
                        files.append(file_info)

        except Exception as e:
            logger.error(f"Error scanning folder: {e}")

        return files

    def save_files_to_db(self, files: List[Dict]) -> int:
        saved_count = 0

        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                for file_info in files:
                    try:
                        cursor.execute('''
                        INSERT OR REPLACE INTO files
                        (path, filename, extension, size, created, modified, mime_type, hash)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (
                            file_info['path'],
                            file_info['filename'],
                            file_info['extension'],
                            file_info['size'],
                            file_info['created'],
                            file_info['modified'],
                            file_info['mime_type'],
                            file_info['hash'],
                        ))
                        saved_count += 1
                    except sqlite3.IntegrityError:
                        cursor.execute('''
                        UPDATE files SET
                        modified = ?, size = ?, hash = ?
                        WHERE path = ?
                        ''', (
                            file_info['modified'],
                            file_info['size'],
                            file_info['hash'],
                            file_info['path'],
                        ))
        except Exception as e:
            logger.error(f"Error saving files to database: {e}")

        return saved_count

scanner = FileScanner()
