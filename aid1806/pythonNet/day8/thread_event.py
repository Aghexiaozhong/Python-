import threading 
from time import sleep 

#共享资源
s = None

#创建事件对象
e = threading.Event()

def bar():
    print("呼叫foo")
    global s 
    s = "天王盖地虎"

def foo():
    print("等口令")
    sleep(2)
    if s == "天王盖地虎":
        print("宝塔镇河妖")
    else:
        print("打死他")
    e.set()

def fun():
    print("呵呵....")
    sleep(1)
    e.wait()
    global s 
    s = "小鸡炖蘑菇"

b = threading.Thread(target = bar)
f = threading.Thread(target = foo)
t = threading.Thread(target = fun)

b.start()
f.start()
t.start()

b.join()
f.join()
t.join()