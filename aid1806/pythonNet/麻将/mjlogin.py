from socket import *
from select import *
import time
from time import *
import sys
import database
import random
d = mjdatabase.Mydatabase()


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8880))
s.listen(10)

# 创建ＩＯ事
# 件地图
fdmap = {s.fileno(): s}  # 前面代号，后面套接子
# 创建poll对象
p = epoll()
# 将套接字加入到关注
p.register(s, (EPOLLIN | EPOLLERR))
dzongfang = {}
pzongfang = {}
mingzi = ""
lpai = []

sockfd1 = socket(AF_INET, SOCK_STREAM, 0)
sockfd1.connect(('0.0.0.0', 8867))  # 绑定斗地主服务器ip
p.register(sockfd1, (EPOLLIN | EPOLLERR))
fdmap[sockfd1.fileno()] = sockfd1


def zhuce(lx):
    print(777)
    name = lx[1]
    mima = lx[2]
    shoujihao = lx[3]
    nicheng = lx[4]
    if d.check_usrexist(name):  # 检测账号
        print(6666)
        fdmap[fd].send("True".encode())  # 发回监测结果
        d.insert_user(name, mima, shoujihao, nicheng)  # 写入数据库
        print(99999)
    else:
        print(777)
        fdmap[fd].send("False".encode())  # 发回监测结果


def denglu(lx):
    print(lx)
    name = lx[1]
    mima = lx[2]
    if d.check_login(name, mima):
        fdmap[fd].send("True".encode())
        global mingzi
        mingzi = name

    else:
        fdmap[fd].send("False".encode())


def dizhu(lx):
    if lx[1] == "客户":
        dizhukehu(lx)
    if lx[1] == "服务器":
        dizhufuwuqi(lx)



def dizhukehu(lx):
    if lx[2] == "开房间":  # 地主　客户　开房间　房间号
        if lx[3] in dzongfang:
            fdmap[fd].send("已经有同名房间了，请从新输入信息间隔".encode())
        else:
            # 以房间号为键，已套接子列表为键值！！注意是列表，方便后面加入其他套接子
            dzongfang[lx[3]] = [fdmap[fd]]
            fdmap[fd].send(("已经创建成功，请房间号为%s" % lx[3]).encode())
    elif lx[2] == "进入房间":  # 地主　客户　进入房间　房间号
        if lx[3] in dzongfang:
            if len(dzongfang[lx[3]])<3:
                dzongfang[lx[3]].append(fdmap[fd])  # 追加套接子进房间号内的列表
                fdmap[fd].send("已经加入".encode())
                if len(dzongfang[lx[3]]) == 3:
                    sleep(0.1)
                    sockfd1.send(("开房间吧^%s" % lx[3]).encode())
                    print("满人了,马上开始")
                print("加入成功")
            else:
                fdmap[fd].send(("已经满人").encode())
        else:
            fdmap[fd].send(("无法找到房间号为%s" % lx[3]).encode())
    elif lx[2] == "出牌":  # 地主　客户　出牌　房间号
        if lx[4] == "抢地主":
            a = dzongfang[lx[3]]
            s = a.index(fdmap[fd])
            lp = []
            lp.append(str(s))
            lh = lx[2:5] + lp + lx[5:]
            sockfd1.send(("^".join(lh)).encode())
        else:
            sockfd1.send(("^".join(lx[2:])).encode())
    elif lx[2] == "快速开始":
        global lpai
        if lpai == []:
            print(7777)
            a = random.random() * 10000  # 随机房间号
            b = str(int(a))
            while b in dzongfang:
                a = random.random() * 10000  # 随机房间号
                b = str(int(a))
            fdmap[fd].send(b.encode())
            lpai.append(b)
            lpai.append(fdmap[fd])
            dzongfang[b] = [fdmap[fd]]
        elif len(lpai) == 3:
            print(6666)
            hao = lpai[0]
            print(6666)
            fdmap[fd].send(hao.encode())
            sleep(0.1)
            print(66666)
            dzongfang[hao].append(fdmap[fd])
            lpai = []
            print(66666666)
            sockfd1.send(("开房间吧^%s" % hao).encode())
            print(6666666666666)

        else:
            print(8888)
            hao = lpai[0]
            lpai.append(fdmap[fd])
            fdmap[fd].send(hao.encode())
            dzongfang[hao].append(fdmap[fd])
    elif lx[2] == "结算一":
        if fdmap[fd] == dzongfang[lx[4]][0]:
            dzongfang[lx[4]][1].send("上家胜利".encode())
            dzongfang[lx[4]][2].send("下家胜利".encode())
        if fdmap[fd] == dzongfang[lx[4]][1]:
            dzongfang[lx[4]][2].send("上家胜利".encode())
            dzongfang[lx[4]][0].send("下家胜利".encode())
        if fdmap[fd] == dzongfang[lx[4]][2]:
            dzongfang[lx[4]][0].send("上家胜利".encode())
            dzongfang[lx[4]][1].send("下家胜利".encode())
#  l[6]是胜利者名字，理论应该给他加积分



def dizhufuwuqi(lx):
    if lx[2] == "出牌":  # 地主　服务器　出牌　房间号码　发到某人　内容
        if lx[3] in dzongfang:  # 房间号在总房间内
            d = dzongfang[lx[3]][int(lx[4])]  # 根据房间号和服务端２发来的顺序取套接子
            d.send(("^".join(lx[5:])+"信息间隔").encode())  # 将服务器２发来的信息发送给对应的人

    if lx[2] == "结算":
        pass


while True:
    # 进行监控
    events = p.poll()
    # print(events)
    for fd, event in events:
        try:
            if fd == s.fileno():
                c, addr = fdmap[fd].accept()
                print("connect from", addr)
                p.register(c, EPOLLIN)
                fdmap[c.fileno()] = c  # 将套接字加入字典
            elif event & EPOLLIN:
                data = fdmap[fd].recv(2048)
                print(data.decode())
                if not data:
                    p.unregister(fd)
                    fdmap[fd].close()
                    del fdmap[fd]
                jie = data.decode()
                fenjiange = jie.split("信息间隔")
                for jie2 in fenjiange:
                    fenjie = jie2.split("^")
                    if not data:
                        pass
                    fuwu = fenjie[0]
                    # fuwu2=fenjie[1]
                    if not data:
                        pass
                    elif fuwu == "登录":
                        denglu(fenjie)
                    elif fuwu == "注册":
                        print(666)
                        zhuce(fenjie)
                    elif fuwu == "地主":
                        dizhu(fenjie)
                    elif fuwu == "查询成绩":
                        chaxunchengj(fenjie)
                    elif fuwu == "退出":
                        pass
        except:
            pass