#!/usr/bin/env python3
#coding=utf-8

'''
name : 迷之自信
date : 2018-6-12
email : lvze@tedu.cn
MOLULES : python3.5  opencv
This is a dict project for AID 1803
'''

from socket import * 
import os 
import signal 
import time 
import pymysql 
import sys
from threading import Thread
import file_module as ftp
import struct

HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT) 

USERNAME = 'mizhizixin'
PASSWORD = '1234567890'
log_times = 0

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    while True:
        c,addr = s.accept() 
        print("Connect from",addr)
        r = log_in(c)
        if r:
            lourch(c)

def log_in(c):
    d=False
    log_times=0
    while True:
        a,b =False,False
        if log_times==3:
            c.close()
            break
        data = c.recv(128).decode()
        if data == USERNAME:
            a=True
        data = c.recv(128).decode()
        if data == PASSWORD:

            b=True

        if a and b:
            c.send(b'OK')
            d=True
            break
        else:
            c.send(b'FALL')
            log_times+=1
            continue
    if d:
        return True
    else:
        return False

def lourch(c):
    while True:
        print('列表')
        data = c.recv(128).decode()
        if data=='1':
            file_system(c)
        elif data=='2':
            moni_system(c)
        elif data=='3':
            quit()

def file_system(c):
    FILE_PATH = "/home/tarena/"
    while True:
        print('发送列表')
        ftp.do_list(c,FILE_PATH)
        data = c.recv(128).decode()
        filename = data.split(' ')[-1]

        if data[0] == 'G':
            ftp.do_get(c)
        elif data[0] == "P":
            ftp.do_put(c,filename,FILE_PATH)
            time.sleep(0.1)
            c.send("b ".encode())
        elif data[0] == "C":
            FILE_PATH = ftp.do_dir(c,filename,FILE_PATH)
        elif data[0] == "Q":
            break
        else:
            continue

def moni_system(c):
    cap = cv2.VideoCapture(0)
    for i in range(20):
            cap.read()
    send_thread = threading.Thread(target = moni_send)
    send_thread.start()
    c.recv(24)
    send_flag = False
    send_thread.join()

def moni_send(c):
    global send_flag
    send_flag = True
    while send_flag:
        _,frame = cap.read()
        _, imgencode = cv2.imencode('.jpg',frame)        
        img_code = numpy.array(imgencode)        
        img  = img_code.tostring()
        c.send(struct.pack("i",len(img))+img)
        sleep(0.13)



if __name__ == '__main__':
    main()