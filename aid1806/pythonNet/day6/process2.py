#process2.py

from multiprocessing import Process
from time import sleep



def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print('I"m working...')
p =Process(target = worker, name = 'WORKER',\
    args = (2,),kwargs = {'name':'Alex'})
p.start()

print(p.name)
print('Child PID :',p.pid)
print('is_aliove?',p.is_alive())
p.join()

print('is_aliove?',p.is_alive())













