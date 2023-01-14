"""
Database Scripts
"""
import sqlite3

def insert_bot_user(usre_id, chat_id, name):
    """
    Insert New User To Database

    Args:
        usre_id (int): Generated UUID
        chat_id (int): Telegram Chat ID
        name (str): Telegram User Name
    """
    db_connection = sqlite3.connect('./volume/webhook.db')
    db_cursor = db_connection.cursor()
    # Check User is Exist Or Not
    find_user_query = """SELECT chat_id FROM users WHERE chat_id = (?) LIMIT 1"""
    user = db_cursor.execute(find_user_query, (chat_id,)).fetchone()
    # Insert New User
    if not user:
        try:
            add_user_query = """INSERT INTO users (user_id, chat_id, name) VALUES (?, ?, ?)"""
            db_cursor.execute(add_user_query, (usre_id, chat_id, name))
        except sqlite3.Error as error:
            print(error)

    # Close DB Connection
    db_connection.commit()
    db_connection.close()


def insert_user_webhook_url(chat_id, link):
    """
    Insert New User Webhook URL To Database
    """
    db_connection = sqlite3.connect('./volume/webhook.db')
    db_cursor = db_connection.cursor()
    # Check User is Exist Or Not
    find_user_query = """SELECT chat_id FROM users WHERE chat_id = (?) LIMIT 1"""
    user = db_cursor.execute(find_user_query, (chat_id,)).fetchone()
    find_link_query = """SELECT id FROM links WHERE user_id = (?) AND link = (?) LIMIT 1"""
    link_record = db_cursor.execute(find_link_query, (user[0], link)).fetchone()

    # Insert New User
    if not link_record:
        try:
            add_link_query = """INSERT INTO links (user_id, link) VALUES (?, ?)"""
            db_cursor.execute(add_link_query, (user[0], link))
        except sqlite3.Error as error:
            print(error)

    # Close DB Connection
    db_connection.commit()
    db_connection.close()
