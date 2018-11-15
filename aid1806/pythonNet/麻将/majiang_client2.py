#!/user/bin/python3
#coding=utf-8
'''
name:钟建
项目名称：麻将
'''
import getpass
from socket import *
import sys,os
from time import sleep

class ClientServer(object):
    def __init__(self,s):
        self.s = s

    def do_zhuce(self):
        while True:

            name = input('用户名:')
            passwd = getpass.getpass('六位数字密码:')
            passwd1 = getpass.getpass('确认密码:')

            if (' ' in name) or (' ' in passwd):
                print('用户名密码不允许空格')
                continue
            if passwd != passwd1:
                print('两次密码不一致')
                continue

            nicheng = input('昵称:')
            tel_num = input('输入十一位电话号码:')

            if type(int(passwd)) != int or (len(passwd) != 6):
                print('请输入六位数字密码')
                continue
            if type(int(tel_num)) != int or (len(tel_num) != 11):
                print('请输入十一位电话号码')
                continue

            msg = 'Z {} {} {} {}'.format(name,passwd,nicheng,tel_num)
            #发送请求
            self.s.send(msg.encode())
            #接收回复
            data = self.s.recv(1024).decode()
            if data == 'OK':
                
                return name

            elif data == 'EXISTS':
                print('该用户已存在')
                return 1

            else:
                return 1

    def do_login(self):
        name = input('输入用户名:')
        passwd = getpass.getpass('密码:')
        
        if (' ' in name) or (' ' in passwd):
            print('用户已存在')

        msg = 'L '+name+' '+passwd
        self.s.send(msg.encode())
        data = self.s.recv(1024).decode()
        if data == 'OK':
            print('登录成功!')
            return name

        else:
            print(data)
            return 1

    def login(self,name):
        while True:
            print('==================')
            print('|   快速开始       |')
            print('|   退出           |')
            print('==================')
            try:
                cmd = int(input('输入命令>>>'))
            except Exception:
                print('输入命令错误!')
                sys.stdin.flush()
                continue
            if cmd not in [1,2]:
                print('没有该选项')
                sys.stdin.flush()
                continue

            elif cmd == 1:
                msg = 'K '+name
                self.s.send(msg.encode())
                data = self.s.recv(1024).decode()
                if data == '不好意思,人已经满了':
                    return
                elif data == 'OK':
                    print('进入房间，开始游戏')
                    
                    self.do_dapai(name)
                    
            
            elif cmd == 2:
                
                return

    def do_dapai(self,name):
        
        pai = []
        pai1 = []
        pai2 = []
        pai3 = []
        dataList = []
        data = self.s.recv(1024).decode()
        sleep(1)
        print(data)
        datalist = data.split(' ')
        for i in datalist:
            if i != '' and i != '1' and i != '2' and i != '3' and i != '4':
                dataList.append(i)
        
        for i in dataList:
            if i[1] == 'W':
                pai1.append(i)
        pai1.sort()
        
        for i in dataList:
            if i[1] == 'D':

                pai2.append(i)
        pai2.sort()
        for i in dataList:
            if i[1] == 'T':
                pai3.append(i)
        pai3.sort()
        pai = pai1+pai2+pai3
        print(pai)

        if len(dataList) == 14:
            
            dapai = input('请出牌:')
            while True:
                
                msg = '位置１出牌'+' '+dapai
                self.s.send(msg.encode())
                print('等待其他人打牌...')
                data = self.s.recv(1024).decode()
                if data == '胡了':
                    break
                print(data)
                for i in pai:
                    if pai.count(data) == 2:
                        xuanze = input('碰还是不碰:')
                        if xuanze == '碰':
                            pai.remove(data)
                            pai.remove(data)
                            
                            dapai = input('请出牌:')
                            
                            self.s.send(dapai.encode())
                            continue
                    if pai.count(data) == 3:
                        xuanze = input('杠还是不杠:')
                        if xuanze == '杠':
                            pai.remove(data)
                            pai.remove(data)
                            pai.remove(data)
        elif len(dataList) == 13:
            while True:
                print('等待其他人打牌...')
                data = self.s.recv(1024).decode()
                if data == '胡了':
                    break
                print(data)
                for i in pai:
                    if pai.count(data) == 2:
                        xuanze = input('碰还是不碰:')
                        if xuanze == '碰':
                            pai.remove(data)
                            pai.remove(data)
                            
                            dapai = input('请出牌:')
                            
                            self.s.send(dapai.encode())
                            continue
                    if pai.count(data) == 3:
                        xuanze = input('杠还是不杠:')
                        if xuanze == '杠':
                            pai.remove(data)
                            pai.remove(data)
                            pai.remove(data)

        


    def do_quit(self):
        msg = 'Q '
        self.s.send(msg.encode())


def main():
    if len(sys.argv) < 3:
        print('argv error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    s = socket()
    s.connect(ADDR)
    tftp = ClientServer(s)
    while True:
        print('')
        print('==========================')
        print('| 1) 注册                  |')
        print('| 2) 登录                  |')
        print('| 3) 退出                  |')
        print('==========================')
        try:

            cmd = int(input('输入选项>>>'))
        
        except Exception:
            print('输入命令有误!')
            continue


        if cmd not in [1,2,3]:
            print('没有该选项!')
            sys.stdin.flush()
            continue

        elif cmd == 1:
            
            name = tftp.do_zhuce()
            if name != 1:
                print('注册成功,直接登录')
                tftp.login(name)
            elif do_register(s) == 1:
                print('注册失败!')
        
        elif cmd == 2:

            
            name = tftp.do_login()
            if name != 1:
                tftp.login(name)

        elif cmd == 3:
            tftp.do_quit()
            sys.exit('欢迎使用')
        


if __name__ == '__main__':

    main()





























