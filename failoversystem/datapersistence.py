import sqlite3

def initialize_db():
    conn = sqlite3.connect('trading_bot.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS state 
                     (key TEXT PRIMARY KEY, value TEXT)''')
    conn.commit()
    return conn, cursor

def persist_data(key, value):
    cursor.execute("INSERT OR REPLACE INTO state (key, value) VALUES (?, ?)", (key, value))
    conn.commit()

def retrieve_data(key):
    cursor.execute("SELECT value FROM state WHERE key=?", (key,))
    return cursor.fetchone()
