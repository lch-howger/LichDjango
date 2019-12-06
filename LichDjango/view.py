import sqlite3
from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import parse_qs
from stars.models import Star

sql_insert_text = "INSERT INTO stars VALUES ('{}','{}','{}','{}')"
sql_select_text = "SELECT * FROM stars WHERE star='{}' AND time='{}'"
sql_select_user = "SELECT * FROM auth_user"
filename_db = '../db.sqlite3'


def stars(request):
    if request.method == 'GET':
        # context = {}
        # return render(request, 'stars.html', context)
        return HttpResponse('GET')
    elif request.method == 'POST':
        body = request.body.decode('utf-8')
        qs = parse_qs(body)
        i = qs.get('id')[0]



        objects = Star.objects.all()
        obj = objects.get(id=i)
        text = obj.text
        star=obj.star

        print(text)

        return HttpResponse(text)


def update_stars(request):
    if request.method == 'POST':
        return HttpResponse('abc')


def get_users():
    db = sqlite3.connect(filename_db)
    cursor = db.cursor()
    cursor.execute(sql_select_user)
    db.commit()
    records = cursor.fetchall()
    cursor.close()
    return records


def test_data(a, b, c, d):
    db = sqlite3.connect(filename_db)
    cursor = db.cursor()
    cursor.execute(sql_insert_text.format(a, b, c, d))
    db.commit()
    cursor.close()
    return False


def get_text(star, time):
    db = sqlite3.connect(filename_db)
    cursor = db.cursor()
    cursor.execute(sql_select_text.format(star, time))
    db.commit()
    records = cursor.fetchall()
    cursor.close()
    return records


def index(request):
    context = {}
    return render(request, 'index.html', context)
