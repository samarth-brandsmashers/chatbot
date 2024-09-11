from pydantic import BaseModel

class MessageCreate(BaseModel):
    text: str
    user_id: int

class MessageUpdate(BaseModel):
    text: str
