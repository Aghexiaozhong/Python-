#!/usr/bin/env python3
#coding = utf-8

from socket import *
import sys
import getpass

def do_register(s):
    while True:
        name = input('用户名:')
        passwd = getpass.getpass('密码:')
        passwd1 = getpass.getpass('确认密码:')
        if (' ' in name) or (' ' in passwd):
            print('用户名密码不允许空格')
            continue
        if passwd != passwd1:
            print('两次密码不一致')
            continue
        msg = 'R {} {}'.format(name,passwd)
        #发送请求
        s.send(msg.encode())
        #接收回复
        data = s.recv(1024).decode()
        if data == 'OK':
            
            return name

        elif data == 'EXISTS':
            print('该用户已存在')
            return 1

        else:
            return 1

def do_login(s):
    
    name = input('输入用户名:')
    passwd = getpass.getpass('密码:')
    
    if (' ' in name) or (' ' in passwd):
        print('用户已存在')

    msg = 'L '+name+' '+passwd
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == 'OK':
        print('登录成功!')
        return name

    else:
        print(data)
        return 1

def login(s,name):
    while True:
        print('============================')
        print('| 1) 查词                  |')
        print('| 2) 查看历史记录          |')
        print('| 3) 退出                  |')
        print('============================')
        
        try:
            cmd2 = int(input('请输入命令:'))
        except KeyboardInterrupt:
            print('')

        except Exception:
            print('命令错误')
            continue

        if cmd2 not in [1,2,3]:
            print('没有该选项')
            sys.stdin.flush()
            continue
        elif cmd2 == 1:
            do_chaci(s,name)

        elif cmd2 == 2:
            do_history(s,name)

        elif cmd2 == 3:
            
            break

def do_chaci(s,name):
    while True:
        word = input('输入单词:')
        if word == '##':
            break
        msg = 'C '+name+' '+word
        s.send(msg.encode())

        data = s.recv(128).decode()
        if data == 'OK':
            data = s.recv(2048).decode()
            print(data)
        else:
            print(data)


def do_history(s,name):
    msg = 'H '+name
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            
            print(data)

    else:
        print(data)

def main():
    if len(sys.argv) < 3:
        print('argv error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket()
    s.connect(ADDR)

    while True:
        print('============================')
        print('| 2) 注册                  |')
        print('| 1) 登录                  |')
        print('| 3) 退出                  |')
        print('============================')
        try:
            cmd = int(input('输入选项>>'))

        except Exception:
            print('输入命令有误!')
            continue

        if cmd not in [1,2,3]:
            print('对不起，没有该选项!')
            sys.stdin.flush()  #清除输入
            continue

        elif cmd == 1:
            name = do_register(s)
            if name != 1:
                print('注册成功,直接登录')
                login(s,name)
            
            elif do_register(s) == 1:
                print('注册失败!')

        elif cmd == 2:
            name = do_login(s)
            if name != 1:
                login(s,name)
                


        elif cmd == 3:
            
            sys.exit('谢谢使用')
if __name__ == '__main__':
    main()






