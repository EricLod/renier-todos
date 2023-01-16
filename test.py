from flask import Flask, render_template, request, url_for, redirect, g
import sqlite3

DATABASE = 'todo.db'

def connect_db():
    return sqlite3.connect(DATABASE)

#app.before_request
def before_request():
    g.db = connect_db()

#app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

#app.route('/')
def home():
    cur = g.db.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    return render_template('home.html', todos=todos)

g.db.execute('CREATE TABLE todos (id INTEGER PRIMARY KEY, task TEXT)')
