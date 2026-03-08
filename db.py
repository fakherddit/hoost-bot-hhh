# إدارة قاعدة البيانات
import sqlite3

DB_PATH = 'bot_host.db'

def get_conn():
    return sqlite3.connect(DB_PATH)

def add_user(user_id, username):
    conn = get_conn()
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()

def add_bot(user_id, token):
    conn = get_conn()
    c = conn.cursor()
    c.execute('INSERT INTO bots (user_id, token, status) VALUES (?, ?, ?)', (user_id, token, 'stopped'))
    conn.commit()
    conn.close()

def get_user_bots(user_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute('SELECT id, token, status FROM bots WHERE user_id=?', (user_id,))
    bots = c.fetchall()
    conn.close()
    return bots
