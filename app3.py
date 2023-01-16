from flask import Flask
import sqlite3

connection = sqlite3.connect("todos.db")
cursor = connection.cursor()

#cursor.execute("create table todos_list (todos_name text, todos text)")

app = Flask(__name__)

list = ("asddddddddddddddf", "sadfas23232")

@app.route("/")
def index():
    return list

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)