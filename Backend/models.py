from typing import Optional, List
from pydantic import BaseModel

class Message(BaseModel):
    id: Optional[int] = None
    text: str
    user_id: int
    suggestions: Optional[List[str]] = None  
