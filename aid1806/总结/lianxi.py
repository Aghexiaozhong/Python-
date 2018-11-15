# from multiprocessing import Process
# import os
# from signal import *
# from time import sleep

# def scale_dirver(sig,farme):
#     if sig == SIGUSR1:
#         print('老司机开车了')

#     elif sig == SIGUSR2:
#         print('车速有点快,系好安全带')
#     elif sig == SIGTSTP:
#         os.kill(p.pid,SIGUSR1)


# def scale_shou(sig,farme):
#     if sig == SIGINT:
#         os.kill(os.getppid(),SIGUSR1)
#     elif sig == SIGQUIT:
#         os.kill(os.getppid(),SIGUSR2)
#     elif sig == SIGUSR1:
#         print('到站了，请下车')
#         os._exit(0)

# def driver():
#     signal(SIGINT,scale_shou)
#     signal(SIGQUIT,scale_shou)
#     signal(SIGUSR1,scale_shou)
#     signal(SIGTSTP,SIG_IGN)
#     while True:
#         sleep(1)
#         print('公交车已准备，等待上车')



# p = Process(target=driver)

# p.start()

# signal(SIGTSTP,scale_dirver)
# signal(SIGUSR1,scale_dirver)
# signal(SIGUSR2,scale_dirver)
# signal(SIGINT,SIG_IGN)
# signal(SIGQUIT,SIG_IGN)

# p.join()


# from select import select
# from socket import *

# s = socket()
# ADDR = ('127.0.0.1',8888)
# s.bind(ADDR)
# s.listen(5)
# while True:
#     print('Waitting for connecting...')
#     c,addr = s.accept()
#     print('connect from',addr)
#     while True:
#         data = c.recv(1024).decode()
#         if not data:
#             break
#         print(data)
#         n = c.send(b'ok')

#     c.close()
# s.close()


# from select import select
# from socket import *

# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(('0.0.0.0',8888))
# s.listen(5)

# rlist = [s]
# wlist = []
# xlist = []

# while True:
#     print('等待ＩＯ发生')
#     rs,ws,xs = select(rlist,wlist,xlist)
#     for r in rs:
#         if r is s:
#             c,addr = s.accept()
#             print('connect from',addr)
#             rlist.append(c)
#         else:
#             data = r.recv(1024).decode()
                
#             if not data:
#                 rlist.remove(r)
#                 r.close()
#             print(data)


        











