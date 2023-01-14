"""
Database Scripts
"""
import sqlite3

def get_telegram_chat_id_by_webhook_url(webhook_url):
    """
    Get Telegram Chat ID By Webhook URL

    Args:
        webhook_url (str): Webhook URL

    Returns:
        int: Telegram Chat ID
    """
    db_connection = sqlite3.connect('./app/volume/webhook.db')
    db_cursor = db_connection.cursor()

    # Check User is Exist Or Not
    user_id_query = """SELECT user_id FROM links WHERE link = (?) LIMIT 1"""
    user_id = db_cursor.execute(user_id_query, (webhook_url,)).fetchone()
    user_chat_id_query = """SELECT chat_id FROM users WHERE user_id = (?) LIMIT 1"""
    user = db_cursor.execute(user_chat_id_query, (user_id[0],)).fetchone()

    # Close DB Connection
    db_connection.commit()
    db_connection.close()

    return user[0]
