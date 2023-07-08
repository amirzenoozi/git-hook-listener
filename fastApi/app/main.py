"""
This File Contains The Main FastAPI Code
"""
from fastapi import FastAPI, Request

import app.scripts.database as db
import app.scripts.telegram as tl

import os

app = FastAPI()


@app.get("/")
def read_root():
    """
    It's Just a Sample Function To Test The API
    """
    return {
        "data": "Hello World!"
    }

@app.post('/webhook/{uuid}')
async def webhook(uuid: str, request: Request):
    """
    This Function Is Called When A New Message Is Received From Any Webhook
    First It Gets The Chat ID From The Database
    Then It Sends The Message To The User

    Args:
        uuid (str): Webhook URL UUID

    Returns:
        Response: JSON Response
    """
    chat_id = os.getenv('GROUP_CHAT_ID')
    topic_id = os.getenv('CHANGELOG_TOPIC_ID')
    # chat_id = db.get_telegram_chat_id_by_webhook_url(uuid)
    payload = await request.json()
    request_type = payload["object_kind"] or "general"
    tl.send_message_to_single_topic(chat_id, payload, request_type, topic_id)

    return {
        "isOk": True
    }
