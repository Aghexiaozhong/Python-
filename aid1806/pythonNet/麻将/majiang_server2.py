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
            sql2 = 'insert into user(username,password,nicheng,telnum)\
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

    def __init__(self,c,count,l):
        self.c = c
        self.num = count
        self.paimian = l
        self.sqlh = majiang_database.Mydatabase('majiangku')
        self.sypai = self.paimian[53:107]
        
    def chuli(self):
        self.c.send(b'OK')
        
        if self.num == 1:
            self.weizhi1()

        elif self.num == 2:
            self.weizhi2() 

        elif self.num == 3:
            self.weizhi3()

        elif self.num == 4:
            self.weizhi4()
        data = self.weizhi1()
        
        return data

    def weizhi1(self):
        sleep(0.1)
        pai1 = self.paimian[:14]
        for i in self.paimian[:14]:
            self.c.send((i+' ').encode())
        self.c.send('1'.encode())

       
        
        data = self.c.recv(1024).decode()
        
        return data
        # sql = "insert into game(paidui) values(%s);"
        # self.sqlh.zhixin(sql,[data])
        
        
        # msg1 = '2'+data
        # msg2 = '3'+data
        # msg3 = '4'+data
        # self.c.send(msg1.encode())
        # self.c.send(msg2.encode())
        # self.c.send(msg3.encode())


    def weizhi2(self):
        sleep(0.1)
        for i in self.paimian[14:27]:
            self.c.send((i+' ').encode())
        self.c.send('2'.encode())
        pai2 = self.paimian[14:27]
        
        while True:
            
            # sql = "select paidui from game where id=%s;"
            # res = self.sqlh.chaxun(sql,[i])
            # for (i,) in res:
            #     self.c.send(i.encode())
            data = self.c.recv(1024).decode()
            
            


    def weizhi3(self):
        sleep(0.1)
        for i in self.paimian[27:40]:
            self.c.send((i+' ').encode())
        self.c.send('3'.encode())
        pai3 = self.paimian[27:40]
        
        while True:
           
            # sql = "select paidui from game where id=%s;"
            # res = self.sqlh.chaxun(sql,[i])
            # for (i,) in res:
            #     self.c.send(i.encode())
            data = self.c.recv(1024).decode()


    def weizhi4(self):
        sleep(0.1)
        for i in self.paimian[40:53]:
            self.c.send((i+' ').encode())
        self.c.send('4'.encode())
        pai4 = self.paimian[40:53]
        
        while True:
           
            # sql = "select paidui from game where id=%s;"
            # res = self.sqlh.chaxun(sql,[i])
            # for (i,) in res:
            #     self.c.send(i.encode())
            data = self.c.recv(1024).decode()


    def dapai(self):
        self.c.send(b'OK')
    
    
    




def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('0.0.0.0',8888))
    s.listen(5)

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    userid_list = []
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
                    
                    
                    # userid = tftp.userid(dataList[1])
                    
                    
                    # data = c.recv(1024).decode()
                    # dataList = data.split(' ')
                    # print(data)
                    # dapai = FangJian(c,count,l)
                    # dapai.chuli(dataList[0],dataList[1])

                    # dapai.dapai(dataList[1])
                    dapai = FangJian(c,count,l)
                    # dapai.chuli()
                    data2 = dapai.chuli()
                    print(data2)
                    c.send(data2.encode())
                    
                    if count > 4:
                        tftp.manle()
                  

        else:
            c.close()
            continue

if __name__ == '__main__':
    main()










