import sys
import os
import asyncio

# -----------------------------------
# Add project root to PYTHONPATH
# -----------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Now imports will work
from backend.llm.gemini_sql_generator import generate_sql_from_question


async def test():
    question = "show top 10 products by sales"
    sql = await generate_sql_from_question(question)

    print("====== GENERATED SQL ======")
    print(sql)
    print("===========================")


if __name__ == "__main__":
    asyncio.run(test())
