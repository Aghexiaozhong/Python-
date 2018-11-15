#httpserver2.py

from socket import *
from threading import Thread
import time

#存放静态页面
STATIC_DIR = './static'

ADDR = ('0.0.0.0',8000)

#HTTPServevr 类用来封装具体的功能
class HTTPServer(object):
    def __init__(self,address):
        #创建套接字
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,\
            SO_REUSEADDR,1)
        self.s.bind(address)
        self.s.listen(5)
        #为对象添加属性变量(为用户提供更多的选择，用不用看他自己)
        self.name = 'HTTPServer'
        self.port = address[1]
        self.address = address

    #启动服务器
    def serve_forever(self):
        print('Listen the port %d' % self.port)
        while True:
            c,addr = self.s.accept()  
            #这里的c 是每个客户端有自己的c，如果self.c 则是全局变量
            #创建线程处理具体请求
            clientThread = Thread(target = self.handleRequest,args = (c,))
            clientThread.setDaemon(True)
            clientThread.start()

    def handleRequest(self,c):
        #接受客户端请求
        request = c.recv(1024).decode()
        #按行切割字符串
        requestHeadlers = request.splitlines()
        #获取请求行
        print(c.getpeername(),':',\
            requestHeadlers[0] )
        #获取请求内容
        getRequest = str(requestHeadlers[0]).split(' ')[1]
        if getRequest == '/' or getRequest[-5:] == '.html':
            data = self.get_html(getRequest)

        else:
            data = self.get_data(getRequest)
        c.send(data.encode())
        c.close()

    def get_html(self,page):
        if page == '/':
            filename = STATIC_DIR + '/index.html'

        else:
            filename = STATIC_DIR + page

        try:
            f = open(filename)
        except Exception:
            #如果没有找到页面
            responseHeadlers = 'HTTP/1.1 404 Not Found\r\n'
            responseHeadlers += 'Connect-Type: text/html\r\n'
            responseHeadlers += '\r\n'
            responseBody = '<h1>Sorry,not found the page</h1>'
        else:
            responseHeadlers = 'HTTP/1.1 200 OK\r\n'
            responseHeadlers += 'Connect-Type: text/html\r\n'
            responseHeadlers += '\r\n'
            responseBody = f.read()

        finally:
            return responseHeadlers + responseBody

    def get_data(self,data):
        responseHeadlers = 'HTTP/1.1 200 OK\r\n'
        responseHeadlers += '\r\n'

        if data == '/time':
            responseBody = time.ctime()

        elif data == '/tedu':
            responseBody = 'Welcome to tedu!'

        elif data == '/favicon.ico':
            f = open(STATIC_DIR + '/favicon.ico')
            responseBody = f.read()

        else:
            responseBody ='The data not found'
        return responseHeadlers + responseBody

if __name__ == '__main__':
    #生成服务器对象
    httpd = HTTPServer(ADDR)
    #启动服务器
    httpd.serve_forever()




















