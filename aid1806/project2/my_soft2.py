#!/usr/bin/python3
from socket import * 
from time import sleep
import sys,os
import signal 

def send_file(s,filebase,filename):
    if os.path.isfile(filebase+filename):
        s.send(("f "+filename).encode())
        sleep(0.1)
        f = open(filebase+filename,'rb')

        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                s.send(b'##')
                break
            s.send(data)
        print('文件传输结束')
        f.close()
    else:
        s.send(("d "+filename).encode())
        sleep(0.1)
        filelist = os.listdir(filebase+filename)
        for i in filelist:
            send_file(s,filebase,filename+'/'+i)



def sendfile(d,addrnum,file):
    ADDR = (d[addrnum],8888)
    s = socket()

    s.connect(ADDR)
    file=file.split('/')
    filebase='/'.join(file[:-1])
    filename='/'+file[-1]
    send_file(s,filebase,filename)
    sleep(0.1)
    s.send("b ".encode())
    s.close()

def recv_file(c,flname):
    while True:
        filename=c.recv(48).decode()
        num = filename.split(' ')

        if num[0] == 'f':
            f = open(flname+num[1],'wb')

            while True:
                data = c.recv(1024)
                if data == b'##':
                    f.close()  
                    break
                f.write(data)
            print("文件：%s 接收完毕" % filename)
        elif num[0] == 'd':
            os.mkdir(flname+num[1])
        elif num[0] == 'b':
            break
    c.close() 


def recvfile(d):
    d1=['%d' % x for x in range(1,len(d)+1)]
    d2=[d[x] for x in d1]
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('',8888))
    s.listen(5)
    while True:
        c, addr = s.accept()
        if addr[0] not in d2:
            c.close()
        else:
            break

    print("Connect from ",addr)


    mrname = './' 
 
    recv_file(c,mrname)

    s.close() 
    
def main():
    d={"1":'176.209.103.80',"2":'176.209.103.75',"3":'176.209.103.83',"4":'176.209.103.63',\
        "5":'176.209.103.82',"6":'176.209.103.72',"7":'176.209.103.69',"8":'176.209.103.60'}

    if len(sys.argv) == 3:
        sendfile(d,sys.argv[1],sys.argv[2])
    else:
        recvfile(d)
if __name__ == '__main__':
    main()
