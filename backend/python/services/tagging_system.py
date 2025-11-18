import sqlite3
from typing import List, Dict, Optional
from database.db import get_connection

class TaggingSystem:
    def create_tag(self, name: str, color: str = '#3B82F6') -> Dict:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
            INSERT INTO tags (name, color)
            VALUES (?, ?)
            ''', (name, color))

            tag_id = cursor.lastrowid
            conn.commit()

            return {
                'id': tag_id,
                'name': name,
                'color': color,
            }
        except sqlite3.IntegrityError:
            return {'error': 'Tag already exists'}
        finally:
            conn.close()

    def tag_file(self, file_id: int, tag_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
            INSERT OR IGNORE INTO file_tags (file_id, tag_id)
            VALUES (?, ?)
            ''', (file_id, tag_id))

            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()

    def untag_file(self, file_id: int, tag_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
            DELETE FROM file_tags
            WHERE file_id = ? AND tag_id = ?
            ''', (file_id, tag_id))

            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()

    def get_file_tags(self, file_id: int) -> List[Dict]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT t.* FROM tags t
        JOIN file_tags ft ON t.id = ft.tag_id
        WHERE ft.file_id = ?
        ''', (file_id,))

        tags = []
        for row in cursor.fetchall():
            tags.append({
                'id': row[0],
                'name': row[1],
                'color': row[2],
            })

        conn.close()
        return tags

    def get_all_tags(self) -> List[Dict]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM tags ORDER BY name')

        tags = []
        for row in cursor.fetchall():
            tags.append({
                'id': row[0],
                'name': row[1],
                'color': row[2],
            })

        conn.close()
        return tags

    def search_by_tag(self, tag_id: int) -> List[Dict]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT f.* FROM files f
        JOIN file_tags ft ON f.id = ft.file_id
        WHERE ft.tag_id = ?
        ORDER BY f.modified DESC
        ''', (tag_id,))

        files = []
        for row in cursor.fetchall():
            files.append({
                'id': row[0],
                'path': row[1],
                'filename': row[2],
                'extension': row[3],
                'size': row[4],
                'created': row[5],
                'modified': row[6],
            })

        conn.close()
        return files

    def delete_tag(self, tag_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('DELETE FROM tags WHERE id = ?', (tag_id,))
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()

tagging_system = TaggingSystem()
