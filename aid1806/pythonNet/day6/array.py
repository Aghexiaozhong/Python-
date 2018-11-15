#array.py

from multiprocessing import Process,Array
import time

#创建共享内存
shm = Array('c',b'hello world')
# shm = Array('i',5)

def fun():
    for i in shm:
        print(i)
    shm[0] = b'H' 

p = Process(target = fun)
p.start()
p.join()

print(shm.value.decode())
# for i in shm:
#     print(i)



















