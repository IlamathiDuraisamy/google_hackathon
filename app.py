from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def fetch_all_records():
    conn = sqlite3.connect('automation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documents")
    records = cursor.fetchall()
    conn.close()
    return records

@app.route('/')
def index():
    documents = fetch_all_records()
    return render_template('index.html', documents=documents)

if __name__ == '__main__':
    app.run(debug=True)
