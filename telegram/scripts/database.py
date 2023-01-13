import sqlite3

def insert_bot_user(usre_id, chat_id, name):
    db_connection = sqlite3.connect('./volume/webhook.db')
    db_cursor = db_connection.cursor()
    # Check User is Exist Or Not
    user = db_cursor.execute("""SELECT chat_id FROM users WHERE chat_id = (?) LIMIT 1""", (chat_id,)).fetchone()
    # Insert New User
    if not user:
        try:    
            db_cursor.execute("""INSERT INTO users (user_id, chat_id, name) VALUES (?, ?, ?)""", (usre_id, chat_id, name))
        except sqlite3.Error as error:
            print(error)
            pass
    # Close DB Connection
    db_connection.commit()
    db_connection.close()

def insert_user_webhook_url(chat_id, link):
    db_connection = sqlite3.connect('./volume/webhook.db')
    db_cursor = db_connection.cursor()
    # Check User is Exist Or Not
    user = db_cursor.execute("""SELECT user_id FROM users WHERE chat_id = (?) LIMIT 1""", (chat_id,)).fetchone()
    link_record = db_cursor.execute("""SELECT id FROM links WHERE user_id = (?) AND link = (?) LIMIT 1""", (user[0], link)).fetchone()
    # Insert New User
    if not link_record:
        try:
            db_cursor.execute("""INSERT INTO links (user_id, link) VALUES (?, ?)""", (user[0], link))
        except sqlite3.Error as error:
            print(error)
            pass
    # Close DB Connection
    db_connection.commit()
    db_connection.close()

