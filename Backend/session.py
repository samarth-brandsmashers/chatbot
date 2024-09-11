from typing import List, Dict, Optional
from models import Message

sessions: Dict[str, List[Message]] = {}

def add_message_to_session(session_id: str, message: Message):
    if session_id not in sessions:
        sessions[session_id] = []
    sessions[session_id].append(message)

def get_session_messages(session_id: str) -> List[Message]:
    return sessions.get(session_id, [])

def update_message_in_session(session_id: str, message_id: int, new_text: str) -> bool:
    messages = sessions.get(session_id, [])
    for msg in messages:
        if msg.id == message_id:
            msg.text = new_text
            return True
    return False

def delete_message_from_session(session_id: str, message_id: int) -> Optional[Message]:
    messages = sessions.get(session_id, [])
    for i, msg in enumerate(messages):
        if msg.id == message_id:
            return messages.pop(i)
    return None
