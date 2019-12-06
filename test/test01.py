import sqlite3

sql_insert_text = "INSERT INTO stars VALUES ('{}','{}','{}','{}')"
sql_select_text = "SELECT * FROM stars WHERE star='{}' AND time='{}'"
sql_select_user = "SELECT * FROM auth_user"
filename_db = '../db.sqlite3'


def get_users():
    db = sqlite3.connect(filename_db)
    cursor = db.cursor()
    cursor.execute(sql_select_user)
    db.commit()
    records = cursor.fetchall()
    cursor.close()
    return records

get_users()