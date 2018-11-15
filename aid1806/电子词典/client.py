#client.py

from multiprocessing import Process
from socket import *
import sys,os
from time import sleep

class TftpClient(object):
    def __init__(self,s):
        self.s = s

    def login(self):
        
        try:
            name = input('输入用户名:')
            passwd = input('输入密码:')
            msg = 'L '+name+' '+passwd
            self.s.send(msg.encode())
            
            data = self.s.recv(1024)
            if data.decode() == 'OK':
                print('登录成功')
                return name
            else:
                print(data.decode())
        except KeyboardInterrupt:
            sys.exit('退出客户端')

        except Exception as e:
            print(e)
                
                
        
            


    def zuce(self):
        while True:
            name = input('输入名字:')
            passwd = input('输入六位密码：')
            if len(passwd) == 6:
                msg = 'Z '+name+' '+passwd
                self.s.send(msg.encode())
                data = self.s.recv(1024).decode()
                if data == 'OK':
                    print('注册成功')
                    break
                else:
                    print(data)
            else:
                print('请输入六位密码!')

    def do_quit(self):
        msg = 'Q '
        self.s.send(msg.encode())


    def chaci(self,name):
        while True:
            danci = input('输入单词:')
            msg = 'C '+name+' '+danci
            if not danci:
                break
            self.s.send(msg.encode())
            data = self.s.recv(1024).decode()
            print(data)


    def history(self,name):
        msg = 'H '+name
        self.s.send(msg.encode())
        sleep(0.1)
        data = self.s.recv(1024).decode()
        print(data)

def main():
    if len(sys.argv)<3:
        print('argv error')
        return 
    PORT = 8888
    HOST = '0.0.0.0'
    ADDR = (HOST,PORT)
    s = socket()
    s.connect(ADDR)
    tftp = TftpClient(s)

    while True:
        print('============================')
        print('| 1) 登录                  |')
        print('| 2) 注册                  |')
        print('| 3) 退出                  |')
        print('============================')
        cmd = int(input('请输入命令:'))
        if cmd == 1:
            tftp.login()

        elif cmd == 2:
            tftp.zuce()
            continue

        elif cmd == 3:
            tftp.do_quit()
            print('欢迎使用')
            sys.exit(0)

        else:
            print('请输入正确指令！')


        name = tftp.login()
        if name:
            while True:
                print('============================')
                print('| 1) 查词                  |')
                print('| 2) 查看历史记录          |')
                print('| 3) 退出                  |')
                print('============================')
                cmd2 = int(input('请输入命令:'))
                if cmd2 == 1:
                    tftp.chaci(name)

                elif cmd2 == 2:
                    tftp.history(name)

                elif cmd2 == 3:
                    
                    break

                else:
                    print('请输入正确指令！')

        else:
            return



if __name__ == '__main__':
    main()

                
            

            














