import sqlite3

conn = sqlite3.connect('automation.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_type TEXT,
    extracted_text TEXT,
    processed_status TEXT DEFAULT 'Pending'
)
''')

conn.commit()
conn.close()

print("Database and table created successfully!")
