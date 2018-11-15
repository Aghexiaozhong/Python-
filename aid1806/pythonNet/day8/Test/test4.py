from test import * 
import multiprocessing 
import time 

counts = []

t = time.time()

for x in range(10):
    th = multiprocessing.Process\
    (target = count,args = (1,1))
    th.start()
    counts.append(th)

for i in counts:
    i.join()
print("Process cpu",time.time() - t)