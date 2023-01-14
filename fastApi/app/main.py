'''
This File Contains The Main FastAPI Code
'''
from fastapi import FastAPI, Request

import app.scripts.database as db
import app.scripts.telegram as tl


app = FastAPI()


@app.get("/")
def read_root():
    '''
    It's Just a Sample Function To Test The API
    '''
    return {
        "data": "Hello World!"
    }

@app.post('/webhook/{uuid}')
async def webhook(uuid: str, request: Request):
    '''
    This Function Is Called When A New Message Is Received From Any Webhook
    First It Gets The Chat ID From The Database
    Then It Sends The Message To The User

    Args:
        uuid (str): Webhook URL UUID

    Returns:
        Response: JSON Response
    '''
    headers = request.headers
    chat_id = db.get_telegram_chat_id_by_webhook_url(uuid)
    payload = await request.json()
    request_type = headers["x-github-event"] or headers["x-gitlab-event"]
    tl.send_message_to_user(chat_id, payload, request_type)

    return {
        "isOk": True
    }
