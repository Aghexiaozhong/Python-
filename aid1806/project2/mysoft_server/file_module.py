import os
import time

def do_list(c,FILE_PATH):
    filelist = os.listdir(FILE_PATH)
    #服务器确认请求是否可以执行
    if filelist == None:
        c.send(b"FALL") 
    c.send(b'OK')
    time.sleep(0.1)
    for filename in filelist:
        if filename[0] != '.': #and os.path.isfile(FILE_PATH + filename):
            c.send(filename.encode())
            time.sleep(0.1)
    c.send(b"##")
    print('文件列表发送完毕')
    return

def do_get(c):
    while True:
        filename=c.recv(128).decode()
        num = filename.split(' ')

        if num[0] == 'f':
            f = open(num[1],'wb')

            while True:
                data = c.recv(1024)
                if data == b'##':
                    f.close()  
                    break
                f.write(data)
            c.send(b"OK")
            print("文件：%s 接收完毕" % filename)
        elif num[0] == 'd':
            os.mkdir(num[1])
            c.send(b"OK")
        elif num[0] == 'b':
            break

def do_put(c,filename,FILE_PATH):
    if os.path.isfile(FILE_PATH+filename):
        c.send(("f "+filename).encode())
        time.sleep(0.2)
        f = open(FILE_PATH+filename,'rb')

        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                c.send(b'##')
                break
            c.send(data)
        print('文件传输结束')
        f.close()
        if (c.recv(128).decode())=='OK':
            print(filename,'传输成功')
        else:
            print(filename,'传输失败')
    else:
        c.send(("d "+filename).encode())
        if (c.recv(128).decode())=='OK':
            print(filename,'传输成功')
        else:
            print(filename,'传输失败')
        filelist = os.listdir(FILE_PATH+filename)
        print(filelist)
        for i in filelist:
            print(i)
            do_put(c,filename+'/'+i,FILE_PATH)

def do_dir(c,dirname,FILE_PATH):
    if os.path.isfile(FILE_PATH+dirname):
        c.send(b'FALL')
    else:
        c.send(b'OK')
        return FILE_PATH+dirname+'/'