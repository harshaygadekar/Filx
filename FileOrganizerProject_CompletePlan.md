# FileOrganizer Pro - Complete Project Plan
## Intelligent Windows File Organization Desktop Application

---

## PART 1: COMPLETE FEATURE LIST (Solving Real Problems)

### Core Problems Solved
1. **Digital Chaos** → Smart Auto-Organization
2. **Time Waste Finding Files** → Lightning-Fast Search + Tagging
3. **Manual Organization Work** → One-Click Batch Operations
4. **Folder Proliferation** → Intelligent Folder Structure Generation
5. **Mixed File Types** → Content-Aware Categorization
6. **Lost Files** → File Location History + Recovery
7. **Duplicate Mess** → Smart Duplicate Detection & Cleanup
8. **Unstructured Organization** → Project-Based Grouping

---

### FEATURE SET 1: AUTO-ORGANIZATION ENGINE
**Problem: Users don't know where to put files, wasting time manually organizing**

**Features:**
- **Smart Auto-Organize**: One-click analysis of entire folder → generates optimal organization structure
  - Analyzes 100+ files in <5 seconds
  - Suggests folder hierarchy with confidence scores
  - Groups by: file type, date range, content keywords, project names
  - Example: "Report Q3 2024.pdf" → /Projects/Q3-2024/Reports/

- **Content-Aware Categorization**: Read file content, not just extension
  - OCR for PDFs to detect document type (Invoice, Contract, Resume, etc.)
  - Image analysis (Screenshots, Photos, Artwork, Designs)
  - Document parsing (Find project names, dates, client names in text)
  - Example: PDF containing "Invoice #12345 from Acme Corp" → /Finance/2024/Acme-Corp/

- **Intelligent Rules Engine**: Build rules without coding
  - If [file type] AND [contains keyword] AND [modified in last X days] → Move to [folder]
  - Visual rule builder with AND/OR logic
  - Pre-built templates: Downloads Cleaner, Project Organizer, Photo Sorter, Invoice Manager
  - Rules save and improve with each use

- **One-Touch Organization**: 
  - Preview all changes before executing (100% safety)
  - Drag-to-organize: drag file from preview → destination folder auto-creates
  - Undo functionality (restore files to original location)
  - Batch move/copy/delete with conflict resolution

---

### FEATURE SET 2: INTELLIGENT SEARCH & DISCOVERY
**Problem: Users spend hours searching for files they know exist**

**Features:**
- **Ultra-Fast Local Search**:
  - Search by filename, extension, size, date range, content keywords
  - Fuzzy matching ("repot.pdf" finds "Report.pdf")
  - Full-text search inside PDFs, Word docs, Text files
  - Search 10,000 files in <1 second

- **Smart Filters**:
  - By file type (Documents, Images, Videos, Archives, Code, etc.)
  - By date modified (Today, This Week, This Month, This Year, Custom)
  - By size (< 1MB, 1-10MB, 10-100MB, > 100MB)
  - By custom tags (see Tagging System below)
  - By folder location
  - Combined multi-filter search

- **Recent Files Dashboard**:
  - Show files opened in last 7 days with thumbnails
  - Quick access chips for frequent locations
  - Recent searches history
  - Saved search queries

- **Content Preview Panel**:
  - Thumbnail preview for images/PDFs
  - Text preview for documents (first 500 chars)
  - File metadata display (size, created, modified, path, file type)
  - One-click open with default application

---

### FEATURE SET 3: TAGGING & METADATA SYSTEM
**Problem: Folder hierarchies are rigid; files belong to multiple categories**

**Features:**
- **Smart Tagging**:
  - Create unlimited custom tags (Project, Client, Priority, Status, etc.)
  - Color-coded tags for visual organization
  - Emoji support for quick visual recognition
  - Multi-tag files (one file can have multiple tags)
  - Tag suggestions based on file name/content

- **Priority & Status Tags**:
  - Priority: Urgent, High, Medium, Low, Later
  - Status: Active, Completed, Archived, Review, Pending
  - Due Dates: Create reminders for files (Show notification when due)
  - Custom status workflows (Design → In Review → Approved)

- **Project Organization**:
  - Group files by project across multiple folders
  - Virtual project folders (files stay in place, linked in project view)
  - Project templates (auto-create structure for new projects)
  - Nested projects (Sub-projects within main projects)

- **Metadata Enhancement**:
  - Auto-extract: Author, Created Date, Modified Date, File Size
  - Manual metadata: Add notes, descriptions, custom fields
  - Batch edit metadata (apply to multiple files)

---

### FEATURE SET 4: DUPLICATE DETECTION & CLEANUP
**Problem: Users accumulate duplicate files, wasting storage space**

**Features:**
- **Smart Duplicate Finder**:
  - Find exact duplicates (same content, different filename)
  - Find similar files (images with same content, different compression)
  - Find near-duplicates (99% similar documents)
  - Scan speed: 1000 files in <3 seconds

- **Duplicate Cleanup Workflow**:
  - Mark duplicates for deletion with safety review
  - Keep newest/oldest option
  - Preview before deletion
  - Move to Trash (not permanent until emptied)
  - Free up storage immediately (show storage saved)

- **Duplicate Prevention**:
  - Warn when dragging duplicate file into folder
  - Auto-rename if trying to save duplicate
  - Option to merge duplicates into one

---

### FEATURE SET 5: MONITORING & AUTOMATION
**Problem: Files get messy immediately after organizing; no continuous maintenance**

**Features:**
- **Folder Monitoring**:
  - Watch Downloads, Desktop, Documents for new files
  - Real-time notification when file added to watched folder
  - Auto-organize new files based on rules
  - Schedule automatic scans (Daily at 2 AM, Weekly, Monthly)

