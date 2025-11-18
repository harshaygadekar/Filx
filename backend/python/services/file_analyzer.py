import os
from pathlib import Path
from typing import Dict, List

class FileAnalyzer:
    def __init__(self):
        self.category_keywords = {
            'documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'rtf'],
            'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp', 'ico', 'tiff', 'raw'],
            'videos': ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'webm', 'mpeg', 'mpg', 'm4v'],
            'audio': ['mp3', 'wav', 'flac', 'aac', 'm4a', 'wma', 'ogg', 'opus', 'alac'],
            'archives': ['zip', '7z', 'rar', 'tar', 'gz', 'iso', 'bz2', 'xz', 'tgz'],
            'code': ['py', 'js', 'java', 'cpp', 'c', 'php', 'rb', 'go', 'rs', 'ts', 'jsx', 'tsx', 'html', 'css', 'json', 'xml', 'yaml', 'yml'],
            'executables': ['exe', 'msi', 'bat', 'cmd', 'ps1', 'sh', 'app', 'dmg'],
        }

    def get_file_category(self, file_path: str) -> str:
        ext = Path(file_path).suffix.lstrip('.').lower()

        for category, extensions in self.category_keywords.items():
            if ext in extensions:
                return category

        return 'other'

    def extract_content_preview(self, file_path: str, max_chars: int = 500) -> str:
        try:
            ext = Path(file_path).suffix.lower()

            if ext in ['.txt', '.md', '.log', '.csv', '.json', '.xml', '.py', '.js', '.html', '.css']:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read(max_chars)
        except:
            pass

        return ""

    def extract_metadata_from_content(self, file_path: str) -> Dict:
        metadata = {
            'keywords': [],
            'mentioned_dates': [],
            'mentioned_companies': [],
        }

        try:
            content = self.extract_content_preview(file_path)

            common_words = ['the', 'and', 'or', 'is', 'to', 'a', 'in', 'of', 'for', 'with', 'on', 'at', 'from', 'by', 'this', 'that']
            words = content.lower().split()
            keywords = [w for w in words if len(w) > 4 and w not in common_words]
            metadata['keywords'] = list(set(keywords[:10]))

        except:
            pass

        return metadata

    def analyze_file(self, file_path: str) -> Dict:
        return {
            'path': file_path,
            'filename': os.path.basename(file_path),
            'category': self.get_file_category(file_path),
            'content_preview': self.extract_content_preview(file_path),
            'metadata': self.extract_metadata_from_content(file_path),
        }

analyzer = FileAnalyzer()
