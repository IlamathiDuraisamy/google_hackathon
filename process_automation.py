import sqlite3

def fetch_all_records():
    conn = sqlite3.connect('automation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documents")
    records = cursor.fetchall()
    conn.close()

    print("Documents in Database:")
    for record in records:
        print(record)

def search_document(keyword):
    conn = sqlite3.connect('automation.db')
    cursor = conn.cursor()
    query = "SELECT * FROM documents WHERE extracted_text LIKE ?"
    cursor.execute(query, ('%' + keyword + '%',))
    results = cursor.fetchall()
    conn.close()

    if results:
        print(f"Documents containing '{keyword}':")
        for result in results:
            print(result)
    else:
        print("No matching documents found.")

def update_status(document_id, status):
    conn = sqlite3.connect('automation.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE documents SET processed_status = ? WHERE id = ?", (status, document_id))
    conn.commit()
    conn.close()
    print(f"Updated document ID {document_id} to status: {status}")

fetch_all_records()
search_document("invoice")
update_status(1, "Processed")
