#lainxi.py

# 创建父子进程分别表示司机和售票员
# 当售票员捕捉到SIGINT信号时，给司机发送SIGUSER1信号
#  此时司机打印'老司机开车了'

# 当售票员捕捉到SIGQUIT信号时，给司机发送SIGUSER2信号
#   此时司机打印'车速有点快，系好安全带'

# 当司机捕捉到SIGTSTP信号时，给售票员发送SIGUSER1信号
#  此时售票员打印'到站了请下车'

# 到站后，售票员先下车（子进程先退出），然后司机下车


from signal import *
import os
from multiprocessing import Process
import sys
from time import sleep

def shoupiaoyuan(sig,frame):

    # k = os.getpid()
    # return k
    
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
        
    if sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)

    if sig == SIGUSR1:
        print('到站了请下车')
        sys.exit()





# signal(SIGINT,shoupiaoyuan)
# signal(SIGQUIT,shoupiaoyuan)


def siji(sig,frame):
    
    
    if sig == SIGUSR1:
        print('老司机开车了')

    if sig == SIGUSR2:
        print('车速有点快，系好安全带')

    if sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)
        sleep(1)
        sys.exit()

def driver():
    signal(SIGINT,shoupiaoyuan)
    signal(SIGQUIT,shoupiaoyuan)
    signal(SIGUSR1,shoupiaoyuan)
    signal(SIGTSTP,SIG_IGN)
    while 1:
        sleep(2)
        print('可以的')
    
p = Process(target = driver)
p.start()



signal(SIGUSR1,siji)
signal(SIGUSR2,siji)
signal(SIGTSTP,siji)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)


p.join()







