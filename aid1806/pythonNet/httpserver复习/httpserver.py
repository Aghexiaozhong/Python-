#!/usr/bin/enu python3
#coding=utf-8

from socket import *
from setting import *
import sys
from threading import Thread
import re

class HTTPServer(object):
    def __init__(self,application):
        self.application = application
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    def bind(self,host,port):
        self.host = host
        self.port = port
        self.s.bind((self.host,self.port))

    def serve_forever(self):
        self.s.listen(10)
        print('Listen to the port %d'% self.port)
        while True:
            c,addr = self.s.accept()
            print('connect from',addr)
            handler_client = Thread(target=self.client_handler,args=(c,))
            handler_client.setDaemon(True)
            handler_client.start()

    def client_handler(self,c):
        
        request = c.recv(4094)
        request_lines = request.splitlines()
        request_line = request_lines[0].decode('utf8')
        pattern = r'(?P<MTEHOD>[A-Z]+)\s+(?P<FILE_PATH>\S+)'
        env = re.match(pattern,request_line).groupdict()

        response = self.application(env)
        #等待frame的回复

        if response:
            c.send(response.encode())
            c.close()



if __name__ == '__main__':
    sys.path.insert(1,MODULE_PATH)
    m = __import__(MODULE)
    application = getattr(m,APP)

    httpd = HTTPServer(application)
    httpd.bind(HOST,PORT)
    httpd.serve_forever()


















