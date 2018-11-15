#pool.py

from multiprocessing import *
from time import sleep,ctime


def worker(msg):
    sleep(2)
    print(msg)
    return ctime()


#创建进程池对象
pool = Pool(processes = 4)

result = []
for i in range(10):
    msg = 'hello %d' % i
    #将事件放入进程池
    #异步执行
    r = pool.apply_async(func = worker,args = (msg,))
    result.append(r)

    # #同步执行(一步一步执行，不常用)
    # pool.apply(func = worker,args = (msg,))
#关闭进程池
pool.close()

#回收进程池
pool.join()

for i in result:
    print(i.get())





