
import sqlite3


def get_user(user_input):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Vulnerabilidad de SQL Injection directa:
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()
