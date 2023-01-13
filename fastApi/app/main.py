import app.scripts.database as db
import app.scripts.telegram as tl

from dotenv import load_dotenv
from fastapi import FastAPI, Request

import os


config = load_dotenv(".env")
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "data": "Hello World!"
    }

@app.post('/webhook/{uuid}')
async def webhook(uuid: str, request: Request):
    chatId = db.get_telegram_chat_id_by_webhook_url(uuid)
    payload = await request.json()
    tl.send_message_to_user(chatId, payload)
    
    return {
        "isOk": True
    }
