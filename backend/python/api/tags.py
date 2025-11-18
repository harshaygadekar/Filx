from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from services.tagging_system import tagging_system

router = APIRouter(prefix="/tags", tags=["tags"])

class CreateTagRequest(BaseModel):
    name: str
    color: str = '#3B82F6'

class TagFileRequest(BaseModel):
    file_id: int
    tag_id: int

@router.post("")
async def create_tag(request: CreateTagRequest):
    try:
        tag = tagging_system.create_tag(request.name, request.color)
        if 'error' in tag:
            raise HTTPException(status_code=400, detail=tag['error'])
        return tag
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("")
async def get_all_tags():
    try:
        tags = tagging_system.get_all_tags()
        return {
            "tags": tags,
            "count": len(tags),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/file")
async def tag_file(request: TagFileRequest):
    try:
        success = tagging_system.tag_file(request.file_id, request.tag_id)
        if not success:
            raise HTTPException(status_code=400, detail="Failed to tag file")
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/file")
async def untag_file(file_id: int, tag_id: int):
    try:
        success = tagging_system.untag_file(file_id, tag_id)
        if not success:
            raise HTTPException(status_code=400, detail="Failed to untag file")
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/file/{file_id}")
async def get_file_tags(file_id: int):
    try:
        tags = tagging_system.get_file_tags(file_id)
        return {
            "tags": tags,
            "count": len(tags),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{tag_id}/files")
async def get_files_by_tag(tag_id: int):
    try:
        files = tagging_system.search_by_tag(tag_id)
        return {
            "files": files,
            "count": len(files),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{tag_id}")
async def delete_tag(tag_id: int):
    try:
        success = tagging_system.delete_tag(tag_id)
        if not success:
            raise HTTPException(status_code=400, detail="Failed to delete tag")
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
