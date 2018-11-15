#queue0.py

from multiprocessing import Queue
from time import sleep

#创建队列
q = Queue(3)

q.put(1)
sleep(0.5)
print(q.empty())

q.put('tankyou process')
q.put([3,4,5,5,67])

print(q.full())
#如果设置为非阻塞则产生full异常
print(q.get())
q.put(666,False)
print(q.full())
print(q.qsize())
q.close()






