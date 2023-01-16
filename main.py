from flask import Flask, request,
import sqlite3
from sqlite3 import Error
import functions as f

app = Flask(__name__)
database = r"C:\sqlite\db\pythonsqlite.db"
table_name = "todos"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


conn = create_connection(database)

#f.select_all_tasks(conn, table_name)


if __name__ == "__main__":
    app.run()
