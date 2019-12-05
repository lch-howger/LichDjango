import sqlite3
from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import parse_qs

sql_select_text = "SELECT * FROM stars WHERE star='{}' AND time='{}'"
filename_db = '../db.sqlite3'


# db = sqlite3.connect('./stars.db', check_same_thread=False)


def get_text(star, time):
    db = sqlite3.connect('./LichDjangoTest/stars.db')
    cursor = db.cursor()
    cursor.execute(sql_select_text.format(star, time))
    db.commit()
    records = cursor.fetchall()
    cursor.close()
    return records


def index(request):
    context = {}
    return render(request, 'index.html', context)


def stars(request):
    if request.method == 'GET':
        # context = {}
        # return render(request, 'stars.html', context)
        return HttpResponse('GET')
    elif request.method == 'POST':

        # body = request.body.decode('utf-8')
        # qs = parse_qs(body)
        # star = qs.get('star')
        # time = qs.get('time')
        #
        # text = get_text(star, time)

        return HttpResponse('POST')