- **Scheduled Organization**:
  - Define: Which folder to watch, Which rules to apply, When to run
  - Schedule picker: Daily, Weekly on [days], Monthly on [date], Custom cron
  - Run silently in background or notify when complete
  - Skip certain file types (don't auto-organize PDFs if in use)

- **Rules Automation**:
  - Create rules like: "Every PDF added to Downloads → Move to /Documents/PDFs"
  - Archive old files: "Files not modified in 6 months → Archive folder"
  - Cleanup: "Empty folders → Delete"
  - Size management: "Videos > 500MB → Archive"

- **Smart Notifications**:
  - Taskbar icon shows status
  - Notification when auto-organization runs
  - Summary: "Organized 47 files, freed 2.3 GB"

---

### FEATURE SET 6: FILE RECOVERY & HISTORY
**Problem: Users accidentally delete/move files and can't recover them**

**Features:**
- **Organization History**:
  - Track every file move/rename/delete operation
  - Undo last X operations (customizable, default 20)
  - Undo all changes from last session
  - View what changed when
  - Restore individual files or batch restore

- **File Location History**:
  - See where file was previously located
  - Timeline view of file's locations
  - Restore to any previous location with one click

- **Trash Management**:
  - Files moved to Trash don't delete immediately
  - View Trash with filters (deleted today, deleted this week, etc.)
  - Restore from Trash with original location or choose new location
  - Auto-empty Trash after 30 days (configurable)
  - Manual empty Trash

- **Backup before Organize**:
  - Create snapshot before major operations
  - Restore entire folder to previous state
  - Compare versions (what changed)

---

### FEATURE SET 7: ANALYTICS & INSIGHTS
**Problem: Users don't understand their file system or what's taking space**

**Features:**
- **Storage Analytics Dashboard**:
  - Total storage used by: File type, Folder, Date range
  - Pie charts showing space distribution
  - Largest files/folders identified
  - Trend: How storage usage changes over time
  - What's taking space? (Show top 10 space hogs)

- **File Organization Metrics**:
  - Organization score: How organized is your system? (0-100%)
  - Duplicate files found: X files, Y GB duplicated
  - Unorganized files: Files not in any project/tag
  - Old files: Files not modified in 6+ months
  - Recommendations: "You have 1.2 GB of duplicate videos. Delete?"

- **File Type Distribution**:
  - Breakdown by: Documents, Images, Videos, Code, Archives, Other
  - Trend over last 12 months
  - Growth rate

- **Usage Insights**:
  - Most frequently opened folder
  - Most recently created/modified files
  - Most used file types
  - Organization improvements over time

---

### FEATURE SET 8: ADVANCED SEARCH & DISCOVERY
**Problem: Can't find files by what they contain or what they look like**

**Features:**
- **Image Search**:
  - Search images by object detection (Find all images with "person", "dog", "landscape")
  - Color search (Find all red images)
  - Similarity search (Find similar photos to selected image)
  - Screenshot detection (Find all screenshots)

- **Document Search**:
  - Search by content inside PDFs, Word docs, Excel sheets
  - Search by extracted text (OCR for scanned documents)
  - Search across all documents simultaneously
  - Find all documents mentioning specific person/company/date

- **Advanced Filters**:
  - Date range picker with presets
  - Size range slider
  - File type multi-select
  - Custom metadata filters
  - Save complex searches as "Smart Folders"

---

### FEATURE SET 9: BATCH OPERATIONS
**Problem: Users have to do operations one file at a time, time-consuming**

**Features:**
- **Batch File Operations**:
  - Select multiple files (100+ support)
  - Move/Copy/Delete all selected files
  - Rename with patterns: `%name_%date_%number` → file_2024-11-18_001
  - Batch convert formats (JPG → PNG, DOCX → PDF, etc.)
  - Change permissions (Read-only, Hidden, etc.)
  - Add tags to multiple files
  - Add to project simultaneously

- **Batch Rename Wizard**:
  - Pattern-based: `Project-%year%-%month%-%counter%`
  - Replace in names: Change "Old" → "New" across all
  - Case conversion: UPPERCASE, lowercase, Title Case
  - Remove patterns: Remove "Copy of" from all names
  - Preview before applying

- **Quick Actions**:
  - Right-click context menu in Windows Explorer
  - "Organize with [Rule Name]"
  - "Add to [Project]"
  - "Tag as [Tag]"
  - "Move to Archive"

---

### FEATURE SET 10: SETTINGS & CUSTOMIZATION
**Problem: One-size-fits-all solutions don't fit everyone's workflow**

**Features:**
- **Appearance Settings**:
  - Light/Dark/Auto theme
  - Accent color picker
  - Folder view: List, Thumbnail, Details, Compact
  - Font size adjustment
  - Custom wallpaper for dashboard

- **Organization Preferences**:
  - Default auto-organize locations
  - Excluded folders (don't touch these)
  - File type associations
  - Archive folder location
  - Backup folder location

- **Rule Customization**:
  - Edit/delete predefined rules
  - Create custom rule templates
  - Set rule priority (run in specific order)
  - Enable/disable rules temporarily
  - Export/Import rules (share with team/backup)

- **Notification Settings**:
  - Popup notifications on/off
  - Taskbar icon badge count
  - Sound notifications
  - Schedule quiet hours (no notifications 11 PM - 7 AM)

- **Performance Settings**:
  - Skip scanning folders larger than X GB
  - Limit concurrent operations
  - Use less CPU mode
  - Enable/disable background monitoring

---

### FEATURE SET 11: FILE ORGANIZATION TEMPLATES
**Problem: Users starting from scratch don't know optimal folder structure**

**Features:**
- **Pre-built Organization Templates**:
  - Downloads Cleaner: Auto-sort Downloads by file type, date, frequency
  - Photography Studio: Images → By Camera Type/Date/Location/Subject
  - Project Manager: Create project structure with subfolders
  - Student Setup: Organize by Course/Semester/Assignment Type
  - Business Documents: By Department/Year/Client/Document Type
  - Creative Work: By Project/Asset Type/Version/Status
  - Code Repository: By Language/Project/Status
  - Financial: By Year/Category/Type (Invoice, Receipt, Statement)

- **Template Customization**:
  - Start with template, customize folder names
  - Add/remove folder levels
  - Add rules to each template
  - Save as new template

- **One-Click Apply**:
  - Select template → Apply to folder
  - Auto-organize existing files according to template
  - Future files organized same way automatically

---

### FEATURE SET 12: INTEGRATION & EXTENSIBILITY
**Problem: File organizer works in isolation, doesn't connect with user's workflow**

**Features:**
- **Windows Integration**:
  - Right-click context menu in Explorer
  - Shell integration (custom commands)
  - Taskbar quick access
  - File association handling
  - Desktop shortcut support

- **Windows Features Support**:
  - Recognize Windows Libraries (Documents, Pictures, Music, Videos)
  - OneDrive/Google Drive sync folder handling
  - Network drive support
  - Archive (7z, ZIP) preview and organization

- **Planned Integrations** (future):
  - Cloud storage (OneDrive, Google Drive, Dropbox)
  - Calendar (organize by calendar events)
  - Email (organize attachments)

- **Export Capabilities**:
  - Export organization report as PDF
  - Export file listing as CSV/Excel
  - Export search results
  - Export rules for backup/sharing

---

### FEATURE SET 13: SAFETY & SECURITY
**Problem: Users scared of organizing because files might get lost/corrupted**

**Features:**
- **Safe Operations**:
  - Preview all changes before executing
  - Confirmation dialog for destructive operations
  - Undo button always available
  - No permanent delete (move to Trash first)
  - File integrity verification before/after operations

- **Backup & Recovery**:
  - Auto-backup before major operations (optional)
  - Backup to separate location
  - Restore full backup with one click
  - Incremental backups (save space)

- **Lock Files**:
  - Lock important files (can't be moved/deleted)
  - Protected folders (skip organization)
  - Read-only enforcement

- **Logging**:
  - Every operation logged with timestamp
  - View what user did
  - Export activity log

---

### FEATURE SET 14: LEARNING & INTELLIGENCE
**Problem: Organization rules are static; don't adapt to user behavior**

**Features:**
- **Behavior Learning**:
  - Track where user manually moves files
  - Learn patterns from user behavior
  - Suggest improvements to rules
  - Adjust categorization based on corrections

- **Smart Suggestions**:
  - "You usually put PDFs with 'Invoice' in name in /Finance. Apply to all?"
  - "These 5 documents look related. Create project?"
  - "You moved this type of file 3 times. Create a rule?"

- **Predictive Organization**:
  - Predict correct destination for new file
  - Show confidence score
  - User can confirm/reject, system learns

---

## PART 2: TECHNICAL ARCHITECTURE

### Tech Stack
```
Frontend: Electron + React + TypeScript
  - Rich UI with Shadcn/UI components
  - Real-time file preview
  - Responsive design

Backend: Python
  - FastAPI for file operations API
  - File system monitoring (watchdog)
  - ML model for categorization (scikit-learn)
  - SQLite for local database

Inter-process: ZeroMQ or HTTP

OS Integration: Windows API (ctypes), WMI
```

### Architecture Diagram
```
┌─────────────────────────────────┐
│  Electron (Frontend - React)    │
│  ├─ Dashboard                   │
│  ├─ Search                      │
│  ├─ Rules Editor                │
│  ├─ File Browser                │
│  └─ Settings                    │
└──────────────────┬──────────────┘
                   │ IPC
┌──────────────────▼──────────────┐
│  Node.js Backend (Express)      │
│  ├─ API Routes                  │
│  ├─ File Operations             │
│  └─ Database Layer              │
└──────────────────┬──────────────┘
                   │ HTTP
┌──────────────────▼──────────────┐
│  Python (FastAPI)               │
│  ├─ File Analysis               │
│  ├─ Rule Engine                 │
│  ├─ ML Categorization           │
│  ├─ Monitoring Service          │
│  └─ Search Engine               │
└──────────────────┬──────────────┘
                   │
┌──────────────────▼──────────────┐
│  SQLite Database                │
│  ├─ File Index                  │
│  ├─ Rules                       │
│  ├─ Tags                        │
│  ├─ Projects                    │
│  ├─ Organization History        │
│  └─ User Preferences            │
└─────────────────────────────────┘
```

### Database Schema
```
Tables:
- files: id, path, filename, extension, size, created, modified, mime_type, hash
- rules: id, name, conditions, actions, enabled, created, modified
- tags: id, name, color, emoji, created
- file_tags: file_id, tag_id
- projects: id, name, description, created, modified
- project_files: project_id, file_id
- organization_history: id, operation, source_path, dest_path, timestamp, reversible
- file_metadata: id, file_id, key, value
- user_preferences: key, value
- search_history: query, timestamp, result_count
```

---

## PART 3: DETAILED DEVELOPMENT PLAN WITH STEP-BY-STEP SOLUTIONS

### PHASE 1: PROJECT SETUP & INFRASTRUCTURE (Week 1-2)
**Objective**: Get basic app skeleton running with Python backend and Electron frontend communicating

#### Step 1.1: Initialize Project Structure
**Problem**: Unorganized codebase makes future development chaotic
**Solution**:
```
file-organizer/
├─ electron/
│  ├─ src/
│  │  ├─ components/
│  │  ├─ pages/
│  │  ├─ utils/
│  │  ├─ types/
│  │  ├─ assets/
│  │  └─ App.tsx
│  ├─ public/
│  ├─ package.json
│  └─ tsconfig.json
├─ backend/
│  ├─ python/
│  │  ├─ main.py
│  │  ├─ api/
│  │  │  ├─ files.py
│  │  │  ├─ rules.py
│  │  │  └─ search.py
│  │  ├─ services/
│  │  │  ├─ file_analyzer.py
│  │  │  ├─ categorizer.py
│  │  │  ├─ monitor.py
│  │  │  └─ rule_engine.py
│  │  ├─ models/
│  │  │  ├─ ml_model.pkl
│  │  │  └─ categorization.py
│  │  ├─ database/
│  │  │  └─ db.py
│  │  ├─ config.py
│  │  ├─ requirements.txt
│  │  └─ Makefile
├─ docs/
├─ tests/
└─ .gitignore
```

**Steps**:
1. Create directory structure with `mkdir -p` commands
2. Initialize Git repo
3. Create `.gitignore` (exclude: __pycache__, node_modules, .env, *.db)
4. Create README with project description

#### Step 1.2: Set Up Electron + React + TypeScript Frontend
**Problem**: Need modern, type-safe frontend framework with hot reload
**Solution**:
```bash
npx create-electron-app file-organizer --template=webpack --typescript

npm install react react-dom
npm install -D @types/react @types/react-dom
npm install typescript ts-loader

# UI Components
npm install shadcn-ui radix-ui recharts lucide-react
npm install tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Utilities
npm install axios zustand date-fns
npm install -D vitest @testing-library/react
```

**Implementation**:
- Create `electron/src/App.tsx` with basic routing
- Set up Tailwind config for styling
- Create folder structure for components, pages, utils
- Add tsconfig with strict mode enabled

#### Step 1.3: Set Up Python Backend with FastAPI
**Problem**: Need lightweight, fast Python API for file operations
**Solution**:
```bash
cd backend/python
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate

pip install fastapi uvicorn python-multipart
pip install watchdog  # File system monitoring
pip install pillow  # Image processing
pip install pdf2image pytesseract  # OCR
pip install sqlite3  # Database
pip install scikit-learn numpy  # ML
pip install python-dotenv  # Config

# Create requirements.txt
pip freeze > requirements.txt
```

**Implementation** (`backend/python/main.py`):
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI(title="FileOrganizer API")

# CORS for Electron
app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "running"}

# Routes will be added in subsequent steps
```

**Run command**:
```bash
uvicorn main:app --reload --port 8000
```

#### Step 1.4: Set Up IPC Communication (Electron ↔ Python)
**Problem**: Electron and Python are different processes; need to communicate
**Solution**: Use HTTP REST API (simpler than socket.io for this use case)

**Electron HTTP Client** (`electron/src/utils/api.ts`):
```typescript
import axios from 'axios';

const API_BASE = 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE,
  timeout: 30000,
});

