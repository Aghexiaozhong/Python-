import os
import time
def do_list(s):
        #接收服务器确认　OK  or  FALL
        data = s.recv(128).decode()
        print(data)
        if data == 'OK':
            while True:
                data = s.recv(128).decode()
                if data == '##':
                    break
                print(data,end=' ')
            print("")
            return
        else:
            print("文件列表请求失败")
            return
def do_get(s,flname):
    s.send(('P '+flname).encode())
    while True:
        filename=s.recv(128).decode()
        num = filename.split(' ')

        if num[0] == 'f':
            f = open(num[1],'wb')

            while True:
                data = s.recv(1024)
                if data == b'##':
                    f.close()  
                    break
                f.write(data)
            s.send(b"OK")
            print("文件：%s 接收完毕" % filename)
        elif num[0] == 'd':
            os.mkdir(num[1])
            s.send(b"OK")
        elif num[0] == 'b':
            break

    

def do_put(s,filename):
    if os.path.isfile(filename):
        s.send(("f "+filename).encode())
        time.sleep(0.1)
        f = open(filename,'rb')

        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                s.send(b'##')
                break
            s.send(data)
        if (s.recv(128).decode())=='OK':
            print(filename,'传输成功')
        else:
            print(filename,'传输失败')
        f.close()
    else:
        s.send(("d "+filename).encode())
        if (s.recv(128).decode())=='OK':
            print(filename,'传输成功')
        else:
            print(filename,'传输失败')
        time.sleep(0.1)
        filelist = os.listdir(filename)
        for i in filelist:
            do_put(s,filename+'/'+i)
def do_dir(s,dirname):
    s.send(('C '+dirname).encode())
    data=s.recv(48).decode()
    if data=='OK':
        return
    else:
        print('Failed:打开失败，不是目录')
        return