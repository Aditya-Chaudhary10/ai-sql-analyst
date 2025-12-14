# backend/services/sql_generation_service.py

from backend.llm.gemini_sql_generator import generate_sql_from_question


async def generate_sql_service(user_question: str) -> str:
    """
    Service layer wrapper for SQL generation.
    This keeps routers clean and allows future changes
    (LangChain, retries, logging, caching, etc.)
    """
    sql = await generate_sql_from_question(user_question)
    return sql
