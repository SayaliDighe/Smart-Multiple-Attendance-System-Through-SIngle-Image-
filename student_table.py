import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    mobile TEXT NOT NULL
)
''')

conn.commit()
conn.close()
