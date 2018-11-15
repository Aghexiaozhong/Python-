#my_thread.py
from threading import Thread
from time import sleep,ctime


class MyThread(Thread):
    def __init__(self,target,name = 'Tedu',args =(),kwargs = {}
        ):
        super().__init__()
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.target = target

    def run(self):
        self.target(*self.args,**self.kwargs)

def player(song,sec):
    for i in range(2):
        print('Playing %s:%s' % (song,ctime()))
        sleep(sec)


t = MyThread(target = player, args = ('卡路里',3))

t.start()
t.join()







