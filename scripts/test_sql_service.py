import asyncio

from backend.services.sql_generation_service import generate_sql_service

async def test():
    sql = await generate_sql_service("show top 10 products by sales")
    print("====== SQL FROM SERVICE ======")
    print(sql)

asyncio.run(test())
