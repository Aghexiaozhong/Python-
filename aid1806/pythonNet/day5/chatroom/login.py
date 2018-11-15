#login.py

import random 
from socket import *
from majiang_database import MyDatabase
from time import *
import os,sys
from select import *

d = MyDatabase()
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#设置epoll对象
p = epoll()
#创建地图
fdmap = {s.fileno():s}

#添加关注
p.register(s,EPOLLIN | EPOLLERR)


sockfd = socket()
sockfd.connect(('0.0.0.0',8888))  #绑定麻将服务器
p.register(sockfd,EPOLLIN | EPOLLERR)
fdmap[sockfd.fileno()] = sockfd

def zhuce(lx):
    print('检测是用户是否存在')
    name = lx[1]
    mima = lx[2]
    shoujihao = lx[3]
    nicheng = lx[4]
    if d.check_usrexist(name): #检测账号
        print('用户存在')
        fdmap[fd].send('True'.encode())
        d.insert_user(name,mima,shoujihao,nicheng)
        print(9999)
    else:
        print(777)
        fdmap[fd].send('False'.encode())

def denglu(lx):
    print(lx)
    name = lx[1]
    mima = lx[2]
    if d.check_login(name,mima):
        fdmap[fd].send('True'.encode())
        global mingzi
        mingzi = name
    else:
        fdmap[fd].send('False'.encode())


while True:
    events = p.poll()
    for fd,event in events:
        try:
            if fd == s.fileno():
                c,addr = fdmap[fd]
                print('Connect from',addr)
                p.register(c,EPOLLIN)
                fdmap[c.fileno()] = c
            elif event & EPOLLIN:
                data = fdmap[fd].recv(2048)
                print(data.decode())
                if not data:
                    p.unregister(fd)
                    fdmap[fd].close()
                    del fdmap[fd]
                jie = data.decode()















