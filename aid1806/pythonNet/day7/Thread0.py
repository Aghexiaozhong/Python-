#Thread0.py

import threading
from time import sleep
import os

a = 1
#写一个线程函数
def music():
    global a
    a = 10000
    for i in range(5):
        sleep(2)
        print('播放龙拳',os.getpid())

t = threading.Thread(target = music)
t.start()

for i in range(5):
    sleep(1.5)
    print('播放稻香',os.getpid())


t.join()
print('a=:',a)
















