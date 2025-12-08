from fastapi import FastAPI, Depends
from backend.db.database import get_db
from sqlalchemy import text
from backend.config.settings import settings
from backend.routers.query_router import router as query_router

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend is running"}

@app.get("/config-check")
def config_check():
    return {
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "log_level": settings.LOG_LEVEL,
        "database_url": settings.DATABASE_URL,
    }

@app.get("/db-test")
async def db_test(db=Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"db_status": result.scalar()}

app.include_router(query_router)
