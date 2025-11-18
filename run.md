# FileOrganizer Pro - Running Guide

This guide explains how to run FileOrganizer Pro after completing the setup.

## Quick Start

You need to run **two processes**: the Python backend and the React frontend.

### Option 1: Using Two Terminals (Recommended for Development)

#### Terminal 1: Start Python Backend

1. Open a terminal/command prompt
2. Navigate to the backend directory:
```bash
cd backend/python
```

3. Activate virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. Start the backend:
```bash
python main.py
```

You should see:
```
FileOrganizer Pro API started
Database: /home/user/.fileorganizer/database.db
INFO:     Uvicorn running on http://127.0.0.1:8000
```

Keep this terminal running!

#### Terminal 2: Start React Frontend

1. Open a **new** terminal/command prompt
2. Navigate to the electron directory:
```bash
cd electron
```

3. Start the development server:
```bash
npm run dev
```

You should see:
```
VITE v5.0.11  ready in XXX ms
➜  Local:   http://localhost:3000/
```

4. Open your browser and navigate to: http://localhost:3000

The application should now be running!

### Option 2: Using Visual Studio Code

1. Open the project in VS Code
2. Open two integrated terminals (Terminal > New Terminal)
3. Follow the same steps as Option 1

**Pro Tip:** Use VS Code's split terminal feature:
- Click the split terminal icon in the terminal panel
- Run backend in the left terminal
- Run frontend in the right terminal

## Using the Application

### 1. Dashboard
- View overall statistics about your files
- See organization score and duplicate file information
- Quick access to organize folders and find duplicates

### 2. File Organizer
- Click "Organize Folder"
- Select a folder to analyze
- Review the organization plan
- Execute the organization

**Example:**
1. Click "Browse" button
2. Select a folder like "Downloads"
3. Click "Analyze Folder"
4. Review where files will be moved
5. Click "Execute Organization"

### 3. Search
- Search for files by name, extension, or content
- Filter results by type, date, size
- View file details and locations

### 4. Tags
- Create custom tags with colors
- Assign tags to files for better organization
- Filter files by tags

### 5. Duplicates
- Automatically find duplicate files
- See how much space duplicates are wasting
- Select and delete duplicates safely

### 6. Settings
- Configure application preferences
- Change theme
- View about information

## Stopping the Application

### Stop Frontend:
- Press `Ctrl+C` in the frontend terminal
- Or close the browser tab and stop the terminal

### Stop Backend:
- Press `Ctrl+C` in the backend terminal

## Production Build (Optional)

To build the application for production:

### Build Frontend:
```bash
cd electron
npm run build
```

This creates optimized production files in `electron/dist/`.

### Run Backend in Production:
```bash
cd backend/python
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Troubleshooting

### Backend Won't Start

**Error: "Port 8000 is already in use"**
- Another instance is already running
- Kill the process using port 8000:
  - **Windows:** `netstat -ano | findstr :8000` then `taskkill /PID <PID> /F`
  - **macOS/Linux:** `lsof -ti:8000 | xargs kill -9`

**Error: "Module not found"**
- Virtual environment not activated
- Run: `pip install -r requirements.txt`

**Error: "Database error"**
- Initialize database: `python database/db.py`
- Check permissions on ~/.fileorganizer/ directory

### Frontend Won't Start

**Error: "Cannot find module"**
- Run: `npm install`
- Clear cache: `npm cache clean --force`

**Error: "Port 3000 is already in use"**
- Change port in `electron/vite.config.ts`
- Or kill process on port 3000

### Application Loads But Shows Errors

**"Backend not running" or connection errors:**
1. Check backend is running on http://localhost:8000
2. Test backend: Open http://localhost:8000 in browser
3. Check firewall isn't blocking port 8000

**API errors when using features:**
1. Check backend terminal for error messages
2. Verify database was initialized
3. Check file permissions for folders you're trying to organize

## Performance Tips

1. **Large Folders**: When organizing folders with 10,000+ files:
   - Be patient, analysis may take 30-60 seconds
   - Backend will show progress in terminal

2. **Duplicate Detection**: Scanning for duplicates calculates file hashes:
   - Can be slow on HDDs
   - SSDs recommended for best performance

3. **Search**: First search may be slow:
   - Subsequent searches are faster
   - Database indexes improve over time

## Keyboard Shortcuts (In Browser)

- `Ctrl+R` or `Cmd+R`: Refresh page
- `F12`: Open developer tools (for debugging)
- `Ctrl+F` or `Cmd+F`: Search on current page

## Auto-Start on Boot (Optional)

### Windows:
1. Create shortcut to start scripts
2. Place in: `shell:startup`

### macOS:
1. Create .command files for start scripts
2. Add to Login Items in System Preferences

### Linux:
1. Create .desktop files
2. Add to autostart directory

## Best Practices

1. **Before Organizing**:
   - Review the organization plan carefully
   - Start with a small test folder first
   - Ensure you have backups of important files

2. **Regular Maintenance**:
   - Run duplicate finder monthly
   - Keep tags organized and meaningful
   - Update organization rules as needed

3. **Database**:
   - Located at ~/.fileorganizer/database.db
   - Backup this file to preserve tags and history
   - Clear old search history periodically

## Logs and Debugging

### Backend Logs:
- Shown in backend terminal
- Check for error messages if features aren't working

### Frontend Logs:
- Press F12 in browser
- Check Console tab for errors
- Check Network tab for API call failures

## Getting Help

If issues persist:
1. Check both terminal outputs for errors
2. Verify all setup steps were completed
3. Ensure Python and Node.js meet minimum versions
4. Test backend directly: http://localhost:8000/health
5. Check that database file exists and has write permissions

## Next Steps

Now that the application is running:
1. Start with the Dashboard to see your file statistics
2. Try organizing a small test folder
3. Create some tags for your common file types
4. Run duplicate detection to free up space
5. Explore the search functionality

Enjoy using FileOrganizer Pro!
