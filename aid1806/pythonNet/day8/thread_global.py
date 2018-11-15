from threading import Thread 
from time import sleep 


a = 1

def foo():
    global a
    a = 1000

def bar():
    sleep(1)
    print("a = ",a)

t1 = Thread(target = foo)
t2 = Thread(target = bar)

t1.start()
t2.start()

t1.join()
t2.join()