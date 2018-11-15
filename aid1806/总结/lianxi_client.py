from socket import *

s = socket()
s.connect(('127.0.0.1',8888))

while True:
    msg  = input('msg>>>')
    s.send(msg.encode())
    if not msg:
        break
    # data = s.recv(1024).decode()
    # print(data)

s.close()















