import sqlite3

def get_telegram_chat_id_by_webhook_url(webhook_url):
    db_connection = sqlite3.connect('./app/volume/webhook.db')
    db_cursor = db_connection.cursor()
    
    # Check User is Exist Or Not
    user_id = db_cursor.execute("""SELECT user_id FROM links WHERE link = (?) LIMIT 1""", (webhook_url,)).fetchone()
    user = db_cursor.execute("""SELECT chat_id FROM users WHERE user_id = (?) LIMIT 1""", (user_id[0],)).fetchone()
    
    # Close DB Connection
    db_connection.commit()
    db_connection.close()

    return user[0]

