from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
import os
import shutil
from services.file_scanner import scanner
from services.file_analyzer import analyzer
from services.rule_engine import rule_engine

router = APIRouter(prefix="/files", tags=["files"])

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
        if not os.path.exists(request.folder_path):
            raise HTTPException(status_code=404, detail="Folder not found")

        files = scanner.scan_folder(request.folder_path, request.recursive)

        analyzed_files = []
        for f in files:
            analysis = analyzer.analyze_file(f['path'])
            analyzed_files.append({**f, **analysis})

        scanner.save_files_to_db(files)

        plan = rule_engine.generate_organization_plan(request.folder_path, analyzed_files)

        return {
            "status": "success",
            "total_files": len(files),
            "files": analyzed_files[:50],
            "plan": plan,
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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

                if not os.path.exists(source):
                    results['errors'].append({
                        'file': source,
                        'error': 'Source file not found'
                    })
                    results['failed'] += 1
                    continue

                os.makedirs(dest, exist_ok=True)

                dest_file = os.path.join(dest, os.path.basename(source))

                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(dest_file)
                    counter = 1
                    while os.path.exists(f"{base}_{counter}{ext}"):
                        counter += 1
                    dest_file = f"{base}_{counter}{ext}"

                shutil.move(source, dest_file)
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
    try:
        if not os.path.exists(folder_path):
            raise HTTPException(status_code=404, detail="Folder not found")

        files = scanner.scan_folder(folder_path)
        return {
            "total": len(files),
            "files": files[skip:skip+limit],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/move")
async def move_file(request: MoveFileRequest):
    try:
        if not os.path.exists(request.source):
            raise HTTPException(status_code=404, detail="Source file not found")

        os.makedirs(os.path.dirname(request.destination), exist_ok=True)
        shutil.move(request.source, request.destination)

        return {
            "status": "success",
            "message": "File moved successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
