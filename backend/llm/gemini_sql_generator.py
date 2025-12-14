import google.generativeai as genai
from backend.config.settings import settings

# Configure Gemini using centralized settings
genai.configure(api_key=settings.GEMINI_API_KEY)


async def generate_sql_from_question(question: str) -> str:
    """
    Takes a natural language question and returns SQL query.
    """

    prompt = f"""
You are an expert PostgreSQL data analyst.

Convert the following question into a valid PostgreSQL SQL query.

Rules:
- Use only SQL
- Do NOT add explanations
- Do NOT add markdown
- Return ONLY the SQL query

Question:
{question}
"""

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text.strip()
