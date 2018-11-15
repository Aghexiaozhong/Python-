#!/usr/bin/env python3
from socket import * 
import sys 
import getpass
import file_module2 as ftp
import os
import time
from moni_module2 import *
import threading

def main():

    HOST = "176.209.103.83"
    PORT = 8000
    s = socket()
    s.connect((HOST,PORT))
    print('''
            =======================================
            --Intelligentize House Manager System--
            =======================================
            ''')
    while True:
        try:
            uname = input("请输入用户名>>")
        except Exception:
            print('命令错误')
            continue
        s.send(uname.encode())
        try:
            password = input("请输入密码>>")
        except Exception:
            print('命令错误')
            continue
        s.send(password.encode())
        data = s.recv(128).decode()
        if data == 'OK':
            print("登录成功！！！")
            do_work(s)
        else:
            print("用户名或密码不正确")
            continue
        break


def do_work(s):
    while True:
        print("********命令选项**********")
        print("********1.桌面文件传输************")
        print("********2.远程室内监控********")
        print("********3.WARRING********")
        try:
            cmd = input("输入选项>>")
        except Exception:
            print('命令错误')
        s.send(cmd.encode())
        if cmd not in ['1','2','3']:
            print('请出入正确选项')
            sys.stdin.flush() #清除标准输入的缓存

        elif cmd == '1':
            transfer_file(s)
        elif cmd == '2':
            moni_camera(s)
        elif cmd == '3':
            break

def transfer_file(s):
    print("********命令选项**********")
    print("******** list************")
    print("******** get file********")
    print("******** put file********")
    print("******** quit************")
    while True:
        print('-------------------------------------------')
        ftp.do_list(s)
        print('-------------------文件列表-----------------')
        data = input("输入命令>>")
        filename = data.split(' ')[-1]
        
        if data[:3] == 'get':
            ftp.do_get(s,filename)
        elif data[:3] == 'put':
            s.send(('G '+filename).encode())
            ftp.do_put(s,filename)
            time.sleep(0.1)
            s.send("b ".encode()) 
        elif data[:2] == 'cd':
            ftp.do_dir(s,filename) 
        elif data[:4] == 'quit':
            s.send("Q ".encode())
            break
        else:
            s.send("T ".encode())
            print("请输出正确命令！！！")
            continue 

def moni_camera(s):
    moni_cap = Moni_obj(s)
    moni_thread = threading.Thread(target = moni_cap.moni_rece)
    moni_thread.start()
    while True:
        print("******** 监控程序已启动，请输入命令查看 ******")
        print("******** 1.查看监控画面 *******************")
        print("******** 2.查看异常监控录像 ****************")
        print("******** 3.退出监控 ***********************")
        t = input('请输入命令：')
        if t== '1':
            moni_cap.start_flag = True
            while True:
                a = input('输入q退出：')
                if a=='q':
                    moni_cap.start_flag = False
                    break
                else:
                    print('请输入正确的命令！！！')
                    continue
                        

        elif t=='2':
            view_moni()
        elif t=='3': 
            moni_cap.thread_flag = False
            moni_thread.join()
            break
   
if __name__ == '__main__':
    main()