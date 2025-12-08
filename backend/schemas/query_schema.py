from pydantic import BaseModel
from typing import TypedDict,Optional
from datetime import datetime


class QueryCreate(BaseModel):
    user_question:str


class QueryResponse(BaseModel):
    id:int
    user_question:str
    generated_sql:Optional[str]=None
    execution_status:str
    error_message:Optional[str]=None
    created_at:datetime
    executed_at:Optional[str]=None

    class Config:
        orm_mode=True