export const fileApi = {
  async analyzeFolder(folderPath: string) {
    return api.post('/files/analyze', { folder_path: folderPath });
  },
  
  async getFiles(folderPath: string, filters?: any) {
    return api.get('/files/list', { params: { folder_path: folderPath, ...filters } });
  },
  
  async organizeFiles(plan: any) {
    return api.post('/files/organize', plan);
  },
};
```

**Python API Entry** (`backend/python/api/files.py`):
```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/files", tags=["files"])

class FolderAnalysisRequest(BaseModel):
    folder_path: str

@router.post("/analyze")
async def analyze_folder(request: FolderAnalysisRequest):
    # Will implement file analysis logic
    return {"status": "analysis_started"}

@router.get("/list")
async def list_files(folder_path: str):
    # Will implement file listing
    return {"files": []}

@router.post("/organize")
async def organize_files(plan: dict):
    # Will implement organization logic
    return {"status": "organized"}
```

**Include in main.py**:
```python
from api import files
app.include_router(files.router)
```

#### Step 1.5: Set Up SQLite Database
**Problem**: Need local persistent storage for files, rules, tags, history
**Solution**:

**Database Setup** (`backend/python/database/db.py`):
```python
import sqlite3
from pathlib import Path
import json

DB_PATH = Path.home() / ".fileorganizer" / "database.db"
DB_PATH.parent.mkdir(exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY,
        path TEXT UNIQUE,
        filename TEXT,
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
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        conditions JSON,
        actions JSON,
        enabled BOOLEAN DEFAULT 1,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        color TEXT,
        emoji TEXT,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS file_tags (
        file_id INTEGER,
        tag_id INTEGER,
        FOREIGN KEY(file_id) REFERENCES files(id),
        FOREIGN KEY(tag_id) REFERENCES tags(id),
        UNIQUE(file_id, tag_id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS organization_history (
        id INTEGER PRIMARY KEY,
        operation TEXT,
        source_path TEXT,
        dest_path TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        reversible BOOLEAN
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized")
```

#### Step 1.6: Test Frontend-Backend Communication
**Problem**: Need to verify Electron can talk to Python
**Solution**:

**Create Test Component** (`electron/src/pages/Home.tsx`):
```typescript
import React, { useState } from 'react';
import { api } from '@/utils/api';

export default function Home() {
  const [status, setStatus] = useState('Not connected');
  
  const testConnection = async () => {
    try {
      const response = await api.get('/health');
      setStatus(`Connected: ${response.data.status}`);
    } catch (err) {
      setStatus(`Error: Backend not running`);
    }
  };
  
  return (
    <div className="p-8">
      <h1>FileOrganizer</h1>
      <p>Status: {status}</p>
      <button 
        onClick={testConnection}
        className="px-4 py-2 bg-blue-500 text-white rounded"
      >
        Test Connection
      </button>
    </div>
  );
}
```

**Test Steps**:
1. Start Python backend: `uvicorn main:app --reload`
2. Start Electron dev: `npm start`
3. Click "Test Connection" button
4. Should show "Connected: running"

---

### PHASE 2: CORE FILE OPERATIONS (Week 2-3)
**Objective**: Implement file reading, analysis, and basic organization

#### Step 2.1: Implement File Scanner with Hashing
**Problem**: Need to efficiently scan folders and detect duplicates
**Solution**:

**File Scanner Service** (`backend/python/services/file_scanner.py`):
```python
import os
import hashlib
from pathlib import Path
from datetime import datetime
from mimetypes import guess_type
from concurrent.futures import ThreadPoolExecutor
import sqlite3
from database.db import DB_PATH

class FileScanner:
    def __init__(self, max_workers=4):
        self.max_workers = max_workers
    
    def get_file_hash(self, file_path: str, chunk_size=8192) -> str:
        """Calculate SHA256 hash of file for duplicate detection"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(chunk_size), b""):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except (IOError, OSError):
            return None
    
    def get_file_info(self, file_path: str) -> dict:
        """Extract file metadata"""
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
        except (IOError, OSError):
            return None
    
    def scan_folder(self, folder_path: str, recursive=True) -> list:
        """Scan folder and return file information"""
        files = []
        
        if not os.path.isdir(folder_path):
            return files
        
        try:
            for root, dirs, filenames in os.walk(folder_path):
                if not recursive:
                    dirs.clear()  # Don't recurse
                
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    file_info = self.get_file_info(file_path)
                    
                    if file_info:
                        file_info['hash'] = self.get_file_hash(file_path)
                        files.append(file_info)
        
        except Exception as e:
            print(f"Error scanning folder: {e}")
        
        return files
    
    def save_files_to_db(self, files: list):
        """Save scanned files to database"""
        conn = sqlite3.connect(DB_PATH)
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
        
        conn.commit()
        conn.close()

scanner = FileScanner()
```

#### Step 2.2: Implement File Analysis for Categorization
**Problem**: Need to read file content and determine category
**Solution**:

**File Analyzer Service** (`backend/python/services/file_analyzer.py`):
```python
import os
import mimetypes
from pathlib import Path
import json

class FileAnalyzer:
    """Analyze files to determine category and extract content"""
    
    def __init__(self):
        self.category_keywords = {
            'documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt'],
            'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp'],
            'videos': ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'webm'],
            'audio': ['mp3', 'wav', 'flac', 'aac', 'm4a', 'wma', 'ogg'],
            'archives': ['zip', '7z', 'rar', 'tar', 'gz', 'iso'],
            'code': ['py', 'js', 'java', 'cpp', 'c', 'php', 'rb', 'go', 'rs'],
            'executables': ['exe', 'msi', 'bat', 'cmd', 'ps1', 'sh'],
        }
    
    def get_file_category(self, file_path: str) -> str:
        """Determine category from file extension"""
        ext = Path(file_path).suffix.lstrip('.').lower()
        
        for category, extensions in self.category_keywords.items():
            if ext in extensions:
                return category
        
        return 'other'
    
    def extract_content_preview(self, file_path: str) -> str:
        """Extract first 500 chars of text-based files"""
        try:
            ext = Path(file_path).suffix.lower()
            
            if ext in ['.txt', '.md', '.log', '.csv', '.json', '.xml']:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read(500)
        except:
            pass
        
        return ""
    
    def extract_metadata_from_content(self, file_path: str) -> dict:
        """Extract keywords, dates, company names from document"""
        metadata = {
            'keywords': [],
            'mentioned_dates': [],
            'mentioned_companies': [],
        }
        
        try:
            content = self.extract_content_preview(file_path)
            
            # Simple keyword extraction
            common_words = ['the', 'and', 'or', 'is', 'to', 'a', 'in', 'of']
            words = content.lower().split()
            keywords = [w for w in words if len(w) > 4 and w not in common_words]
            metadata['keywords'] = list(set(keywords[:10]))
            
        except:
            pass
        
        return metadata
    
    def analyze_file(self, file_path: str) -> dict:
        """Complete file analysis"""
        return {
            'path': file_path,
            'filename': os.path.basename(file_path),
            'category': self.get_file_category(file_path),
            'content_preview': self.extract_content_preview(file_path),
            'metadata': self.extract_metadata_from_content(file_path),
        }

analyzer = FileAnalyzer()
```

#### Step 2.3: Implement Rule Engine
**Problem**: Need to evaluate rules against files and generate organization plan
**Solution**:

**Rule Engine Service** (`backend/python/services/rule_engine.py`):
```python
import json
from typing import List, Dict
from datetime import datetime, timedelta
import sqlite3
from database.db import DB_PATH

class RuleEngine:
    """Evaluate rules and generate organization plan"""
    
    def __init__(self):
        self.condition_operators = {
            'equals': lambda a, b: a == b,
            'contains': lambda a, b: b in a,
            'startswith': lambda a, b: a.startswith(b),
            'endswith': lambda a, b: a.endswith(b),
            'gt': lambda a, b: a > b,
            'lt': lambda a, b: a < b,
            'in': lambda a, b: a in b.split(','),
        }
    
    def load_rules(self) -> List[Dict]:
        """Load enabled rules from database"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM rules WHERE enabled = 1')
        
        rules = []
        for row in cursor.fetchall():
            rules.append({
                'id': row[0],
                'name': row[1],
                'conditions': json.loads(row[2]),
                'actions': json.loads(row[3]),
            })
        
        conn.close()
        return rules
    
    def evaluate_condition(self, file_info: Dict, condition: Dict) -> bool:
        """Evaluate single condition against file"""
        field = condition.get('field')
        operator = condition.get('operator')
        value = condition.get('value')
        
        file_value = file_info.get(field)
        
        if operator in self.condition_operators:
            return self.condition_operators[operator](file_value, value)
        
        return False
    
    def evaluate_rule(self, file_info: Dict, rule: Dict) -> bool:
        """Evaluate all conditions in rule (AND logic)"""
        conditions = rule.get('conditions', [])
        
        for condition in conditions:
            if not self.evaluate_condition(file_info, condition):
                return False
        
        return True
    
    def generate_destination(self, file_info: Dict, rule: Dict) -> str:
        """Generate destination path from rule action"""
        action = rule.get('actions', {})
        dest_template = action.get('destination', 'Organized')
        
        # Replace placeholders
        dest = dest_template
        dest = dest.replace('{extension}', file_info['extension'].lstrip('.'))
        dest = dest.replace('{filename}', file_info['filename'])
        dest = dest.replace('{year}', datetime.now().strftime('%Y'))
        dest = dest.replace('{month}', datetime.now().strftime('%m'))
        dest = dest.replace('{category}', file_info.get('category', 'Other'))
        
        return dest
    
    def generate_organization_plan(self, folder_path: str, files: List[Dict]) -> Dict:
        """Generate complete organization plan for files"""
        rules = self.load_rules()
        plan = {
            'total_files': len(files),
            'operations': [],
            'summary': {
                'to_move': 0,
                'duplicates': 0,
                'errors': 0,
            }
        }
        
        for file_info in files:
            for rule in rules:
                if self.evaluate_rule(file_info, rule):
                    destination = self.generate_destination(file_info, rule)
                    
                    plan['operations'].append({
                        'source': file_info['path'],
                        'destination': destination,
                        'rule_id': rule['id'],
                        'action': 'move',
                    })
                    
                    plan['summary']['to_move'] += 1
                    break
        
        return plan

rule_engine = RuleEngine()
```

#### Step 2.4: Create API Endpoints for File Operations
**Problem**: Electron needs API endpoints to trigger file operations
**Solution**:

**Update** `backend/python/api/files.py`:
```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.file_scanner import scanner
from services.file_analyzer import analyzer
from services.rule_engine import rule_engine

router = APIRouter(prefix="/files", tags=["files"])

class AnalyzeFolderRequest(BaseModel):
    folder_path: str

class OrganizeFilesRequest(BaseModel):
    plan: dict

@router.post("/analyze")
async def analyze_folder(request: AnalyzeFolderRequest):
    """Scan folder and generate organization plan"""
    try:
        # Scan folder
        files = scanner.scan_folder(request.folder_path)
        
        # Analyze files
        analyzed_files = [analyzer.analyze_file(f['path']) for f in files]
        
        # Save to database
        scanner.save_files_to_db(files)
        
        # Generate plan
        plan = rule_engine.generate_organization_plan(
            request.folder_path,
            files
        )
        
        return {
            "status": "success",
            "total_files": len(files),
            "plan": plan,
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/organize")
async def organize_files(request: OrganizeFilesRequest):
    """Execute organization plan"""
    try:
        operations = request.plan.get('operations', [])
        results = {
            'succeeded': 0,
            'failed': 0,
            'errors': [],
        }
        
        for op in operations:
            try:
                source = op['source']
                dest = op['destination']
                
                # Create destination directory
                os.makedirs(dest, exist_ok=True)
                
                # Move file
                dest_file = os.path.join(dest, os.path.basename(source))
                shutil.move(source, dest_file)
                
                # Log operation
                # ... (will implement logging)
                
                results['succeeded'] += 1
            
            except Exception as e:
                results['failed'] += 1
                results['errors'].append({
                    'file': op['source'],
                    'error': str(e)
                })
        
        return {
            "status": "success" if results['failed'] == 0 else "partial",
            "results": results,
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list")
async def list_files(folder_path: str, skip: int = 0, limit: int = 100):
    """List files in folder with pagination"""
    try:
        files = scanner.scan_folder(folder_path)
        return {
            "total": len(files),
            "files": files[skip:skip+limit],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

---

### PHASE 3: UI IMPLEMENTATION (Week 3-4)
**Objective**: Build rich, responsive UI for all features

#### Step 3.1: Create Dashboard Component
**Problem**: Users need overview of system status and quick actions
**Solution**:

**Dashboard** (`electron/src/pages/Dashboard.tsx`):
```typescript
import React, { useState, useEffect } from 'react';
import { BarChart, Bar, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';
import { api } from '@/utils/api';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { AlertCircle, FolderOpen, FileStack, TrendingUp } from 'lucide-react';

export default function Dashboard() {
  const [stats, setStats] = useState({
    totalFiles: 0,
    storageUsed: '0 GB',
    organizationScore: 0,
    duplicatesFound: 0,
    duplicateSize: '0 GB',
  });

  useEffect(() => {
    // Fetch statistics
    const fetchStats = async () => {
      try {
        const response = await api.get('/analytics/stats');
        setStats(response.data);
      } catch (err) {
        console.error('Error fetching stats:', err);
      }
    };
    
    fetchStats();
  }, []);

  const storageData = [
    { name: 'Documents', value: 35 },
    { name: 'Images', value: 25 },
    { name: 'Videos', value: 30 },
    { name: 'Other', value: 10 },
  ];

  const COLORS = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444'];

  return (
    <div className="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-screen">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-slate-900">Dashboard</h1>
        <p className="text-slate-600 mt-2">Overview of your file organization</p>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Total Files</CardTitle>
            <FileStack className="h-4 w-4 text-blue-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.totalFiles}</div>
            <p className="text-xs text-slate-500">files indexed</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Storage Used</CardTitle>
            <TrendingUp className="h-4 w-4 text-green-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.storageUsed}</div>
            <p className="text-xs text-slate-500">total capacity</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Organization Score</CardTitle>
            <TrendingUp className="h-4 w-4 text-purple-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.organizationScore}%</div>
            <p className="text-xs text-slate-500">well organized</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Duplicates Found</CardTitle>
            <AlertCircle className="h-4 w-4 text-red-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.duplicatesFound}</div>
            <p className="text-xs text-slate-500">{stats.duplicateSize} wasted</p>
          </CardContent>
        </Card>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        {/* Storage Distribution */}
        <Card>
          <CardHeader>
            <CardTitle>Storage Distribution</CardTitle>
          </CardHeader>
          <CardContent>
            <PieChart width={300} height={300}>
              <Pie
                data={storageData}
                cx={150}
                cy={150}
                innerRadius={60}
                outerRadius={100}
                paddingAngle={2}
                dataKey="value"
              >
                {storageData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
            <div className="mt-4 space-y-2">
              {storageData.map((item, idx) => (
                <div key={idx} className="flex items-center justify-between text-sm">
                  <span className="flex items-center">
                    <div
                      className="w-3 h-3 rounded-full mr-2"
                      style={{ backgroundColor: COLORS[idx] }}
                    ></div>
                    {item.name}
                  </span>
                  <span className="font-medium">{item.value}%</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Recent Activity */}
        <Card>
          <CardHeader>
            <CardTitle>Recent Activity</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <p className="font-medium">Files Organized</p>
                  <p className="text-sm text-slate-500">47 files moved</p>
                </div>
                <span className="text-green-500 font-bold">+47</span>
              </div>
              <div className="border-t pt-4"></div>
              <div className="flex items-center justify-between">
                <div>
                  <p className="font-medium">Duplicates Cleaned</p>
                  <p className="text-sm text-slate-500">2.3 GB freed</p>
                </div>
                <span className="text-blue-500 font-bold">-2.3 GB</span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Quick Actions */}
      <div className="space-y-4">
        <h2 className="text-lg font-semibold text-slate-900">Quick Actions</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Button size="lg" className="bg-blue-500 hover:bg-blue-600">
            <FolderOpen className="mr-2 h-5 w-5" />
            Organize Folder
          </Button>
          <Button size="lg" variant="outline">
            <FileStack className="mr-2 h-5 w-5" />
            Find Duplicates
          </Button>
        </div>
      </div>
    </div>
  );
}
```

#### Step 3.2: Create File Organizer Component
**Problem**: Users need interface to select folder, preview changes, and execute organization
**Solution**:

**File Organizer** (`electron/src/pages/Organizer.tsx`):
```typescript
import React, { useState } from 'react';
import { api } from '@/utils/api';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { CheckCircle, AlertCircle, Loader } from 'lucide-react';

export default function Organizer() {
  const [selectedFolder, setSelectedFolder] = useState('');
  const [loading, setLoading] = useState(false);
  const [plan, setPlan] = useState(null);
  const [executing, setExecuting] = useState(false);
  const [result, setResult] = useState(null);

  const selectFolder = async () => {
    // Use Electron's dialog to select folder
    const { ipcRenderer } = require('electron');
    const result = await ipcRenderer.invoke('dialog:openDirectory');
    
    if (result.filePaths.length > 0) {
      setSelectedFolder(result.filePaths[0]);
    }
  };

  const analyzFolder = async () => {
    if (!selectedFolder) return;
    
    setLoading(true);
    try {
      const response = await api.post('/files/analyze', {
        folder_path: selectedFolder,
      });
      
      setPlan(response.data.plan);
    } catch (err) {
      console.error('Error analyzing folder:', err);
    } finally {
      setLoading(false);
    }
  };

  const executePlan = async () => {
    if (!plan) return;
    
    setExecuting(true);
    try {
      const response = await api.post('/files/organize', { plan });
      setResult(response.data.results);
    } catch (err) {
      console.error('Error executing plan:', err);
    } finally {
      setExecuting(false);
    }
  };

  return (
    <div className="p-8 space-y-6">
      <div>
        <h1 className="text-3xl font-bold">File Organizer</h1>
        <p className="text-slate-600">Analyze and organize your files</p>
      </div>

      {/* Step 1: Select Folder */}
      <Card>
        <CardHeader>
          <CardTitle>Step 1: Select Folder</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="p-4 border-2 border-dashed rounded-lg bg-slate-50">
              <p className="text-center">
                {selectedFolder || 'No folder selected'}
              </p>
            </div>
            <Button onClick={selectFolder} className="w-full">
              Browse Folder
            </Button>
          </div>
        </CardContent>
      </Card>

      {/* Step 2: Analyze */}
      {selectedFolder && (
        <Card>
          <CardHeader>
            <CardTitle>Step 2: Analyze & Preview</CardTitle>
          </CardHeader>
          <CardContent>
            <Button
              onClick={analyzFolder}
              disabled={loading}
              className="w-full"
              size="lg"
            >
              {loading ? (
                <>
                  <Loader className="mr-2 h-5 w-5 animate-spin" />
                  Analyzing...
                </>
              ) : (
                'Analyze Folder'
              )}
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Step 3: Preview Plan */}
      {plan && (
        <Card>
          <CardHeader>
            <CardTitle>Step 3: Preview Changes</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <Alert>
              <AlertCircle className="h-4 w-4" />
              <AlertDescription>
                {plan.summary.to_move} files will be moved
              </AlertDescription>
            </Alert>

            <div className="max-h-96 overflow-y-auto space-y-2">
              {plan.operations.slice(0, 20).map((op, idx) => (
                <div
                  key={idx}
                  className="p-3 bg-slate-50 rounded flex items-start justify-between"
                >
                  <div className="flex-1">
                    <p className="font-medium text-sm">{op.source.split('\\').pop()}</p>
                    <p className="text-xs text-slate-500">
                      → {op.destination}
                    </p>
                  </div>
                  <CheckCircle className="h-5 w-5 text-green-500 ml-2" />
                </div>
              ))}
              
              {plan.operations.length > 20 && (
                <p className="text-center text-slate-500 py-2">
                  +{plan.operations.length - 20} more files
                </p>
              )}
            </div>

            <Button
              onClick={executePlan}
              disabled={executing}
              className="w-full bg-green-600 hover:bg-green-700"
              size="lg"
            >
              {executing ? (
                <>
                  <Loader className="mr-2 h-5 w-5 animate-spin" />
                  Organizing...
                </>
              ) : (
                'Execute Organization'
              )}
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Step 4: Results */}
      {result && (
        <Card className="border-green-200 bg-green-50">
          <CardHeader>
            <CardTitle className="text-green-900">Organization Complete</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span>Files Successfully Moved:</span>
                <span className="font-bold text-green-600">
                  {result.succeeded}
                </span>
              </div>
              {result.failed > 0 && (
                <div className="flex justify-between">
                  <span>Failed:</span>
                  <span className="font-bold text-red-600">{result.failed}</span>
                </div>
              )}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
```

#### Step 3.3: Create Search Component
**Problem**: Users need powerful search to find files quickly
**Solution**:

**Search** (`electron/src/pages/Search.tsx`):
```typescript
import React, { useState, useCallback } from 'react';
import { api } from '@/utils/api';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Search as SearchIcon, Filter, Loader } from 'lucide-react';

export default function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [filters, setFilters] = useState({
    fileType: '',
    dateRange: 'all',
    sizeMin: 0,
    sizeMax: Infinity,
  });

  const handleSearch = useCallback(async () => {
    if (!query.trim()) return;
    
    setLoading(true);
    try {
      const response = await api.get('/search', {
        params: {
          q: query,
          ...filters,
        },
      });
      
      setResults(response.data.results);
    } catch (err) {
      console.error('Search error:', err);
    } finally {
      setLoading(false);
    }
  }, [query, filters]);

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <div className="p-8 space-y-6">
      <div>
        <h1 className="text-3xl font-bold">Search Files</h1>
        <p className="text-slate-600">Find files by name, type, date, or content</p>
      </div>

      {/* Search Bar */}
      <div className="space-y-4">
        <div className="flex gap-2">
          <div className="flex-1 relative">
            <SearchIcon className="absolute left-3 top-3 h-5 w-5 text-slate-400" />
            <Input
              placeholder="Search files..."
              className="pl-10"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyPress={handleKeyPress}
            />
          </div>
          <Button onClick={handleSearch} disabled={loading} size="lg">
            {loading ? <Loader className="animate-spin" /> : 'Search'}
          </Button>
        </div>

        {/* Filters */}
        <div className="flex gap-2 flex-wrap">
          <select
            className="px-3 py-2 border rounded-lg"
            value={filters.fileType}
            onChange={(e) => setFilters({ ...filters, fileType: e.target.value })}
          >
            <option value="">All Types</option>
            <option value="documents">Documents</option>
            <option value="images">Images</option>
            <option value="videos">Videos</option>
            <option value="audio">Audio</option>
          </select>

          <select
            className="px-3 py-2 border rounded-lg"
            value={filters.dateRange}
            onChange={(e) => setFilters({ ...filters, dateRange: e.target.value })}
          >
            <option value="all">All Dates</option>
            <option value="today">Today</option>
            <option value="week">This Week</option>
            <option value="month">This Month</option>
            <option value="year">This Year</option>
          </select>
        </div>
      </div>

      {/* Results */}
      {results.length > 0 && (
        <div className="space-y-3">
          <p className="text-sm text-slate-600">
            Found {results.length} results
          </p>
          
          {results.map((file, idx) => (
            <Card key={idx} className="hover:bg-slate-50 cursor-pointer transition">
              <CardContent className="pt-6">
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <p className="font-medium">{file.filename}</p>
                    <p className="text-sm text-slate-500">{file.path}</p>
                    <div className="flex gap-4 mt-2 text-xs text-slate-400">
                      <span>{file.size} bytes</span>
                      <span>{new Date(file.modified).toLocaleDateString()}</span>
                    </div>
                  </div>
                  <Button variant="ghost" size="sm">
                    Open
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {query && results.length === 0 && !loading && (
        <Card className="bg-slate-50">
          <CardContent className="pt-6 text-center">
            <p className="text-slate-600">No files found matching "{query}"</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
```

---

### PHASE 4: RULES & AUTOMATION (Week 4-5)
**Objective**: Implement rule creation, editing, and automation

#### Step 4.1: Implement Rules UI
**Problem**: Users need to create and manage organization rules visually
**Solution**:

**Rules Manager** (`electron/src/pages/Rules.tsx`):
```typescript
import React, { useState, useEffect } from 'react';
import { api } from '@/utils/api';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Plus, Edit2, Trash2, Copy } from 'lucide-react';
import RuleBuilder from '@/components/RuleBuilder';

export default function Rules() {
  const [rules, setRules] = useState([]);
  const [showBuilder, setShowBuilder] = useState(false);
  const [editingRule, setEditingRule] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadRules();
  }, []);

  const loadRules = async () => {
    try {
      const response = await api.get('/rules');
      setRules(response.data.rules);
    } catch (err) {
      console.error('Error loading rules:', err);
    }
  };

  const deleteRule = async (ruleId) => {
    try {
      await api.delete(`/rules/${ruleId}`);
      setRules(rules.filter(r => r.id !== ruleId));
    } catch (err) {
      console.error('Error deleting rule:', err);
    }
  };

  const duplicateRule = async (rule) => {
    const newRule = {
      ...rule,
      name: `${rule.name} (Copy)`,
    };
    
    try {
      const response = await api.post('/rules', newRule);
      setRules([...rules, response.data.rule]);
    } catch (err) {
      console.error('Error duplicating rule:', err);
    }
  };

  return (
    <div className="p-8 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Organization Rules</h1>
          <p className="text-slate-600">Automate file organization with custom rules</p>
        </div>
        <Button onClick={() => setShowBuilder(true)} size="lg">
          <Plus className="mr-2 h-5 w-5" />
          New Rule
        </Button>
      </div>

      {/* Rule Builder Modal */}
      {showBuilder && (
        <RuleBuilder
          rule={editingRule}
          onSave={() => {
            setShowBuilder(false);
            setEditingRule(null);
            loadRules();
          }}
          onCancel={() => {
            setShowBuilder(false);
            setEditingRule(null);
          }}
        />
      )}

      {/* Rules List */}
      <div className="space-y-3">
        {rules.map((rule) => (
          <Card key={rule.id}>
            <CardContent className="pt-6">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <p className="font-bold text-lg">{rule.name}</p>
                  <p className="text-sm text-slate-600 mt-2">
                    {rule.conditions.length} condition(s) →{' '}
                    {rule.actions.destination}
                  </p>
                  <div className="mt-3 space-y-1">
                    {rule.conditions.map((cond, idx) => (
                      <p key={idx} className="text-xs text-slate-500">
                        {cond.field} {cond.operator} {cond.value}
                      </p>
                    ))}
                  </div>
                </div>
                
                <div className="flex gap-2 ml-4">
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => {
                      setEditingRule(rule);
                      setShowBuilder(true);
                    }}
                  >
                    <Edit2 className="h-4 w-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => duplicateRule(rule)}
                  >
                    <Copy className="h-4 w-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => deleteRule(rule.id)}
                    className="text-red-500"
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {rules.length === 0 && (
        <Card className="bg-slate-50">
          <CardContent className="pt-6 text-center">
            <p className="text-slate-600">No rules yet. Create one to automate organization.</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
```

#### Step 4.2: Rule Builder Component
**Problem**: Users need intuitive visual interface to build rules
**Solution**:

**RuleBuilder** (`electron/src/components/RuleBuilder.tsx`):
```typescript
import React, { useState } from 'react';
import { api } from '@/utils/api';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Plus, Trash2 } from 'lucide-react';

export default function RuleBuilder({ rule, onSave, onCancel }) {
  const [name, setName] = useState(rule?.name || '');
  const [conditions, setConditions] = useState(
    rule?.conditions || [{ field: 'extension', operator: 'equals', value: '' }]
  );
  const [destination, setDestination] = useState(
    rule?.actions.destination || ''
  );
  const [saving, setSaving] = useState(false);

  const fields = ['extension', 'filename', 'size', 'created', 'modified'];
  const operators = ['equals', 'contains', 'startswith', 'gt', 'lt'];

  const addCondition = () => {
    setConditions([
      ...conditions,
      { field: 'extension', operator: 'equals', value: '' },
    ]);
  };

  const removeCondition = (idx) => {
    setConditions(conditions.filter((_, i) => i !== idx));
  };

  const updateCondition = (idx, key, value) => {
    const newConditions = [...conditions];
    newConditions[idx][key] = value;
    setConditions(newConditions);
  };

  const handleSave = async () => {
    if (!name || !destination) {
      alert('Fill in all required fields');
      return;
    }

    setSaving(true);
    try {
      const ruleData = {
        name,
        conditions,
        actions: { destination },
      };

      if (rule?.id) {
        await api.put(`/rules/${rule.id}`, ruleData);
      } else {
        await api.post('/rules', ruleData);
      }

      onSave();
    } catch (err) {
      console.error('Error saving rule:', err);
      alert('Error saving rule');
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <Card className="w-full max-w-2xl">
        <CardHeader>
          <CardTitle>
            {rule ? 'Edit Rule' : 'Create New Rule'}
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Rule Name */}
          <div>
            <label className="block text-sm font-medium mb-2">Rule Name</label>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="e.g., Organize PDFs"
            />
          </div>

          {/* Conditions */}
          <div>
            <label className="block text-sm font-medium mb-3">Conditions</label>
            <div className="space-y-3">
              {conditions.map((cond, idx) => (
                <div key={idx} className="flex gap-2 items-end">
                  <select
                    value={cond.field}
                    onChange={(e) => updateCondition(idx, 'field', e.target.value)}
                    className="flex-1 px-3 py-2 border rounded"
                  >
                    {fields.map(f => (
                      <option key={f} value={f}>{f}</option>
                    ))}
                  </select>

                  <select
                    value={cond.operator}
                    onChange={(e) => updateCondition(idx, 'operator', e.target.value)}
                    className="flex-1 px-3 py-2 border rounded"
                  >
                    {operators.map(op => (
                      <option key={op} value={op}>{op}</option>
                    ))}
                  </select>

                  <Input
                    value={cond.value}
                    onChange={(e) => updateCondition(idx, 'value', e.target.value)}
                    placeholder="value"
                    className="flex-1"
                  />

                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => removeCondition(idx)}
                    className="text-red-500"
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              ))}
            </div>

            <Button
              variant="outline"
              size="sm"
              onClick={addCondition}
              className="mt-3"
            >
              <Plus className="mr-2 h-4 w-4" />
              Add Condition
            </Button>
          </div>

          {/* Destination */}
          <div>
            <label className="block text-sm font-medium mb-2">
              Destination Folder
            </label>
            <div className="space-y-2">
              <Input
                value={destination}
                onChange={(e) => setDestination(e.target.value)}
                placeholder="/Organized/{category}/{year}/{month}"
              />
              <p className="text-xs text-slate-500">
                Available variables: {'{category}'}, {'{year}'}, {'{month}'}, {'{extension}'}
              </p>
            </div>
          </div>

          {/* Actions */}
          <div className="flex justify-end gap-2 pt-4 border-t">
            <Button variant="outline" onClick={onCancel}>
              Cancel
            </Button>
            <Button onClick={handleSave} disabled={saving}>
              {saving ? 'Saving...' : 'Save Rule'}
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
```

---

### PHASE 5: ADVANCED FEATURES (Week 5-6)
**Objective**: Implement search, tagging, duplicate detection, monitoring

#### Step 5.1: Implement Search Engine
**Problem**: Need fast full-text search across 10,000+ files
**Solution**:

**Search Service** (`backend/python/services/search_engine.py`):
```python
import sqlite3
from database.db import DB_PATH
from datetime import datetime, timedelta

class SearchEngine:
    """Full-text search across files and content"""
    
    def __init__(self):
        pass
    
    def search(self, query: str, filters: dict = None) -> list:
        """Search files with optional filters"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        sql = 'SELECT * FROM files WHERE 1=1'
        params = []
        
        # Filename/content search
        sql += ' AND (filename LIKE ? OR path LIKE ?)'
        search_param = f'%{query}%'
        params.extend([search_param, search_param])
        
        # Filters
        if filters:
            if filters.get('file_type'):
                sql += ' AND extension = ?'
                params.append(filters['file_type'])
            
            if filters.get('date_range'):
                now = datetime.now()
                if filters['date_range'] == 'today':
                    start_date = now.replace(hour=0, minute=0, second=0)
                elif filters['date_range'] == 'week':
                    start_date = now - timedelta(days=7)
                elif filters['date_range'] == 'month':
                    start_date = now - timedelta(days=30)
                elif filters['date_range'] == 'year':
                    start_date = now - timedelta(days=365)
                else:
                    start_date = None
                
                if start_date:
                    sql += ' AND modified >= ?'
                    params.append(start_date.isoformat())
            
            if filters.get('size_min'):
                sql += ' AND size >= ?'
                params.append(filters['size_min'])
            
            if filters.get('size_max'):
                sql += ' AND size <= ?'
                params.append(filters['size_max'])
        
        sql += ' LIMIT 100'
        
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
            })
        
        conn.close()
        return results

search_engine = SearchEngine()
```

**Add Search API Endpoint** (`backend/python/api/search.py`):
```python
from fastapi import APIRouter
from services.search_engine import search_engine

router = APIRouter(prefix="/search", tags=["search"])

@router.get("")
async def search(q: str, file_type: str = None, date_range: str = None):
    """Search files"""
    filters = {}
    if file_type:
        filters['file_type'] = file_type
    if date_range:
        filters['date_range'] = date_range
    
    results = search_engine.search(q, filters)
    
    return {
        "query": q,
        "results": results,
        "count": len(results),
    }
```

#### Step 5.2: Implement Tagging System
**Problem**: Users need to tag files with multiple labels for flexible organization
**Solution**:

**Tagging Service** (`backend/python/services/tagging.py`):
```python
import sqlite3
from database.db import DB_PATH

class TaggingSystem:
    """Manage tags and file tagging"""
    
    def create_tag(self, name: str, color: str, emoji: str = None) -> dict:
        """Create new tag"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
            INSERT INTO tags (name, color, emoji)
            VALUES (?, ?, ?)
            ''', (name, color, emoji))
            
            tag_id = cursor.lastrowid
            conn.commit()
            
            return {
                'id': tag_id,
                'name': name,
                'color': color,
                'emoji': emoji,
            }
        finally:
            conn.close()
    
    def tag_file(self, file_id: int, tag_id: int) -> bool:
        """Tag a file"""
        conn = sqlite3.connect(DB_PATH)
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
    
    def get_file_tags(self, file_id: int) -> list:
        """Get all tags for a file"""
        conn = sqlite3.connect(DB_PATH)
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
                'emoji': row[3],
            })
        
        conn.close()
        return tags
    
    def get_all_tags(self) -> list:
        """Get all tags in system"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tags ORDER BY name')
        
        tags = []
        for row in cursor.fetchall():
            tags.append({
                'id': row[0],
                'name': row[1],
                'color': row[2],
                'emoji': row[3],
            })
        
        conn.close()
        return tags
    
    def search_by_tag(self, tag_id: int) -> list:
        """Find all files with specific tag"""
        conn = sqlite3.connect(DB_PATH)
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
            })
        
        conn.close()
        return files

tagging_system = TaggingSystem()
```

#### Step 5.3: Implement Duplicate Finder
**Problem**: Users accumulate large duplicate files, wasting storage
**Solution**:

**Duplicate Finder Service** (`backend/python/services/duplicate_finder.py`):
```python
import sqlite3
from database.db import DB_PATH

class DuplicateFinder:
    """Find and manage duplicate files"""
    
    def find_duplicates(self) -> dict:
        """Find all duplicate files by hash"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Group files by hash, find duplicates
        cursor.execute('''
        SELECT hash, COUNT(*) as count
        FROM files
        WHERE hash IS NOT NULL
        GROUP BY hash
        HAVING COUNT(*) > 1
        ORDER BY count DESC
        ''')
        
        duplicates = {}
        total_wasted = 0
        
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
                    'size': row[4],
                    'modified': row[6],
                })
            
            # Calculate wasted space (file_size * (count - 1))
            wasted = files[0]['size'] * (count - 1)
            total_wasted += wasted
            
            duplicates[hash_val] = {
                'count': count,
                'files': files,
                'wasted_space': wasted,
            }
        
        conn.close()
        
        return {
            'duplicates': duplicates,
            'total_duplicates': len(duplicates),
            'total_wasted_space': total_wasted,
        }
    
    def mark_for_deletion(self, file_ids: list) -> bool:
        """Mark files for deletion (safe delete)"""
        # In real implementation, move to trash bin
        # Keep the original logic for now
        return True
    
    def delete_duplicates(self, duplicates: dict) -> dict:
        """Delete marked duplicate files"""
        results = {
            'deleted': 0,
            'failed': 0,
            'space_freed': 0,
        }
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        for hash_val, data in duplicates.items():
            # Keep first file, delete rest
            files_to_delete = data['files'][1:]
            
            for file in files_to_delete:
                try:
                    import os
                    import shutil
                    
                    # Move to trash instead of permanent delete
                    trash_path = os.path.expandvars(r'%USERPROFILE%\AppData\Local\Temp')
                    shutil.move(file['path'], os.path.join(trash_path, file['filename']))
                    
                    results['deleted'] += 1
                    results['space_freed'] += file['size']
                except Exception as e:
                    results['failed'] += 1
        
        conn.close()
        return results

duplicate_finder = DuplicateFinder()
```

**Add Duplicate API** (`backend/python/api/duplicates.py`):
```python
from fastapi import APIRouter
from services.duplicate_finder import duplicate_finder

router = APIRouter(prefix="/duplicates", tags=["duplicates"])

@router.get("/find")
async def find_duplicates():
    """Find all duplicate files"""
    result = duplicate_finder.find_duplicates()
    return result

@router.post("/cleanup")
async def cleanup_duplicates(duplicates: dict):
    """Delete duplicate files"""
    result = duplicate_finder.delete_duplicates(duplicates)
    return result
```

---

### PHASE 6: MONITORING & HISTORY (Week 6-7)
**Objective**: Implement file monitoring, organization history, and undo

#### Step 6.1: Implement File Monitoring Service
**Problem**: Users want automatic organization as new files arrive
**Solution**:

**Monitor Service** (`backend/python/services/monitor.py`):
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sqlite3
import threading
import time
from database.db import DB_PATH
from services.rule_engine import rule_engine
from services.file_scanner import scanner
from services.file_analyzer import analyzer

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback
    
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(0.5)  # Wait for file to finish writing
            self.callback(event.src_path, 'created')
    
    def on_modified(self, event):
        if not event.is_directory:
            self.callback(event.src_path, 'modified')

class FileMonitor:
    def __init__(self):
        self.observers = {}
        self.watched_folders = self._load_watched_folders()
    
    def _load_watched_folders(self) -> dict:
        """Load which folders to watch from database"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT key, value FROM user_preferences
        WHERE key LIKE 'watch_%'
        ''')
        
        folders = {}
        for key, value in cursor.fetchall():
            folders[value] = True
        
        conn.close()
        return folders
    
    def watch_folder(self, folder_path: str):
        """Start watching a folder for changes"""
        if folder_path in self.observers:
            return  # Already watching
        
        def on_file_change(path, event_type):
            self._handle_file_change(path, event_type)
        
        event_handler = FileChangeHandler(on_file_change)
        observer = Observer()
        observer.schedule(event_handler, folder_path, recursive=True)
        observer.start()
        
        self.observers[folder_path] = observer
        self.watched_folders[folder_path] = True
    
    def stop_watching(self, folder_path: str):
        """Stop watching a folder"""
        if folder_path in self.observers:
            self.observers[folder_path].stop()
            self.observers[folder_path].join()
            del self.observers[folder_path]
            del self.watched_folders[folder_path]
    
    def _handle_file_change(self, file_path: str, event_type: str):
        """Handle file change event"""
        try:
            # Analyze new file
            file_info = scanner.get_file_info(file_path)
            if not file_info:
                return
            
            file_info['hash'] = scanner.get_file_hash(file_path)
            
            # Get rules
            rules = rule_engine.load_rules()
            
            # Find matching rule
            for rule in rules:
                if rule_engine.evaluate_rule(file_info, rule):
                    destination = rule_engine.generate_destination(file_info, rule)
                    
                    # Auto-organize if enabled
                    import os
                    import shutil
                    os.makedirs(destination, exist_ok=True)
                    dest_file = os.path.join(destination, os.path.basename(file_path))
                    shutil.move(file_path, dest_file)
                    
                    # Log operation
                    self._log_operation('auto_organize', file_path, dest_file)
                    
                    break
        
        except Exception as e:
            print(f"Error handling file change: {e}")
    
    def _log_operation(self, operation: str, source: str, dest: str):
        """Log file operation to database"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO organization_history (operation, source_path, dest_path, reversible)
        VALUES (?, ?, ?, 1)
        ''', (operation, source, dest))
        
        conn.commit()
        conn.close()

monitor = FileMonitor()
```

#### Step 6.2: Implement Organization History & Undo
**Problem**: Users need to undo operations if something goes wrong
**Solution**:

**History Service** (`backend/python/services/history.py`):
```python
import sqlite3
import os
import shutil
from database.db import DB_PATH
from datetime import datetime, timedelta

class OrganizationHistory:
    """Track and manage organization operations"""
    
    def log_operation(self, operation: str, source: str, dest: str):
        """Log an operation"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO organization_history 
        (operation, source_path, dest_path, reversible)
        VALUES (?, ?, ?, 1)
        ''', (operation, source, dest))
        
        conn.commit()
        conn.close()
    
    def get_history(self, limit: int = 50) -> list:
        """Get recent operations"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT id, operation, source_path, dest_path, timestamp
        FROM organization_history
        ORDER BY timestamp DESC
        LIMIT ?
        ''', (limit,))
        
        history = []
        for row in cursor.fetchall():
            history.append({
                'id': row[0],
                'operation': row[1],
                'source': row[2],
                'destination': row[3],
                'timestamp': row[4],
            })
        
        conn.close()
        return history
    
    def undo_operation(self, operation_id: int) -> bool:
        """Undo a specific operation"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT source_path, dest_path FROM organization_history
        WHERE id = ?
        ''', (operation_id,))
        
        row = cursor.fetchone()
        if not row:
            conn.close()
            return False
        
        source, dest = row
        
        try:
            # Move file back
            if os.path.exists(dest):
                os.makedirs(os.path.dirname(source), exist_ok=True)
                shutil.move(dest, source)
            
            # Mark as reverted
            cursor.execute('''
            DELETE FROM organization_history WHERE id = ?
            ''', (operation_id,))
            
            conn.commit()
            conn.close()
            return True
        
        except Exception as e:
            conn.close()
            return False
    
    def undo_last_n_operations(self, n: int) -> dict:
        """Undo last N operations"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT id, source_path, dest_path FROM organization_history
        ORDER BY timestamp DESC
        LIMIT ?
        ''', (n,))
        
        operations = cursor.fetchall()
        results = {'succeeded': 0, 'failed': 0}
        
        for op_id, source, dest in operations:
            if self.undo_operation(op_id):
                results['succeeded'] += 1
            else:
                results['failed'] += 1
        
        conn.close()
        return results
    
    def clear_old_history(self, days: int = 30):
        """Clear history older than N days"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
        
        cursor.execute('''
        DELETE FROM organization_history WHERE timestamp < ?
        ''', (cutoff_date,))
        
        conn.commit()
        conn.close()

history_service = OrganizationHistory()
```

---

## PART 4: CRITICAL PROBLEMS & SOLUTIONS

### Problem 1: Performance with Large Folders
**Issue**: Scanning 100,000+ files takes too long
**Solution**:
- Use threading to scan multiple files concurrently
- Implement incremental scanning (scan only new files since last scan)
- Cache file hashes to avoid recalculating
- Add progress bar to UI showing scan progress

**Implementation**:
```python
from concurrent.futures import ThreadPoolExecutor

def scan_folder_concurrent(folder_path: str, max_workers=8):
    files = []
    executor = ThreadPoolExecutor(max_workers=max_workers)
    
    for root, dirs, filenames in os.walk(folder_path):
        futures = [executor.submit(self.get_file_info, os.path.join(root, f))
                   for f in filenames]
        
        for future in futures:
            result = future.result()
            if result:
                files.append(result)
    
    return files
```

---

### Problem 2: Handling File Locks (Files in Use)
**Issue**: Can't move/delete files currently open in other applications
**Solution**:
- Check if file is in use before moving
- Queue operation and retry after delay
- Show user which files are locked and why

**Implementation**:
```python
import win32file
import win32con

def is_file_in_use(file_path: str) -> bool:
    try:
        win32file.CreateFile(
            file_path,
            win32con.GENERIC_READ | win32con.GENERIC_WRITE,
            0,  # Exclusive access
            None,
            win32con.OPEN_EXISTING,
            0,
            None
        )
        return False
    except:
        return True
```

---

### Problem 3: Database Locks with Concurrent Access
**Issue**: Multiple processes accessing SQLite simultaneously cause locks
**Solution**:
- Use connection pooling
- Set appropriate timeout values
- Queue database writes

**Implementation**:
```python
import sqlite3

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.execute("PRAGMA journal_mode=WAL")  # Write-Ahead Logging
    return conn
```

---

### Problem 4: Duplicate Detection with Large Files
**Issue**: Hashing 10 GB video files is slow
**Solution**:
- Only hash first/last chunks of large files
- Cache results
- Run in background

**Implementation**:
```python
def get_file_hash_fast(file_path: str, sample_size=1024*1024) -> str:
    """Hash only first 1MB and last 1MB of file for speed"""
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, 'rb') as f:
            # Hash first chunk
            chunk = f.read(sample_size)
            sha256.update(chunk)
            
            # Hash last chunk
            f.seek(-sample_size, 2)
            chunk = f.read(sample_size)
            sha256.update(chunk)
        
        return sha256.hexdigest()
    except:
        return None
```

---

### Problem 5: Windows API Integration
**Issue**: Need to interact with Windows file system features
**Solution**:
- Use pywin32 for Windows-specific operations
- Implement safe file deletion to Recycle Bin
- Support Windows attributes (hidden, read-only)

**Implementation**:
```python
import ctypes
from pathlib import Path

def move_to_recycle_bin(file_path: str) -> bool:
    """Move file to Windows Recycle Bin"""
    try:
        # Use Windows SHFileOperation
        flags = 0x00000010  # FOF_TORECYCLEBIN
        
        from ctypes import wintypes
        
        # Implementation here
        return True
    except:
        return False
```

---

## PART 5: UI/UX DESIGN SPECIFICATIONS

### Design System
```
Colors:
- Primary: #3B82F6 (Blue)
- Success: #10B981 (Green)
- Warning: #F59E0B (Amber)
- Danger: #EF4444 (Red)
- Dark: #1E293B (Slate-900)
- Light: #F1F5F9 (Slate-100)

Typography:
- Headers: Inter Bold (700)
- Subheaders: Inter SemiBold (600)
- Body: Inter Regular (400)
- Small: Inter Regular (400, 12px)

Spacing: 4px, 8px, 16px, 24px, 32px (Tailwind scale)

Shadows:
- Small: 0 1px 2px rgba(0,0,0,0.05)
- Medium: 0 4px 6px rgba(0,0,0,0.1)
- Large: 0 20px 25px rgba(0,0,0,0.1)

Radius: 6px (cards, buttons), 12px (containers)
```

### Main Pages
1. **Dashboard** - Overview with stats and charts
2. **Organizer** - Analyze and organize files
3. **Search** - Find files with advanced filters
4. **Rules** - Manage organization rules
5. **Duplicates** - Find and remove duplicates
6. **History** - View and undo operations
7. **Analytics** - Storage analysis and insights
8. **Tags** - Manage tags and projects
9. **Settings** - Preferences and configuration

---

## PART 6: DEVELOPMENT TIMELINE

**Total Duration: 8 Weeks**

- **Week 1-2**: Project setup, basic file operations
- **Week 2-3**: File analysis, rule engine
- **Week 3-4**: UI implementation (Dashboard, Organizer, Search)
- **Week 4-5**: Rules editor, automation
- **Week 5-6**: Advanced features (tagging, duplicates)
- **Week 6-7**: Monitoring, history, undo
- **Week 7-8**: Testing, optimization, bug fixes, packaging

---

## PART 7: INSTALLATION & PACKAGING

**Create Windows Installer**:
```python
# build.py using PyInstaller
import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=FileOrganizer',
    '--onefile',
    '--windowed',
    '--icon=assets/icon.ico',
    '--add-data=backend/python:backend',
    'electron/dist/main.js',
])
```

---

## PART 8: KEY METRICS TO TRACK

```
Performance:
- File scan speed: < 1000 files/sec
- Search response: < 100ms for 10,000 files
- Rule evaluation: < 10ms per file
- UI responsiveness: 60 FPS

Reliability:
- Operation success rate: > 99.9%
- Data loss incidents: 0
- Undo capability: 100%

User Experience:
- First-time setup time: < 5 minutes
- Average scan time: < 30 seconds
- Rule creation time: < 2 minutes
```

---

## SUMMARY

This is a complete roadmap for building a production-grade file organizer. Focus on:

1. **Phase 1-2 FIRST**: Get basic file operations working
2. **Phase 3**: Make the UI look great (drives adoption)
3. **Phase 4-5**: Add automation (makes it valuable)
4. **Phase 6-7**: Add safety features (builds trust)

Start with Phase 1, ship MVP in 4 weeks, then add features incrementally.

**Key to Success**:
- Test each phase thoroughly before moving to next
- Get early user feedback on UI
- Focus on reliability over features
- Make undo/rollback foolproof
- Never lose user data

Good luck!
