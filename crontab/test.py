import urllib.request
import re
import sqlite3
from lxml import html

url = 'https://www.d1xz.net/yunshi/tomorrow/Gemini'

# 请求得到response
response = urllib.request.urlopen(url)
decode = response.read().decode()

# print(decode)

# 用etree来解析
etree = html.etree
etree_html = etree.HTML(decode)

# 从html中取出元素class
xpath = etree_html.xpath('//*[@class="det"] ')
# xpath = etree_html.xpath('//*[@class="det week_det"] ')

result = etree.tostring(xpath[0], encoding='utf-8').decode('utf-8')
print(result)
