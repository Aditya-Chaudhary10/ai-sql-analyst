import os
from dotenv import load_dotenv

load_dotenv()  # read .env at project root

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "AI_SQL_Analyst")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    REDIS_URL: str = os.getenv("REDIS_URL", "")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")

settings = Settings()
