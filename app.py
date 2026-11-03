import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")

@app.route("/user")
def get_user():
    name = request.args.get("name")
    conn = sqlite3.connect("users.db")
    result = conn.execute(
        "SELECT * FROM users WHERE name = ?", (name,)
    ).fetchall()
    return str(result)

if __name__ == "__main__":
    app.run()
