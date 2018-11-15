#sock_server.py
#多进程TCP server
from socketserver import *

#创建server 类
class Server(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        #self.request  ===> accept()里返回的套接字
        print('Connect from',\
            self.request.getpeername())
        while True:
            data = self.request.recv(1024).decode()
            if not data:
                break
            print(data)
            self.request.send(b'Receuve your msg')
#创建server 对象
server = Server(('0.0.0.0',8888),Handler)

#启动服务器
server.serve_forever()





