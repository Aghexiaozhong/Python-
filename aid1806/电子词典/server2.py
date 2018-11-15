#!/usr/bin/env python3
#coding = utf-8

'''
name:钟建
data:2018-8-27
emial:5973965176@qq.com
modules:python3.5 mysql
This is a dict project for AID
'''

from socket import *

import os,sys
from select import *
import signal

import time
import pymysql

DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def do_child(c,db):
    #循环接收请求
    while True:
        data = c.recv(1024).decode()
        dataList = data.split(' ')
        if (not data) or dataList[0] == 'E':
            c.close()
            print('客户端退出')
            sys.exit(0)

        elif dataList[0] == 'R':
            do_register(c,dataList[1],dataList[2],db)

        elif dataList[0] == 'L':
            do_login(c,db,dataList[1],dataList[2])

        elif dataList[0] == 'C':
            do_chaci(c,db,dataList[1],dataList[2])

        elif dataList[0] == 'H':
            do_history(c,db,dataList[1])

def do_register(c,name1,passwd1,db):
    cursor = db.cursor()
    sql = "select * from user where name='%s'" \
    % name1
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return
    sql = "insert into user(name,passwd) \
    values ('%s','%s')" % (name1,passwd1)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')

    except:
        db.rollback()
        c.send(b'Failed')
        return

    else:
        print('{}注册成功'.format(name1))

def do_login(c,db,name1,passwd1):
    cursor = db.cursor()
    sql = "select * from user where \
    name ='%s' and passwd = '%s'" % (name1,passwd1)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'OK')

    else:
        c.send('用户名或密码不正确'.encode())

def do_chaci(c,db,name1,word1):
    cursor = db.cursor()

    def insert_history():
        tm = time.ctime()
        sql = "insert into hist (name,word,time) \
        values ('%s','%s','%s')" % (name1,word1,tm)
        try:
            cursor.execute(sql)
            db.commit()

        except:
            db.rollback()
            return

    try:

        f = open(DICT_TEXT,'rb')

    except:
        c.send('500 服务器异常'.encode())
        return
    while True:
        line = f.readline().decode()
        w = line.split(' ')[0]
        if (w > word1) or (not line):
            c.send('没找到该单词'.encode())
            break
        elif w == word1:
            c.send(b'OK')
            time.sleep(0.1)
            c.send(line.encode())
            insert_history()
            break
    f.close()


def do_history(c,db,name1):
    cursor = db.cursor()

    try:
        sql = "select * from hist where \
        name = '%s'" %name1
        cursor.execute(sql)
        r = cursor.fetchall()
        if not r:
            c.send('没有历史记录'.encode())
            return
        else:
            c.send(b'OK')

    except:
        c.send('数据库查询错误'.encode())
        return
    n = 0
    for i in r:
        n += 1
        if n > 10:
            break
        time.sleep(0.1)
        msg = '%s %s %s' % (i[1],i[2],i[3])
        c.send(msg.encode())

    time.sleep(0.1)
    c.send(b'##')


#主控制流程
def main():
    #连接数据库
    db = pymysql.connect('localhost','root','123456', \
        'cidian')
    s =socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #忽略子进程退出
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            print('Waiting for connect...')
            c,addr = s.accept()
            print('conect from',addr)

        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')

        except Exception as e:
            print(e)
            continue

        #创建子进程，处理客户端请求
        pid = os.fork()

        if pid == 0:
            s.close()
            do_child(c,db)

        else:
            c.close()
            continue

if __name__ == '__main__':
    main()








