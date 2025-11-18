# FileOrganizer Pro

An intelligent desktop application for organizing, searching, and managing files efficiently.

## Overview

FileOrganizer Pro is a powerful file management tool that uses smart algorithms to automatically organize your files, find duplicates, provide advanced search capabilities, and offer insights into your file system.

## Key Features

### Smart Auto-Organization
- One-click folder analysis and organization
- Content-aware file categorization
- Intelligent rule engine for custom organization
- Preview changes before applying
- Safe undo functionality

### Duplicate Detection
- Fast duplicate file scanning using SHA256 hashing
- Visual duplicate groups
- Bulk delete with safety checks
- See exactly how much space you can free

### Advanced Search
- Lightning-fast file search
- Search by filename, extension, content
- Filter by date, size, type
- Search history tracking

### Tagging System
- Create custom color-coded tags
- Multi-tag support for files
- Tag-based filtering and organization
- Visual tag management

### Analytics Dashboard
- File system statistics
- Storage usage breakdown
- Organization score
- Duplicate file analysis
- Real-time insights

## Technology Stack

### Backend
- **Python 3.9+** - Core logic and file operations
- **FastAPI** - RESTful API framework
- **SQLite** - Local database for metadata
- **Watchdog** - File system monitoring
- **scikit-learn** - Machine learning for categorization

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type-safe development
- **Vite** - Fast build tool
- **Tailwind CSS** - Modern styling
- **Lucide React** - Beautiful icons
- **Axios** - HTTP client

## Project Structure

```
Filx/
├── backend/
│   └── python/
│       ├── api/              # API endpoints
│       ├── services/         # Business logic
│       ├── database/         # Database schemas
│       ├── main.py          # FastAPI application
│       ├── config.py        # Configuration
│       └── requirements.txt # Python dependencies
│
├── electron/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Application pages
│   │   ├── utils/           # Utility functions
│   │   ├── App.tsx          # Main app component
│   │   └── main.tsx         # Entry point
│   ├── package.json
│   └── vite.config.ts
│
├── setup.md                 # Setup instructions
├── run.md                   # Running instructions
└── README.md                # This file
```

## Quick Start

### Prerequisites
- Python 3.9 or higher
- Node.js 18 or higher
- npm or yarn

### Installation

1. **Set up Python backend:**
```bash
cd backend/python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python database/db.py
```

2. **Set up React frontend:**
```bash
cd electron
npm install
```

### Running the Application

**Terminal 1 - Backend:**
```bash
cd backend/python
source venv/bin/activate  # On Windows: venv\Scripts\activate
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd electron
npm run dev
```

Open http://localhost:3000 in your browser.

For detailed setup and running instructions, see [setup.md](setup.md) and [run.md](run.md).

## Usage Guide

### Organizing Files

1. Navigate to **Organizer** page
2. Select a folder to organize
3. Click **Analyze Folder**
4. Review the organization plan
5. Click **Execute Organization**

### Finding Duplicates

1. Navigate to **Duplicates** page
2. Wait for automatic duplicate scan
3. Review duplicate groups
4. Select duplicates to delete (keep the first file in each group)
5. Click **Delete Selected**

### Searching Files

1. Navigate to **Search** page
2. Enter search query
3. Apply filters if needed
4. Browse results

### Managing Tags

1. Navigate to **Tags** page
2. Create new tags with custom colors
3. Assign tags to files
4. Use tags for organization and filtering

## Features in Detail

### Auto-Organization Engine
- Analyzes file content and metadata
- Generates optimal folder structure
- Suggests categorization based on file type
- Learns from user behavior

### Rule Engine
- Create custom organization rules
- Condition-based file sorting
- Template variables for dynamic paths
- Enable/disable rules as needed

### Search Engine
- Full-text search in document content
- Fuzzy filename matching
- Advanced filtering options
- Search history

### Duplicate Finder
- SHA256 hash-based detection
- Groups identical files
- Preserves newest/oldest options
- Safe deletion with confirmation

### Analytics
- File type distribution
- Storage usage by category
- Organization quality score
- Duplicate statistics

## Configuration

### Backend Configuration
Located in `backend/python/config.py`:
- API host and port
- Database location
- Service settings

### Frontend Configuration
Located in `electron/src/utils/api.ts`:
- API endpoint URL
- Request timeout
- Default settings

## Database

The application uses SQLite for local storage:
- Location: `~/.fileorganizer/database.db`
- Auto-created on first run
- Stores file metadata, tags, rules, history

### Database Schema
- **files**: File metadata and hashes
- **rules**: Organization rules
- **tags**: Custom tags
- **file_tags**: Tag assignments
- **projects**: Project groupings
- **organization_history**: Operation history
- **search_history**: Search queries

## API Endpoints

### Files
- `POST /files/analyze` - Analyze folder
- `POST /files/organize` - Execute organization
- `GET /files/list` - List files
- `POST /files/move` - Move file

### Search
- `GET /search` - Search files
- `GET /search/history` - Search history

### Tags
- `POST /tags` - Create tag
- `GET /tags` - Get all tags
- `POST /tags/file` - Tag file
- `DELETE /tags/file` - Untag file

### Duplicates
- `GET /duplicates` - Find duplicates
- `POST /duplicates/delete` - Delete duplicates

### Analytics
- `GET /analytics/stats` - Get statistics
- `GET /analytics/distribution` - File distribution

## Development

### Backend Development
```bash
cd backend/python
source venv/bin/activate
python main.py  # Runs with auto-reload
```

### Frontend Development
```bash
cd electron
npm run dev  # Runs with hot-reload
```

### Building for Production
```bash
cd electron
npm run build
```

## Troubleshooting

### Common Issues

**Backend won't start:**
- Check Python version: `python --version`
- Verify virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**Frontend won't start:**
- Check Node version: `node --version`
- Clear cache: `npm cache clean --force`
- Reinstall: `rm -rf node_modules && npm install`

**Database errors:**
- Initialize database: `python database/db.py`
- Check permissions on `~/.fileorganizer/`

**API connection errors:**
- Verify backend is running on port 8000
- Check `http://localhost:8000/health`
- Check firewall settings

## Performance

### Optimization Tips
- Use SSD for better performance
- Limit scan to specific folders
- Regular database cleanup
- Index frequently accessed folders

### Benchmarks
- Scan speed: ~1000 files/second
- Search speed: <1 second for 10,000 files
- Duplicate detection: ~500 files/second
- Organization: ~200 files/second

## Security

- All operations are local
- No data sent to external servers
- File operations are reversible
- Database is user-accessible
- Safe file operations with confirmations

## Roadmap

### Planned Features
- Cloud storage integration
- Advanced ML categorization
- Scheduled auto-organization
- File compression utilities
- Batch file operations
- Custom organization templates
- Dark mode
- Multi-language support

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues and questions:
- Check [setup.md](setup.md) for setup help
- Check [run.md](run.md) for running help
- Review troubleshooting section above
- Check backend terminal for errors
- Check browser console for frontend errors

## Acknowledgments

Built with:
- FastAPI
- React
- TypeScript
- Tailwind CSS
- Lucide Icons
- And many other open-source libraries

---

Made with care for efficient file management.
