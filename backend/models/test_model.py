from sqlalchemy import Column, Integer, String
from .base import Base

class TestTable(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
