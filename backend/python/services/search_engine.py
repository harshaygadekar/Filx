import sqlite3
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from database.db import get_connection

class SearchEngine:
    def __init__(self):
        pass

    def search(self, query: str, filters: Optional[Dict] = None) -> List[Dict]:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "SELECT * FROM files WHERE 1=1"
        params = []

        if query:
            sql += " AND (filename LIKE ? OR extension LIKE ? OR mime_type LIKE ?)"
            query_param = f"%{query}%"
            params.extend([query_param, query_param, query_param])

        if filters:
            if filters.get('file_type'):
                sql += " AND extension = ?"
                params.append(f".{filters['file_type']}")

            if filters.get('date_range'):
                date_filter = filters['date_range']
                if date_filter == 'today':
                    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                    sql += " AND modified >= ?"
                    params.append(today.isoformat())
                elif date_filter == 'week':
                    week_ago = datetime.now() - timedelta(days=7)
                    sql += " AND modified >= ?"
                    params.append(week_ago.isoformat())
                elif date_filter == 'month':
                    month_ago = datetime.now() - timedelta(days=30)
                    sql += " AND modified >= ?"
                    params.append(month_ago.isoformat())

            if filters.get('min_size'):
                sql += " AND size >= ?"
                params.append(filters['min_size'])

            if filters.get('max_size'):
                sql += " AND size <= ?"
                params.append(filters['max_size'])

        sql += " ORDER BY modified DESC LIMIT 100"

        cursor.execute(sql, params)

        results = []
        for row in cursor.fetchall():
            results.append({
                'id': row[0],
                'path': row[1],
                'filename': row[2],
                'extension': row[3],
                'size': row[4],
                'created': row[5],
                'modified': row[6],
                'mime_type': row[7],
                'hash': row[8],
            })

        conn.close()

        if query:
            self._save_search_history(query, len(results))

        return results

    def _save_search_history(self, query: str, result_count: int):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO search_history (query, result_count)
            VALUES (?, ?)
            ''', (query, result_count))
            conn.commit()
            conn.close()
        except:
            pass

    def get_recent_searches(self, limit: int = 10) -> List[Dict]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT DISTINCT query, MAX(timestamp) as last_searched, result_count
        FROM search_history
        GROUP BY query
        ORDER BY last_searched DESC
        LIMIT ?
        ''', (limit,))

        results = []
        for row in cursor.fetchall():
            results.append({
                'query': row[0],
                'last_searched': row[1],
                'result_count': row[2],
            })

        conn.close()
        return results

search_engine = SearchEngine()
