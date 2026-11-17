import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


@app.get("/notes")
def list_notes():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, text FROM notes ORDER BY id")
        rows = cur.fetchall()
    return jsonify([{"id": r[0], "text": r[1]} for r in rows])


@app.post("/notes")
def add_note():
    text = request.get_json()["text"]
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO notes (text) VALUES (%s) RETURNING id", (text,))
        new_id = cur.fetchone()[0]
    return jsonify({"id": new_id, "text": text}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)