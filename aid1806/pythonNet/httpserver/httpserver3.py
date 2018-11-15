#coding=utf-8

'''
name:钟建
time:2018-8-28
功能：httpserver部分

'''
from threading import Thread
from socket import *
import sys
from setting import *
import re


#处理http请求类
class HTTPServer(object):
    def __init__(self,application): #application就是webframe里的call
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        #获取模块接口
        self.application = application

    def bind(self,host,port):
        self.host = host
        self.port = port
        self.s.bind((self.host,self.port))

    #启动服务器
    def serve_forever(self):
        self.s.listen(5)
        print('Listen the port %d...' % self.port)
        while True:
            c,addr = self.s.accept()
            print('connect from',addr)
            handler_client = Thread(target= \
                self.client_handler,args=(c,))
            handler_client.setDaemon(True)
            handler_client.start()

    def client_handler(self,c):
        #接受浏览器request
        request = c.recv(4096)
        print(request)
        #可以分析请求头和请求体
        request_lines = request.splitlines()
        #获取请求行内容
        request_line = request_lines[0].decode('utf-8')
        #获取请求方法和请求内容
        try:
            env = re.match(r'(?P<METHOD>[A-Z]+)\s+(?P<PATH_INFO>/\S*)', \
                request_line).groupdict()

        except:
            response_headlers = 'HTTP/1.1 500 SERVER ERROR'
            response_headlers += '\r\n'
            response_body = 'server error'
            response = response_headlers + response_body
            c.send(response.encode())


        # method,filename = \
        # re.findall(r'^([A-Z]+)\s+(/\S*)',request_line)[0]
        
        # #将解析内容合成字典给web frame使用
        # env = {'METHOD':method,'PATH_INFO':filename}
        # print(env)

        #将env给Frame 处理，得到返回内容
        response = self.application(env)

        #发送给客户端
        if response:
            c.send(response.encode())
            c.close()

if __name__ == '__main__':
    #将要使用的模块导入进来
    sys.path.insert(1,MODULE_PATH)
    m = __import__(MODULE)
    application = getattr(m,APP)


    httpd = HTTPServer(application)
    httpd.bind(HOST,PORT)
    httpd.serve_forever()




















