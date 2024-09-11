from fastapi import APIRouter, HTTPException
from typing import List
from models import Message
from schemas import MessageCreate, MessageUpdate
import session
from chatbot import generate_response, generate_suggestions

router = APIRouter()

next_id = 1

@router.post("/messages/", response_model=Message)
def create_message(session_id: str, message: MessageCreate):
    global next_id

    new_message = Message(id=next_id, **message.model_dump())
    session.add_message_to_session(session_id, new_message)

    bot_response_text = generate_response(new_message.text)

    suggestions = generate_suggestions(new_message.text)

    bot_response = Message(id=next_id + 1, text=bot_response_text, user_id=0, suggestions=suggestions)

    session.add_message_to_session(session_id, bot_response)

    next_id += 2

    return new_message

@router.get("/messages/", response_model=List[Message])
def read_messages(session_id: str):
    return session.get_session_messages(session_id)

@router.put("/messages/{message_id}", response_model=Message)
def update_message(session_id: str, message_id: int, message_update: MessageUpdate):
    updated = session.update_message_in_session(session_id, message_id, message_update.text)
    if updated:
        return next((msg for msg in session.get_session_messages(session_id) if msg.id == message_id), None)
    raise HTTPException(status_code=404, detail="Message not found")

@router.delete("/messages/{message_id}", response_model=Message)
def delete_message(session_id: str, message_id: int):
    deleted = session.delete_message_from_session(session_id, message_id)
    if deleted:
        return next((msg for msg in session.get_session_messages(session_id) if msg.id == message_id), None)
    raise HTTPException(status_code=404, detail="Message not found")
