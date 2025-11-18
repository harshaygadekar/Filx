import sqlite3
from typing import Dict, List
from database.db import get_connection

class DuplicateFinder:
    def find_duplicates(self) -> Dict:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT hash, COUNT(*) as count
        FROM files
        WHERE hash IS NOT NULL AND hash != ''
        GROUP BY hash
        HAVING COUNT(*) > 1
        ORDER BY count DESC
        ''')

        duplicates = {}
        total_wasted = 0
        total_duplicates = 0

        for hash_val, count in cursor.fetchall():
            cursor.execute('''
            SELECT * FROM files WHERE hash = ?
            ORDER BY modified DESC
            ''', (hash_val,))

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

            if files:
                wasted = files[0]['size'] * (count - 1)
                total_wasted += wasted
                total_duplicates += count - 1

                duplicates[hash_val] = {
                    'count': count,
                    'files': files,
                    'wasted_space': wasted,
                }

        conn.close()

        return {
            'duplicates': duplicates,
            'total_duplicate_count': total_duplicates,
            'total_wasted_space': total_wasted,
            'duplicate_groups': len(duplicates),
        }

    def delete_duplicates(self, file_ids: List[int]) -> Dict:
        conn = get_connection()
        cursor = conn.cursor()

        deleted_count = 0
        errors = []

        for file_id in file_ids:
            try:
                cursor.execute('SELECT path FROM files WHERE id = ?', (file_id,))
                result = cursor.fetchone()

                if result:
                    import os
                    file_path = result[0]

                    if os.path.exists(file_path):
                        os.remove(file_path)

                    cursor.execute('DELETE FROM files WHERE id = ?', (file_id,))
                    deleted_count += 1

            except Exception as e:
                errors.append({
                    'file_id': file_id,
                    'error': str(e)
                })

        conn.commit()
        conn.close()

        return {
            'deleted_count': deleted_count,
            'errors': errors,
        }

duplicate_finder = DuplicateFinder()
