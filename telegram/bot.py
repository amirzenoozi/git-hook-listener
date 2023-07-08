"""
This is the main file of the telegram bot.
"""
import sqlite3
import os
import uuid
import telebot

import scripts.database as db

app = telebot.TeleBot("1849393294:AAHG0nwoHgwSIC4dOnmMOB-3SqDrMgzl-aU")
db_connection = sqlite3.connect('./volume/webhook.db')
db_cursor = db_connection.cursor()

try:
    USER_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id CHAR(50),
        chat_id CHAR(50),
        Name CHAR(50)
    );'''
    db_cursor.executescript(USER_TABLE_QUERY)
    LINK_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id CHAR(50),
        link CHAR(150),
        FOREIGN KEY (user_id) REFERENCES BotUsers (user_id)
    );'''
    db_cursor.executescript(LINK_TABLE_QUERY)
except sqlite3.Error as error:
    print(error)

db_connection.commit()
db_connection.close()

@app.message_handler(commands=['start'])
def start_bot(messages):
    """
    Start Bot Function

    Args:
        messages (Message): Telegram Message Object
    """
    user_uuid = str(uuid.uuid4())
    if messages.reply_to_message is not None:
        thread_id = messages.reply_to_message.message_thread_id
    else:
        thread_id = ''
    app.send_message(
        chat_id=messages.chat.id,
        text=f'Wellcome Dear {messages.from_user.first_name}👋🏻',
        parse_mode='Markdown',
        message_thread_id=thread_id,
    )
    db.insert_bot_user(user_uuid, messages.from_user.id, messages.from_user.first_name)


@app.message_handler(commands=['new'])
def get_webhook_url(messages):
    """
    Generate Webhook URL For Each User
    """
    webhook_address_uuid = f'{str(uuid.uuid4())}'
    base_url = os.getenv('BASE_URL')
    if messages.reply_to_message is not None:
        thread_id = messages.reply_to_message.message_thread_id
    else:
        thread_id = ''


    app.send_message(
        chat_id=messages.chat.id,
        text=f'Dear {messages.from_user.first_name} Please Check Your Direct Messages!',
        message_thread_id=thread_id,
    )
    app.send_message(
        chat_id=messages.from_user.id,
        text=f'''Please Add Generated Url To Your Gitlab Repo 🦊.
        \n\nYour Webhook URL:
        \n`{base_url}/webhook/{webhook_address_uuid}`''',
        parse_mode='Markdown',
    )
    db.insert_user_webhook_url(messages.from_user.id, webhook_address_uuid)


if __name__ == '__main__':
    # Running Telegram Bot
    print("We Are Starting The Bot...")
    app.infinity_polling()
