import os
import sqlite3

sql_create_table = 'CREATE TABLE stars_star (id TEXT NOT NULL, star TEXT NOT NULL, time TEXT NOT NULL, text TEXT NOT NULL)'
filename_db = '../db.sqlite3'

# connect to the database and get the cursor
db = sqlite3.connect(filename_db)
cursor = db.cursor()

# create database and table
cursor.execute(sql_create_table)
db.commit()
cursor.close()
