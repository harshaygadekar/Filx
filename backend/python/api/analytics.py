from fastapi import APIRouter, HTTPException
from database.db import get_connection
from collections import defaultdict

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/stats")
async def get_stats():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*), SUM(size) FROM files")
        total_files, total_size = cursor.fetchone()
        total_files = total_files or 0
        total_size = total_size or 0

        cursor.execute("""
        SELECT hash, COUNT(*) as count, size
        FROM files
        WHERE hash IS NOT NULL AND hash != ''
        GROUP BY hash
        HAVING COUNT(*) > 1
        """)
        duplicate_data = cursor.fetchall()
        duplicate_count = sum(count - 1 for _, count, _ in duplicate_data)
        duplicate_size = sum((count - 1) * size for _, count, size in duplicate_data)

        conn.close()

        storage_gb = total_size / (1024 ** 3)
        duplicate_gb = duplicate_size / (1024 ** 3)

        organization_score = min(100, max(0, 100 - (duplicate_count * 2)))

        return {
            "totalFiles": total_files,
            "storageUsed": f"{storage_gb:.2f} GB",
            "organizationScore": organization_score,
            "duplicatesFound": duplicate_count,
            "duplicateSize": f"{duplicate_gb:.2f} GB",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/distribution")
async def get_file_distribution():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT extension, COUNT(*), SUM(size) FROM files GROUP BY extension")

        category_map = {
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
            'videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.m4a'],
            'archives': ['.zip', '.7z', '.rar', '.tar', '.gz'],
            'code': ['.py', '.js', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.ts', '.html', '.css'],
        }

        distribution = defaultdict(lambda: {'count': 0, 'size': 0})

        for ext, count, size in cursor.fetchall():
            ext = ext or ''
            size = size or 0
            category = 'other'

            for cat, extensions in category_map.items():
                if ext.lower() in extensions:
                    category = cat
                    break

            distribution[category]['count'] += count
            distribution[category]['size'] += size

        conn.close()

        result = []
        for category, data in distribution.items():
            result.append({
                'name': category.capitalize(),
                'count': data['count'],
                'size': data['size'],
                'size_gb': data['size'] / (1024 ** 3)
            })

        return {
            "distribution": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
