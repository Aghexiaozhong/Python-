

import gevent
#在socket导入之前使用
from gevent import monkey
monkey.patch_all()
from socket import *
from time import ctime

def server(port):
    s = socket()
    s.bind(('0.0.0.0',port))
    s.listen(5)

    while True:
        print('Waiting for connect...')
        c,addr = s.accept()
        print('connect from',addr)
        
        gevent.spawn(handler,c)

#处理客户端请求
def handler(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
            
        print('Receive:',data)
        c.send(ctime().encode())
    c.close()

if __name__ == '__main__':
    server(8888)


















