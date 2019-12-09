import time
import os

abspath = os.path.abspath('.')
path = os.path.join(abspath, 'test.txt')

str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

file = open('./test.txt', 'a')
file.write('AAA------' + str + '\n')
file.close()
