#copy_file.py


import os
from multiprocessing import Process

size = os.path.getsize('./56.jpeg')

#复制前半部分
def copy1(img):
    f = open(img,'rb')
    n = size // 2
    fw = open('7.jpeg','wb')
    while 1:
        # if n < 1024:
        #     data = f.read(n)
        #     fw.write(data)
        #     break
        # data = f.read(1024)
        # fw.write(data)
        # n -= 1024
        data =f.read(1024)
        if n < f.tell()+1024:
            f.read(n-f.tell())
            break
        fw.write(data)
    f.close()
    fw.close()
    print('复制成功')


#复制后半部分
def copy2(img):
    f = open(img,'rb')
    fw = open('7.jpeg','wb')
    f.seek(size // 2 ,0)
    while 1:
        data = f.read(1024)
        if not data:
            break 
        fw.write(data)
    f.close()
    fw.close()
    print('复制成功')

p1 = Process(target = copy1,args = ('56.jpeg',))
p2 = Process(target = copy2,args = ('56.jpeg',))

p1.start()
p2.start()

p1.join()
p2.join()











