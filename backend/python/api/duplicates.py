from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from services.duplicate_finder import duplicate_finder

router = APIRouter(prefix="/duplicates", tags=["duplicates"])

class DeleteDuplicatesRequest(BaseModel):
    file_ids: List[int]

@router.get("")
async def find_duplicates():
    try:
        result = duplicate_finder.find_duplicates()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/delete")
async def delete_duplicates(request: DeleteDuplicatesRequest):
    try:
        result = duplicate_finder.delete_duplicates(request.file_ids)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
