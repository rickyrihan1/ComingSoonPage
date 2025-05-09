# create_db.py
import sqlite3

conn = sqlite3.connect('emails.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE
    )
''')
conn.commit()
conn.close()
