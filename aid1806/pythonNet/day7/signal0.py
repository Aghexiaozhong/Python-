#signal0.py

import signal
from time import sleep


signal.alarm(5)

#使用忽略的方法处理信号
signal.signal(signal.SIGALRM,signal.SIG_IGN)

signal.signal(signal.SIGINT,signal.SIG_IGN)
while True:
    sleep(2)
    print('摁ctrl-c:')
    print('等待时钟....')
















