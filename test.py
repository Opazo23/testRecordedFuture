import sqlite3
from flask import Flask, request

app = Flask(__name__)

PI_KEY = "AKIAIOSFODNN7EXAMPLE"  # fake AWS key
@app.route("/user")
def search_user():
    # CodeQL detecta claramente que entrada del usuario (request.args)
    # va directo a la query SQL sin sanitizar
    user_input = request.args.get("username")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = "SELECT * FROM testonum WHERE username = ?"
    cursor.execute(query, (user_input,))

    return cursor.fetchall()
