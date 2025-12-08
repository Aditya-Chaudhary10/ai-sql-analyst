from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.ai_query import AIQuery
from backend.schemas.query_schema import QueryCreate
from datetime import datetime

# ------------------------------------
# Create a new query record in DB
# ------------------------------------
async def create_query(db: AsyncSession, payload: QueryCreate):
    new_query = AIQuery(
        user_question=payload.user_question,
        execution_status="pending",
        created_at=datetime.utcnow()
    )

    db.add(new_query)
    await db.commit()
    await db.refresh(new_query)  # fetch generated id

    return new_query


# ------------------------------------
# Fetch a query record by ID
# ------------------------------------
async def get_query_by_id(db: AsyncSession, query_id: int):
    result = await db.execute(
        select(AIQuery).where(AIQuery.id == query_id)
    )
    return result.scalar_one_or_none()
