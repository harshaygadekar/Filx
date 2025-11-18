# FileOrganizer Pro - Setup Guide

This guide will help you set up FileOrganizer Pro on your system.

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.9 or higher**
   - Download from: https://www.python.org/downloads/
   - Verify installation: `python --version` or `python3 --version`

2. **Node.js 18 or higher**
   - Download from: https://nodejs.org/
   - Verify installation: `node --version`

3. **npm or yarn**
   - Comes with Node.js
   - Verify installation: `npm --version`

## Installation Steps

### Step 1: Clone or Download the Project

If you have Git installed:
```bash
git clone <repository-url>
cd Filx
```

### Step 2: Set Up Python Backend

1. Navigate to the Python backend directory:
```bash
cd backend/python
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

5. Initialize the database:
```bash
python database/db.py
```

You should see: "Database initialized at ..."

### Step 3: Set Up Electron Frontend

1. Navigate to the Electron directory:
```bash
cd ../../electron
```

2. Install Node.js dependencies:
```bash
npm install
```

This may take a few minutes as it downloads all required packages.

### Step 4: Verify Installation

1. Check that all Python packages are installed:
```bash
cd ../backend/python
pip list
```

You should see packages like fastapi, uvicorn, watchdog, etc.

2. Check that all Node packages are installed:
```bash
cd ../../electron
ls node_modules
```

You should see directories for react, axios, lucide-react, etc.

## Troubleshooting

### Python Issues

If you encounter "python not found":
- Try using `python3` instead of `python`
- Ensure Python is added to your PATH

If pip install fails:
- Update pip: `python -m pip install --upgrade pip`
- Try installing packages individually if one fails

### Node.js Issues

If npm install fails:
- Clear npm cache: `npm cache clean --force`
- Delete node_modules and package-lock.json, then run `npm install` again

If you get permission errors:
- Don't use sudo on macOS/Linux
- Run terminal as Administrator on Windows

### Database Issues

If database initialization fails:
- Check that you have write permissions in your home directory
- The database will be created at `~/.fileorganizer/database.db`
- Manually create the directory if needed: `mkdir ~/.fileorganizer`

## Configuration

### Python Backend Configuration

The backend is configured in `backend/python/config.py`. Default settings:
- API Host: 127.0.0.1
- API Port: 8000
- Database: ~/.fileorganizer/database.db

You can modify these by creating a `.env` file in `backend/python/`:
```
API_HOST=127.0.0.1
API_PORT=8000
```

### Frontend Configuration

The frontend API endpoint is configured in `electron/src/utils/api.ts`:
- Default: http://localhost:8000

Make sure this matches your Python backend port.

## Next Steps

Once setup is complete, proceed to `run.md` to learn how to start the application.

## System Requirements

### Minimum Requirements:
- 2 GB RAM
- 500 MB free disk space
- Python 3.9+
- Node.js 18+

### Recommended:
- 4 GB RAM
- 1 GB free disk space
- Python 3.10+
- Node.js 20+

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure all prerequisites are installed
3. Verify you're in the correct directory for each step
4. Check that your firewall isn't blocking port 8000
