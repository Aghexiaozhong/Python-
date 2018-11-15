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
from multiprocessing import Process
import os,sys
from select import *
import signal
from database import Mydatabase
from time import sleep


class TftpServer(object):
    def __init__(self,c):
        self.c = c
        self.sqlh = Mydatabase('cidian')

    def do_login(self,name1,passwd1):
        while True:
            sql = 'select name from user'
            res = self.sqlh.chaxun(sql)
            if (name1,) in res:
                sql2 = 'select passwd from user \
                where name = %s'
                res2 = self.sqlh.chaxun(sql2,[name1])
                if (passwd1,) in res2:
                    self.c.send(b'OK')
                    break
                else:
                    self.c.send('密码错误'.encode())
            else:
                self.c.send('用户不存在'.encode())

        
    def do_zuce(self,name1,passwd1):
        sql = 'select name from user'
        res = self.sqlh.chaxun(sql)
        
        
        if (name1,) not in res:
            self.c.send(b'OK')
            sql2 = 'insert into user(name,passwd)\
             values (%s,%s)'
            self.sqlh.zhixin(sql2,[name1,passwd1])
            
        else:
            self.c.send('用户已存在'.encode())
            


    def do_history(self,name1):
        sql = 'select name from hist'
        res = self.sqlh.chaxun(sql)
        if (name1,) in res:
            sql2 = 'select word \
            from hist where name=%s'
            res2 = self.sqlh.chaxun(sql2,[name1])
            for i in res2:
                for j in i:
                    self.c.send(name1.encode())
                    self.c.send(' '.encode())
                
                    self.c.send(j.encode())
                    self.c.send(' '.encode())
                    self.c.send('\n'.encode())   
        else:
            self.c.send('没有历史记录'.encode())   

    def do_chaci(self,name1,danci):
        sql = 'select word from words'
        res = self.sqlh.chaxun(sql)
        
        if danci == '':
            print('结束查词')
            
            
        elif (danci,) in res:
            sql2 = 'select interpret from \
            words where word=%s'
            res2 = self.sqlh.chaxun(sql2,[danci])
            ((i,),) = res2

            self.c.send(i.encode())
            sql3 = 'insert into hist(name,word) \
            values (%s,%s)'
            self.sqlh.zhixin(sql3,[name1,danci])
            

        else:
            self.c.send('您搜索的单词不存在'.encode())


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('0.0.0.0',8888))
    s.listen(5)

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while 1:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
        print('客户端登录',addr)

        #创建子进程处理客户端请求
        pid = os.fork()

        
        if pid == 0:
            s.close()  #对于子进程，s是没用的，他只负责和客户端交互
            tftp = TftpServer(c)
            while 1:
                data = c.recv(1024).decode()
                dataList = data.split(' ')
                    
                if (not data) or dataList[0] == 'Q':
                    print('客户端退出')
                    sys.exit(0)

                elif dataList[0] == 'Z':
                    tftp.do_zuce(dataList[1],dataList[2])

                elif dataList[0] == 'L':
                    tftp.do_login(dataList[1],dataList[2])

                elif dataList[0] == 'C':
                    tftp.do_chaci(dataList[1],dataList[2])

                elif dataList[0] == 'H':
                    tftp.do_history(dataList[1])

        else:
            c.close()
            continue
    
if __name__ == '__main__':
    main()   






        


            


    


    






















