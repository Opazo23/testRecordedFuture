import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/product")
def search_product():
    category = request.args.get("category")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM products WHERE category = '{category}'"
    cursor.execute(query)
    return str(cursor.fetchall())
