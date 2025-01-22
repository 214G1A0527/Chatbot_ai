from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..agents.chat_agent import ChatAgent
import os

router = APIRouter()
chat_agent = ChatAgent(os.getenv("DATABASE_URL"))

class ChatMessage(BaseModel):
    message: str

@router.post("/chat")
async def chat(message: ChatMessage):
    try:
        response = chat_agent.process_query(message.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 