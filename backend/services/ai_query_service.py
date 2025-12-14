from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime

from backend.models.ai_query import AIQuery
from backend.schemas.query_schema import QueryCreate
from backend.llm.gemini_sql_generator import generate_sql_from_question


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
    await db.refresh(new_query)

    return new_query


# ------------------------------------
# Fetch a query record by ID
# ------------------------------------
async def get_query_by_id(db: AsyncSession, query_id: int):
    result = await db.execute(
        select(AIQuery).where(AIQuery.id == query_id)
    )
    return result.scalar_one_or_none()


# ------------------------------------
# Generate SQL using Gemini & update DB
# ------------------------------------
async def generate_sql_for_query(
    db: AsyncSession,
    query_id: int
):
    """
    1. Fetch query from DB
    2. Generate SQL using Gemini
    3. Save generated SQL back to DB
    """

    # 1️⃣ Fetch query
    result = await db.execute(
        select(AIQuery).where(AIQuery.id == query_id)
    )
    query_obj = result.scalar_one_or_none()

    if not query_obj:
        raise ValueError("Query not found")

    # 2️⃣ Generate SQL via Gemini
    sql = await generate_sql_from_question(query_obj.user_question)

    # 3️⃣ Update DB
    query_obj.generated_sql = sql
    query_obj.execution_status = "sql_generated"
    query_obj.executed_at = datetime.utcnow()

    await db.commit()
    await db.refresh(query_obj)

    return query_obj
