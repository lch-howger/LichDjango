import urllib.request
import re
import sqlite3
from lxml import html

base_url = 'https://www.d1xz.net/yunshi/'
sql_update = "UPDATE stars_star SET text='{}' WHERE id='{}'"
filename_db = '../db.sqlite3'

db = sqlite3.connect(filename_db)

for i in range(12):
    id02 = ''
    star = ''
    if i == 0:
        id02 = '00'
        star = 'Aries'
    elif i == 1:
        id02 = '01'
        star = 'Taurus'
    elif i == 2:
        id02 = '02'
        star = 'Gemini'
    elif i == 3:
        id02 = '03'
        star = 'Cancer'
    elif i == 4:
        id02 = '04'
        star = 'Leo'
    elif i == 5:
        id02 = '05'
        star = 'Virgo'
    elif i == 6:
        id02 = '06'
        star = 'Libra'
    elif i == 7:
        id02 = '07'
        star = 'Scorpio'
    elif i == 8:
        id02 = '08'
        star = 'Sagittarius'
    elif i == 9:
        id02 = '09'
        star = 'Capricorn'
    elif i == 10:
        id02 = '10'
        star = 'Aquarius'
    elif i == 11:
        id02 = '11'
        star = 'Pisces'
    # 拼接id
    id = '02' + id02

    # 拼接url
    url = base_url + 'week' + '/' + star

    # 请求得到response
    response = urllib.request.urlopen(url)
    decode = response.read().decode()

    # 用etree来解析
    etree = html.etree
    etree_html = etree.HTML(decode)

    # 从html中取出元素class
    result = ''
    # xpath = etree_html.xpath('//*[@class="det"] ')
    xpath = etree_html.xpath('//*[@class="det week_det"] ')

    result = etree.tostring(xpath[0], encoding='utf-8').decode('utf-8')
    print(result)

    # 把记录添加到数据库
    cursor = db.cursor()
    cursor.execute(sql_update.format(result, id))
    db.commit()
    cursor.close()
