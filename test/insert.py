import sqlite3
import time

sql_insert = "insert into testdb values('{}')"

str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

db = sqlite3.connect('../db.sqlite3')
cursor = db.cursor()
cursor.execute(sql_insert.format(str))
db.commit()
cursor.close()
