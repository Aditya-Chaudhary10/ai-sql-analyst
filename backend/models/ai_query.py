from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .base import Base

class AIQuery(Base):
    __tablename__ = "ai_queries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_question = Column(Text, nullable=False)
    generated_sql = Column(Text, nullable=True)
    execution_status = Column(String(50), default="pending", nullable=False)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    executed_at = Column(DateTime(timezone=True), nullable=True)
