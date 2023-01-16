import sqlite3
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "manbearpig"

todo_list = []

release_list = [["Eric", "Grand Theft Auto", "state of New Guernsey"],
                ["Grant", "Grand Theft Auto 2", "Anywhere, USA"]]

@app.route("/")
def main():
    #data = get_db()
    #return data[0]
    #return render_template("index.html", all_data=data)
    return release_list

"""
@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
"""

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("groceries.db")
        cursor = db.cursor()
        cursor.execute("select name from groceries")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]
    return all_data

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run()
