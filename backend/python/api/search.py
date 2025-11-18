from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
from services.search_engine import search_engine

router = APIRouter(prefix="/search", tags=["search"])

@router.get("")
async def search(
    q: str,
    file_type: Optional[str] = None,
    date_range: Optional[str] = None,
    min_size: Optional[int] = None,
    max_size: Optional[int] = None
):
    try:
        filters = {}
        if file_type:
            filters['file_type'] = file_type
        if date_range:
            filters['date_range'] = date_range
        if min_size:
            filters['min_size'] = min_size
        if max_size:
            filters['max_size'] = max_size

        results = search_engine.search(q, filters)

        return {
            "query": q,
            "results": results,
            "count": len(results),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/history")
async def get_search_history(limit: int = 10):
    try:
        history = search_engine.get_recent_searches(limit)
        return {
            "history": history,
            "count": len(history),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
