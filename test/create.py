import sqlite3

sql_create = 'create table testdb (time text not null)'

filename_db = '../db.sqlite3'

# connect to the database and get the cursor
db = sqlite3.connect(filename_db)
cursor = db.cursor()

# create database and table
cursor.execute(sql_create)
db.commit()
cursor.close()
