from test import * 
import multiprocessing 
import time 

counts = []

def io():
    write()
    read()

t = time.time()

for x in range(10):
    th = multiprocessing.Process(target = io)
    th.start()
    counts.append(th)

for i in counts:
    i.join()
print("Process IO",time.time() - t)