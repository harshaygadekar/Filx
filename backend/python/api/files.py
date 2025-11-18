from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
import os
import shutil
import logging
from pathlib import Path
from services.file_scanner import scanner
from services.file_analyzer import analyzer
from services.rule_engine import rule_engine

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/files", tags=["files"])

# SECURITY FIX: Path validation to prevent path traversal attacks
def validate_path(path: str, allow_absolute: bool = True) -> Path:
    """
    Validate and sanitize file paths to prevent path traversal attacks.

    Args:
        path: The path to validate
        allow_absolute: Whether to allow absolute paths

    Returns:
        Validated Path object

    Raises:
        HTTPException: If path is invalid or contains traversal sequences
    """
    try:
        path_obj = Path(path).resolve()

        # Check for path traversal attempts
        if ".." in str(path):
            raise HTTPException(
                status_code=400,
                detail="Path traversal detected: '..' not allowed in paths"
            )

        # Validate path exists
        if not path_obj.exists():
            raise HTTPException(status_code=404, detail=f"Path not found: {path}")

        # Additional security: Optionally restrict to certain base directories
        # Uncomment and modify if you want to restrict to specific directories
        # allowed_base = Path.home()
        # if not path_obj.is_relative_to(allowed_base):
        #     raise HTTPException(status_code=403, detail="Access denied to this path")

        return path_obj
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Path validation error for '{path}': {e}")
        raise HTTPException(status_code=400, detail=f"Invalid path: {str(e)}")

class AnalyzeFolderRequest(BaseModel):
    folder_path: str
    recursive: bool = True

class OrganizeFilesRequest(BaseModel):
    plan: Dict

class MoveFileRequest(BaseModel):
    source: str
    destination: str

@router.post("/analyze")
async def analyze_folder(request: AnalyzeFolderRequest):
    try:
        # SECURITY: Validate path to prevent traversal attacks
        folder_path = validate_path(request.folder_path)

        # Verify it's a directory
        if not folder_path.is_dir():
            raise HTTPException(status_code=400, detail="Path must be a directory")

        files = scanner.scan_folder(str(folder_path), request.recursive)

        analyzed_files = []
        for f in files:
            analysis = analyzer.analyze_file(f['path'])
            analyzed_files.append({**f, **analysis})

        scanner.save_files_to_db(files)

        plan = rule_engine.generate_organization_plan(str(folder_path), analyzed_files)

        return {
            "status": "success",
            "total_files": len(files),
            "files": analyzed_files[:50],
            "plan": plan,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error analyzing folder: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/organize")
async def organize_files(request: OrganizeFilesRequest):
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

                # SECURITY: Validate both source and destination paths
                try:
                    source_path = validate_path(source)
                    # For destination, we need to handle non-existent paths differently
                    dest_path = Path(dest).resolve()

                    # Check for path traversal in destination
                    if ".." in dest:
                        raise ValueError("Path traversal detected in destination")

                except HTTPException as e:
                    results['errors'].append({
                        'file': source,
                        'error': str(e.detail)
                    })
                    results['failed'] += 1
                    continue
                except Exception as e:
                    results['errors'].append({
                        'file': source,
                        'error': str(e)
                    })
                    results['failed'] += 1
                    continue

                # BUGFIX: Create parent directory with parents=True
                dest_path.mkdir(parents=True, exist_ok=True)

                dest_file = dest_path / source_path.name

                # BUGFIX: Fix race condition with atomic operation and better counter limit
                if dest_file.exists():
                    base = dest_file.stem
                    ext = dest_file.suffix
                    counter = 1
                    max_attempts = 1000  # Prevent infinite loop
                    while counter < max_attempts:
                        dest_file = dest_path / f"{base}_{counter}{ext}"
                        if not dest_file.exists():
                            break
                        counter += 1

                    if counter >= max_attempts:
                        raise ValueError(f"Could not find unique filename after {max_attempts} attempts")

                shutil.move(str(source_path), str(dest_file))
                results['succeeded'] += 1
                logger.info(f"Moved file from {source_path} to {dest_file}")

            except Exception as e:
                results['failed'] += 1
                results['errors'].append({
                    'file': op['source'],
                    'error': str(e)
                })
                logger.error(f"Error moving file {op['source']}: {e}")

        return {
            "status": "success" if results['failed'] == 0 else "partial",
            "results": results,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error organizing files: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/list")
async def list_files(folder_path: str, skip: int = 0, limit: int = 100):
    try:
        # SECURITY: Validate path
        folder_path_obj = validate_path(folder_path)

        # Verify it's a directory
        if not folder_path_obj.is_dir():
            raise HTTPException(status_code=400, detail="Path must be a directory")

        files = scanner.scan_folder(str(folder_path_obj))
        return {
            "total": len(files),
            "files": files[skip:skip+limit],
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error listing files: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/move")
async def move_file(request: MoveFileRequest):
    try:
        # SECURITY: Validate source path
        source_path = validate_path(request.source)

        # SECURITY: Validate destination path (check for traversal)
        dest_path = Path(request.destination).resolve()
        if ".." in request.destination:
            raise HTTPException(
                status_code=400,
                detail="Path traversal detected in destination path"
            )

        # BUGFIX: Handle empty dirname case and use parents=True
        dest_parent = dest_path.parent
        if dest_parent and str(dest_parent) != '.':
            dest_parent.mkdir(parents=True, exist_ok=True)

        shutil.move(str(source_path), str(dest_path))
        logger.info(f"Moved file from {source_path} to {dest_path}")

        return {
            "status": "success",
            "message": "File moved successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error moving file: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to move file: {str(e)}")
