#signal1.py

from signal import *
import time

def handler(sig,frame):
    if sig == SIGALRM:
        print('收到时钟信号')
    elif sig == SIGINT:
        print('就不结束，很皮')




alarm(5)
signal(SIGALRM,handler)
signal(SIGINT,handler)

while True:
    print('Waiting for a signal...')
    time.sleep(2)

















