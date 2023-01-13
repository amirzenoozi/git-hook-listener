import scripts.database as db
import sqlite3
import telebot
import os
import uuid

app = telebot.TeleBot(os.getenv('BOT_TOKEN'))
db_connection = sqlite3.connect('./volume/webhook.db')
db_cursor = db_connection.cursor()

try:
    db_cursor.executescript('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id CHAR(50), chat_id CHAR(50), Name CHAR(50));''')
    db_cursor.executescript('''CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id CHAR(50), link CHAR(150), FOREIGN KEY (user_id) REFERENCES BotUsers (user_id));''')
except sqlite3.Error as error:
    print(error)
    pass

db_connection.commit()
db_connection.close()

@app.message_handler(commands=['start'])
def start_bot(messages):
    user_uuid = str(uuid.uuid4())
    app.send_message(messages.chat.id, f'Wellcome Dear {messages.from_user.first_name}👋🏻', parse_mode='Markdown')
    db.insert_bot_user(user_uuid, messages.from_user.id, messages.from_user.first_name)


@app.message_handler(commands=['new'])
def get_webhook_url(messages):
    webhook_address_uuid = f'{str(uuid.uuid4())}'
    base_url = os.getenv('BASE_URL')
    app.send_message(
        messages.chat.id,
        f'Please Add Generated Url To Your Gitlab Ripo 🦊. \n\nYour Webhook URL:\n`{base_url}/webhook/{webhook_address_uuid}`',
        parse_mode='Markdown'
    )
    db.insert_user_webhook_url(messages.from_user.id, webhook_address_uuid)


if __name__ == '__main__':
    # Running Telegram Bot
    print("We Are Starting The Bot...")
    app.infinity_polling()