
import sqlite3

def validate_database():
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users(name) VALUES ('Alice')")

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count > 0:
        print("Database validation passed ✅")
    else:
        print("Database validation failed ❌")

    conn.close()

if __name__ == "__main__":
    validate_database()
