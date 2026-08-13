import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def search_user():
    # CodeQL detecta claramente que entrada del usuario (request.args)
    # va directo a la query SQL sin sanitizar
    user_input = request.args.get("username")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM testonum WHERE username = '{user_input}'"
    cursor.execute(query)

    return cursor.fetchall()
