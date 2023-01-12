import scripts.database as db
import scripts.telegram as tl

from dotenv import load_dotenv
from flask import Flask, request, abort

import os


config = load_dotenv(".env")
app = Flask(__name__)

@app.route('/', methods=['POST'])
def welcome():
    if request.method == 'POST':
        return 'Hello World!'
    else:
        abort(400)


@app.route('/webhook/<uuid>', methods=['POST'])
def webhook(uuid):
    chatId = db.get_telegram_chat_id_by_webhook_url(uuid)
    
    if request.method == 'POST':
        tl.send_message_to_user(chatId, request)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':  
    app.run(debug=os.getenv('IS_DEV'))
