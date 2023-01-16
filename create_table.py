import sqlite3

connection = sqlite3.connect("groceries.db")
cursor = connection.cursor()