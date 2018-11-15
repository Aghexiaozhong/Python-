#pool_map.py

from multiprocessing import Pool
import time

def fun(n):
    time.sleep(1)
    print('执行 pool_map事件',n)
    return n**2
pool = Pool(4)

#在进程池放入六个事件
r = pool.map(fun,range(6))
print('返回值列表:',r)
pool.close()
pool.join()









