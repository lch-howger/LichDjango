import time
import os

abspath = os.path.abspath('.')
path = os.path.join(abspath, 'test.txt')

str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(path)

file = open(path, 'a')
file.write('AAA------' + path + '\n')
file.close()

file = open(path, 'a')
file.write('AAA------' + str + '\n')
file.close()
