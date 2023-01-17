from flask import Flask, request, url_for, redirect
import sqlite3
from sqlite3 import Error
import functions as f

app = Flask(__name__)
database = r"C:\sqlite\db\pythonsqlite.db"
conn2 = sqlite3.connect(database, check_same_thread=False)
todo_list = [["apples"], ["pears"], ["bananas"], ["grapes"]]


@app.route("/names", methods=["GET"])
def names():
    cur = conn2.cursor()
    cur.execute("SELECT name FROM todos")
    rows = cur.fetchall()
    names_list = []
    if not names_list:
        for row in rows:
            names_list.append(row[0])
    return names_list


@app.route("/namesraw", methods=["GET"])
def namesraw():
    cur = conn2.cursor()
    cur.execute("SELECT name FROM todos")
    rows = cur.fetchall()
    return rows


@app.route("/todos", methods=["GET"])
def todos():
    cur = conn2.cursor()
    cur.execute("SELECT todo_list FROM todos")
    rows = cur.fetchall()
    todos_list = ""
    for row in rows:
        todos_list = todos_list + str(row[0]) + "\n"
    todos_list = todos_list.replace("[", "")
    todos_list = todos_list.replace("]", "")
    return todos_list


@app.route("/todosraw", methods=["GET"])
def todosraw():
    cur = conn2.cursor()
    cur.execute("SELECT todo_list FROM todos")
    rows = cur.fetchall()
    return rows


@app.route("/req_name", methods=["POST"])
def reqname(name):
    req_Json = request.json
    name = req_Json["name"]
    cur = conn2.cursor()
    cur.execute("SELECT * FROM todos")
    rows = cur.fetchall()
    answer = ""
    for row in rows:
        print(row[1])
        if row[1] == name:
            answer = str(row)
    if answer == "":
        answer = "Invalid name..."
    return answer


@app.route("/req_id", methods=["POST"])
def reqid():
    req_Json = request.json
    id = req_Json["id"]
    cur = conn2.cursor()
    cur.execute("SELECT * FROM todos")
    rows = cur.fetchall()
    answer = ""
    for row in rows:
        if str(row[0]) == id:
            answer = str(row)
    if answer == "":
        answer = "Invalid id..."
    return answer


def update_task(conn, task):
    sql = """UPDATE todos
                SET name = ?,
                    todo_list = ?
                WHERE id = ?"""
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    print("Success!")


@app.route("/update_id", methods=["POST"])
def updateid():
    req_Json = request.json
    id = req_Json["id"]
    name = req_Json["name"]
    todos = req_Json["todo_list"]
    todos = str(todos).replace("'", '"')
    todoToUpdate = [str(name), str(todos), id]
    update_task(conn2, todoToUpdate)
    todoToUpdate = {"id": id, "name": name, "todo_list": todos}
    return todoToUpdate


def delete_task(conn, id):
    sql = 'DELETE FROM todos WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    print("Success!")


@app.route("/delete_id", methods=["POST"])
def deleteid():
    req_Json = request.json
    id = req_Json["id"]
    delete_task(conn2, id)
    return id


@app.route("/all", methods=["GET"])
def all():
    cur = conn2.cursor()
    cur.execute("SELECT * FROM todos")
    rows = cur.fetchall()
    return rows


def create_todo(conn, todo_list):
    sql = "INSERT INTO todos (name,todo_list) VALUES(?,?)"
    cur = conn.cursor()
    cur.execute(sql, todo_list)
    conn.commit()
    return cur.lastrowid


def select_todo_by_name(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT id FROM todos WHERE name=?", (name,))
    rows = cur.fetchall()
    idOut = rows[0][0]
    return idOut


@app.route("/add_name", methods=["POST"])
def addname():
    req_Json = request.json
    name = req_Json["name"]
    todos = req_Json["todo_list"]
    output = [name, str(todos)]
    namesList = names()
    proceed = False
    for items in namesList:
        if items == name:
            proceed = True
            break
    if not proceed:
        create_todo(conn2, output)
        id = select_todo_by_name(conn2, name)
        output = {"id":id, "name":name, "todo_list":str(todos)}
    else:
        output = "Name already exists!"
    return output


taskToInsert = ("Ericcc", '[["apples"], ["pears"], ["bananas"], ["grapes"]]')

if __name__ == "__main__":
    app.run()
