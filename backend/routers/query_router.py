from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.database import get_db
from backend.schemas.query_schema import QueryCreate, QueryResponse
from backend.services.ai_query_service import create_query, get_query_by_id

router = APIRouter(prefix="/api/query", tags=["Query Operations"])


# -------------------------------
# Submit a user natural-language question
# -------------------------------
@router.post("/submit", response_model=QueryResponse)
async def submit_query(payload: QueryCreate, db: AsyncSession = Depends(get_db)):
    new_query = await create_query(db, payload)
    return new_query


# -------------------------------
# Fetch a query by its ID
# -------------------------------
@router.get("/{query_id}", response_model=QueryResponse)
async def get_query(query_id: int, db: AsyncSession = Depends(get_db)):
    result = await get_query_by_id(db, query_id)

    if not result:
        raise HTTPException(status_code=404, detail="Query not found")

    return result
