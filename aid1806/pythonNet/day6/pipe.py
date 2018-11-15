#pipe.py

from multiprocessing import Process,Pipe
import os,time

#创建管道
fd1,fd2 = Pipe()

def fun(name):
    time.sleep(3)
    #向管道写入内容
    fd1.send('hello '+str(name))

jobs = []
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

while True:
    #从管道读取内容
    data = fd2.recv()
    
    print(data)

for i in jobs:
    i.join()











