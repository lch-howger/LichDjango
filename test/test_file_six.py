import time

str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

file = open('test.txt', 'a')
file.write('six------'+str + '\n')
file.close()
