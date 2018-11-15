#majiang_server.py

import random 
from socket import *
from time import sleep
import os,sys
from multiprocessing import Pool
import signal
import majiang_database

class TftpServer(object):
    def __init__(self,c):
        self.c = c 
        self.sqlh = majiang_database.Mydatabase('majiangku')
    
    def do_zhuce(self,name1,passwd1,nicheng,telnum1):
        sql = 'select username from user'
        res = self.sqlh.chaxun(sql)
        
        
        if (name1,) not in res:
            self.c.send(b'OK')
            sql2 = 'insert into user(username,password,user_nicheng,telnum)\
             values (%s,%s,%s,%s)'
            self.sqlh.zhixin(sql2,[name1,passwd1,nicheng,telnum1])
            
        else:
            self.c.send('用户已存在'.encode())


    def do_login(self,name1,passwd1):

        sql = 'select username from user'
        res = self.sqlh.chaxun(sql)
        if (name1,) in res:
            sql2 = 'select password from user \
            where username = %s'
            res2 = self.sqlh.chaxun(sql2,[name1])
            if (passwd1,) in res2:
                self.c.send(b'OK')
                
            else:
                self.c.send('密码错误'.encode())
        else:
            self.c.send('用户不存在'.encode())

    def manle(self):
        self.c.send('不好意思,人已经满了'.encode())


    def userid(self,name1):
        sql = "select userid from user \
        where username= %s"
        res = self.sqlh.chaxun(sql,[name1])
        for (i,) in res:
            return i



class FangJian(object):

    def __init__(self,s,c,l,count):
        self.s = s
        self.c = c
        self.pai = l
        self.count = count

    def chuli(self):
        
        if self.count == 1:
            self.weizhi1()

        elif self.count == 2:
            self.weizhi2() 

        elif self.count == 3:
            self.weizhi3()

        elif self.count == 4:
            self.weizhi4()
        
    def weizhi1(self):
        self.c.send(b'OK')
        sleep(0.1)
        for i in self.pai[:14]:
            self.c.send((i+' ').encode())
        pai_list1 = self.pai[:14]
        self.c.send('1'.encode()) 
        
        while 1:
            
            data = self.c.recv(1024).decode()
            print(data)
            pai_list1.remove(data)

            return pai_list1
                

    def weizhi2(self):
        self.c.send(b'OK')
        sleep(0.1)
        for i in self.pai[14:27]:
            self.c.send((i+' ').encode())
        pai2 = self.pai[14:27]
        self.c.send('2'.encode())
            # while 1:
            # data = self.s.recv(1024)
            # sleep(0.1)
            # self.c.send(data)

    def weizhi3(self):
        self.c.send(b'OK')
        sleep(0.1)
        for i in self.pai[27:40]:
            self.c.send((i+' ').encode())
        pai3 = self.pai[27:40]
        self.c.send('3'.encode())

    def weizhi4(self):
        self.c.send(b'OK')
        sleep(0.1)
        for i in self.pai[40:53]:
            self.c.send((i+' ').encode())
        pai4 = self.pai[40:53]
        self.c.send('4'.encode())



    def dapai(self):
        self.c.send(b'OK')

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('0.0.0.0',8888))
    s.listen(5)

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    count = 0
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

        count += 1

        userid_list = []
        if pid == 0:
            # s.close()  对于子进程，s是没用的，他只负责和客户端交互
            tftp = TftpServer(c)
            
            while 1:
                data = c.recv(1024).decode()
                dataList = data.split(' ')
                    
                if (not data) or dataList[0] == 'Q':
                    print('客户端退出')
                    
                    sys.exit(0)

                elif dataList[0] == 'Z':
                    tftp.do_zhuce(dataList[1],dataList[2],dataList[3],dataList[4])

                elif dataList[0] == 'L':
                    tftp.do_login(dataList[1],dataList[2])

                elif dataList[0] == 'K':

                    
                
                    l=[]
                    for i in range(1,10):
                        for j in ['D','W','T']:
                            l.append(str(i)+j)
                    l = l*4

                    random.shuffle(l)
                    userid = tftp.userid(dataList[1])
                    
                    dapai = FangJian(s,c,l,count)
                    while 1:
                        pai_list1 = dapai.weizhi1()
                        print(pai_list1)
                    pai_list2 = dapai.chuli()
                    pai_list3 = dapai.chuli()
                    pai_list4 = dapai.chuli()
                    if count > 4:
                        tftp.manle()

                
        else:
            c.close()
            continue

if __name__ == '__main__':
                    
                    
    main()










