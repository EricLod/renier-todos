from flask import Flask, redirect, url_for, request
import sqlite3



app = Flask(__name__)

@app.route('/task')
def task():
   return (["asdf", "fdsa", "qwerty"])

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
