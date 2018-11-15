import time
from threading import Thread

class T(object):
    def __init__(self):
        self.a = True
        self.b = 0
    def p(self):
        while self.a:
            self.b+=1
            time.sleep(0.2)
t = T()

l = Thread(target = t.p)
l.start()
b = input('请结束线程')
if b == '1':
    t.a=False
    print('dayin',t.b)
l.join()
print("=====主线程结束======")