#process_event.py

from multiprocessing import Event,Process
from time import sleep


def wait_event():
    print('准备操作临界资源')
    e.wait()
    f = open('56.jpeg','rb')
    fw = open('59.jpeg','wb')
    while 1:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

def wait_event_timeout():
    print('也想操作临界资源')
    e.wait(4)
    if e.is_set():
        f = open('56.jpeg','rb')
        fw = open('60.jpeg','wb')
        while 1:
            data = f.read(1024)
            if not data:
                break
            fw.write(data)
        f.close()
        fw.close()
        
    else:
        print('等不了了，不等了')
e = Event()
p1 = Process(target = wait_event)
p2 = Process(target = wait_event_timeout)
p1.start()
p2.start()

print('假装主进程在操作临界资源')

sleep(3)
f = open('/home/tarena/56.jpeg','rb')
fw = open('56.jpeg','wb')
while 1:
    data = f.read(1024)
    if not data:
        break
    fw.write(data)
f.close()
fw.close()
e.set()
print('主进程操作完毕')



p1.join()
p2.join()
















