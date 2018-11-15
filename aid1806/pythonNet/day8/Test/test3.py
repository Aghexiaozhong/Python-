from test import * 
import threading 
import time 

counts = []

def io():
    write()
    read()

t = time.time()

for x in range(10):
    th = threading.Thread(target = io)
    th.start()
    counts.append(th)

for i in counts:
    i.join()
print("Thread IO",time.time() - t)