from socket import *
import tkinter as tk
from tkinter import messagebox
import pickle
import time
import sys
new_name = ""
image = None
image_file = None
nameid = ""
sockfd = socket()
sockfd.connect(('127.0.0.1', 8880))

# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from socket import *
import threading
file_path = './obj/images/'
loading_image = file_path + 'loading.png'
guo = file_path + 'guo.bmp'
backgroundsheng_image = file_path + 'backgroudsheng.png'
backgroundbai_image = file_path + 'backgroudbai.png'
background_image = file_path + 'background.png'
# shengli = file_path+"shengli.png"
shibai = file_path+"shibai.png"
send_image = file_path + 'cp.png'
refuse_image = file_path + 'bc.png'
fen1 = file_path+'fen1.bmp'
fen2 = file_path+'fen2.bmp'
fen3 = file_path+'fen3.bmp'
fen0 = file_path+'fen0.bmp'
dizhu = file_path+'dizhu.png'
pinming = file_path+'pinming.png'
xiaobei = file_path+'xiaobei.bmp'
bei2 = file_path+"bei2.bmp"

lzuikai = [] # 手牌
lgongpai = [] #　底牌
shangjiashenfen = "" # 上家身份
xiajiashenfen = "" # 下家身份
benrenshenfen = "" # 本人身份
lshangjia = [] # 下家出牌
lxiajia = [] # 上家出牌
lgangchu = [] # 自己刚出的牌
shangsheng = '17' #　上家剩余牌数
xiasheng = '17' # 下家剩余牌数
dizhufangjianhao = "" # 地主房间号
qianzhui = "地主^客户^出牌^"+dizhufangjianhao
y1 = 0
n = 11  # 10秒倒计时计数
c = ''
tuichu = 0

def dizhumain(s):
    pygame.init()
    screen = pygame.display.set_mode((900, 600), 0, 32)
    loading = pygame.image.load(loading_image).convert()
    guos = pygame.image.load(guo).convert()

    screen.blit(loading, (0, 0))  # 画等待
    pygame.display.update()
    sleep(1)
    backgroundsheng=pygame.image.load(backgroundsheng_image).convert()
    backgroundbai=pygame.image.load(backgroundbai_image).convert()
    
    background = pygame.image.load(background_image).convert()
    screen.blit(background, (0, 0))  # 画背景

    send_pokers = pygame.image.load(send_image).convert()
    refuse_pokers = pygame.image.load(refuse_image).convert()
    fen1s = pygame.image.load(fen1).convert()
    fen2s = pygame.image.load(fen2).convert()
    fen3s = pygame.image.load(fen3).convert()
    fen0s = pygame.image.load(fen0).convert()
    # shenglis = pygame.image.load(shengli).convert()
    shibais = pygame.image.load(shibai).convert()
    dizhus = pygame.image.load(dizhu).convert()
    pinmings = pygame.image.load(pinming).convert()
    xiaobeis = pygame.image.load(xiaobei).convert()
    bei2s = pygame.image.load(bei2).convert()
    global lshangjia, lxiajia, lzuikai
    name = s
    d = 0

    def daojishi():  # 倒计时函数，
        global n
        while True:
            n -= 1
            sleep(1)
            if n <= 0:
                break

    def huasheng():  # 绘制剩余牌数字
        myfont = pygame.font.Font(None, 30)
        whit = 255, 255, 255
        shuzi1 = myfont.render(shangsheng, False, whit)
        screen.blit(shuzi1, (50, 300))
        shuzi2 = myfont.render(xiasheng, False, whit)
        screen.blit(shuzi2, (850, 300))

    def daojishihuitu():  # 绘制倒计时
        global n

        myfont = pygame.font.Font(None, 40)
        whit = 0, 0, 255
        if n > 0:
            shuzi3 = myfont.render(str(n), False, whit)
            screen.blit(shuzi3, (600, 400))

    def dayin(L, x, y):  # 传入要打印牌扑克的列表，和起始的坐标点,打印出扑克
        for h in L:
            hs = pygame.image.load(file_path+h+".jpg").convert()
            screen.blit(hs, (x, y))
            x += 20

    def greater_than(lzuikai, weizhi, c):  # 传入手拍列表，和上次人出牌，请玩家在手中选择，比上次牌大的，或者跳过不出牌
        while True:
            print("能管上吗?")
            t = threading.Thread(target=daojishi)
            t.start()
            L1 = click(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a == '':
                # background = pygame.image.load(background_image).convert()
                # screen.blit(background, (0, 0))
                sockfd.send((qianzhui+weizhi+"过").encode())
                global lgangchu
                lgangchu = ["过"]
                print("管不上")
                return
            else:
                if jian2(a, c):
                    print("zhen")
                    chuqu(lzuikai, a)

                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    sheng = len(lzuikai)
                    sockfd.send((qianzhui+weizhi+a+"^"+str(sheng)).encode())
                    return


                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(("地主^客户^结算一^胜利^"+dizhufangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        result = "win"
                        dizhushenglihui(result)
                        return

                else:
                    print("输入错误，请重新输入")

    def jian1(a):  # 检测随意出牌,但要符合出牌基本规则
        xinl = paixu(a)
        L = xinl.split("^")
        l = []
        for x in L:
            y = hou(x)
            l.append(y)
        if len(l) == 2:
            if l == [16, 17]:
                combo = {"type":"Boms","key":17,"length":2}
                return combo
        if len(l) == 1:
            combo = {"type":"single","key":l[0],"length":1}
            return combo
        if len(l) == 2:
            if l[0] == l[1]:
                combo = {"type":"double","key":l[0],"length":2}
                return combo
            return False
        if len(l) == 3:
            if l[0] == l[1] and l[0] == l[2]:
                combo = {"type":"three","key":l[0],"length":3}
                return combo
            return False
        if len(l) == 4:
            m = {}
            for x in l:
                if x not in m:
                    m[x] = 1
                else:
                    m[x] += 1
            for y in m:
                if m[y] == 4:
                    combo = {"type":"Boms","key":y,"length":4}
                    return combo
                elif m[y] == 3:
                    combo = {"type":"three_one","key":y,"length":4}
                    return combo
            return False
        if len(l) > 4:
            m = {}
            for x in l:
                if x not in m:
                    m[x] = 1
                else:
                    m[x] += 1
            if len(l) % 4 == 0:
                j = 0
                three = []
                for y in m:
                    if m[y] == 3:
                        three.append(m[y])
                        j += 1
                if j >= (len(l)//4):
                    for x in range(len(l)//4):
                        if three[x] != three[0] + x or three[-1] > 14:
                            break
                        combo = {"type":"three_one","key":three[0],"length":len(l)}
                        return combo
            if len(l) == 6:
                for y in m:
                    if m[y] == 4:
                        combo = {"type":"four_two","key":y,"length":6}
                        return combo 

            for y in m:
                if m[y] != 2:
                    for x in range(len(l)):
                        if l[x] != l[0] + x or l[-1] > 14:
                            return False
                    combo = {"type":"stright","key":l[0],"length":len(l)}
                    return combo
            for z in range(len(l)//2):
                if l[2*z] != l[0] + z or l[-1] > 14:
                    return False
            combo = {"type":"double_stright","key":l[0],"length":len(l)}
            return combo
            
    def gaishuju(dazong):  # 收到抢地主信息，改３家的身份，和地主的牌数，和公共牌
        global lzuikai, lgongpai, shangjiashenfen, xiajiashenfen, benrenshenfen
        lshuju = dazong.split("^")
        dizhuname = lshuju[1]
        lgongpai = lshuju[3:-1]
        # lzuikai = (lzuikai+lshuju[3:-1]).copy

        if lshuju[-1] == "本人":
            print(lzuikai)
            shangjiashenfen = "贫民"
            xiajiashenfen = "贫民"
            benrenshenfen = "地主"
        if lshuju[-1] == "上家":
            shangjiashenfen = "地主"
            xiajiashenfen = "贫民"
            benrenshenfen = "贫民"
            global shangsheng
            shangsheng = "20"
        if lshuju[-1] == "下家":
            shangjiashenfen = "贫民"
            xiajiashenfen = "地主"
            benrenshenfen = "贫民"
            global xiasheng
            xiasheng = "20"

    def click(lzuikai):  # 鼠标事件，点鼠标选择扑克,每秒打印１次倒计时，超时返回空
        # screen.blit(send_pokers, (610, 250))
        # screen.blit(refuse_pokers, (610, 330))
        global n,ncun
        print(99999)
        n = ncun
        n1 = n
        print(n1)
        print(n)
        pygame.display.update()
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        L1 = []
        move_poker(L1, lzuikai)
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(260, 260 + len(a3) * 20) and y in range(430, 581):
                            ss = (x - 260) // 20
                            if a3[ss] in L1:
                                L1.remove(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(260 + len(a3) * 20, 260 + len(a3) * 20 + 85) and y in range(430, 581):
                            if a3[-1] in L1:
                                L1.remove(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(610, 661) and y in range(250, 291):
                            print(L1, '22222')

                            ncun=n
                            n=0
                            return L1
                        elif x in range(610, 661) and y in range(330, 371):
                            n = 0
                            L1 = []
                            return L1
                    except:
                        continue
            if n1 != n:
                n1 = n
                move_poker(L1, lzuikai)
            if n < 1:
                return []

    def click2(lzuikai):  # 鼠标事件，点鼠标选择扑克,每秒打印１次倒计时，超时返回地一个扑克
        # screen.blit(send_pokers, (610, 250))
        # screen.blit(refuse_pokers, (610, 330))
        global n
        print(99999)
        n1 = n
        pygame.display.update()
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        L1 = []
        move_poker(L1, lzuikai)
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(260, 260 + len(a3) * 20) and y in range(430, 581):
                            ss = (x - 260) // 20
                            if a3[ss] in L1:
                                L1.remove(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(260 + len(a3) * 20, 260 + len(a3) * 20 + 85) and y in range(430, 581):
                            if a3[-1] in L1:
                                L1.remove(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(610, 661) and y in range(250, 291):
                            print(L1, '22222')
                            n = 0
                            return L1
                        elif x in range(610, 661) and y in range(330, 371):
                            n = 0
                            L1 = []
                            return L1
                    except:
                        continue
            if n1 != n:
                n1 = n
                move_poker(L1, lzuikai)
            if n < 1:
                print(a3[0])
                L1 = []
                L1.append(a3[0])
                return L1

    def move_poker(L1, lzuikai):  # 打印出点鼠标后，扑克的新顺序
        # screen.blit(background, (0, 0))
        # screen.blit(xiaobeis, (0, 200))
        # screen.blit(xiaobeis, (800, 200))
        huasheng()
        # huayichupai2()
        screen.blit(bei2s, (0, 400))
        screen.blit(send_pokers, (610, 250))
        screen.blit(refuse_pokers, (610, 330))
        daojishihuitu()
        shenfenhuizi()
        x1 = 0
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':
                win_lose(u"YOU WIN!!!")
                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            if poker2 in L1:
                sa = 400
            else:
                sa = 430
            screen.blit(poker_outhand, (260 + x1, sa))
            x1 += 20
        # sleep(0.01)
        pygame.display.update()

    def informal(name, lzuikai):  # 随意出牌
        print("随便出")
        while True:
            t = threading.Thread(target=daojishi)
            t.start()
            L1 = click2(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a != "":
                if jian1(a):
                    chuqu(lzuikai, a)
                    global lgangchu
                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print(l1)
                    background = pygame.image.load(
                        background_image).convert()
                    screen.blit(background, (0, 0))
                    for poker2 in l1:
                        poker_outhand = pygame.image.load(
                            file_path + poker2 + '.jpg').convert_alpha()
                        screen.blit(poker_outhand, (250 + x1, 300))
                        x1 += 20
                        # sleep(0.01)
                        # pygame.display.update()
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    print(lzuikai)
                    sheng = len(lzuikai)
                    sockfd.send(
                        (qianzhui+"^位置一出牌^"+'^'.join(L1)+"^"+str(sheng)).encode())



                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(
                            ("地主^客户^结算一^胜利^"+dizhufangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        result = "win"
                        dizhushenglihui(result)

                    return
                else:
                    print("输入错误，请重新输入")
            else:
                print('输入错误，请重新输入')


    def huayichupai():  # 画已经出的牌（包括，上家，下家，和自己）

        # 上家出牌
        print(lshangjia)
        print(lxiajia)
        print(lgangchu)
        if lshangjia == []:
            pass
        elif lshangjia == ["过"]:
            screen.blit(guos, (225, 225))
        else:

            dayin(lshangjia, 130, 160)

        if lxiajia == []:
            pass
        elif lxiajia == ["过"]:
            screen.blit(guos, (678, 225))
        else:
            dayin(lxiajia, 600, 160)

        if lgangchu == []:
            pass
        elif lgangchu == ["过"]:
            screen.blit(guos, (260, 300))
        else:
            dayin(lgangchu, 300, 250)

        if lgongpai == []:
            pass
        else:

            dayin(lgongpai, 400, 0)


    def refresh(lzuikai):  # 全图刷新
        screen.blit(background, (0, 0))

        screen.blit(xiaobeis, (0, 200))
        screen.blit(xiaobeis, (800, 200))
        huasheng()
        huayichupai()
        shenfenhuizi()
        x1 = 0
        print(lzuikai)

        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':

                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            screen.blit(poker_outhand, (260 + x1, 430))
            x1 += 20
            # sleep(0.01)
        pygame.display.update()

    def dizhushenglihui(result):
        screen.blit(background, (0, 0))
        screen.blit(xiaobeis, (0, 200))
        screen.blit(xiaobeis, (800, 200))
        huasheng()
        huayichupai()
        myfont = pygame.font.Font(None, 130)
        whit = 255, 0, 0
        shenglizi = myfont.render(result, False, whit)
        screen.blit(shenglizi, (300, 200))

        shenfenhuizi()

        x1 = 0
        print(lzuikai)

        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':

                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            screen.blit(poker_outhand, (260 + x1, 430))
            x1 += 20
            # sleep(0.01)
        pygame.display.update()
        sleep(5)
        pygame.quit()

    def shenfenhuizi():
        if benrenshenfen != "":
            if shangjiashenfen == "地主":
                screen.blit(dizhus, (0, 0))
            else:
                screen.blit(pinmings, (0, 0))
            if xiajiashenfen == "地主":
                screen.blit(dizhus, (800, 0))
            else:
                screen.blit(pinmings, (800, 0))
            if benrenshenfen == "地主":
                screen.blit(dizhus, (40, 440))
            else:
                screen.blit(pinmings, (40, 440))

    def jiaofen(n):  # 叫地主事件　如果上次叫分积分0触发
        if n == 0:
            screen.blit(fen1s, (200, 300))
            screen.blit(fen2s, (350, 300))
        elif n == 1:
            screen.blit(fen2s, (350, 300))
        screen.blit(fen3s, (500, 300))
        screen.blit(fen0s, (650, 300))
        # screen.blit(refuse_pokers, (610, 330))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if n == 0:
                            if x in range(200, 300) and y in range(300, 350):
                                return 1
                            elif x in range(350, 450) and y in range(300, 350):
                                return 2
                        elif n == 1:
                            if x in range(350, 450) and y in range(300, 350):
                                return 2
                        if x in range(500, 600) and y in range(300, 350):
                            return 3
                        elif x in range(650, 750) and y in range(300, 350):
                            return 0
                    except:
                        continue


    def hou(str1):  # 取后两位数字，用于排序
        if str1 == '':
            return
        return int(str1[2:])

    def paixu(a):  # 把字符串根据后两位数字排序
        lp = a.split("^")
        xinl = sorted(lp, key=hou)
        xina = "^".join(xinl)
        return xina

    def jian2(a, b):  # 检测是否符合基本出牌原则,是否比上一家大
        if not jian1(a):
            return False
        l1 = jian1(a)
        l2 = jian1(b)
        if l1["type"] == "Boms" and l2["type"] != "Boms":
            return True
        elif l1["type"] != "Boms" and l2["type"] == "Boms":
            return False
        elif l1["type"] == "Boms" and l2["type"] == "Boms":
            if l1["key"] > l2["key"]:
                return True
            return False

        elif l1["type"] == l2["type"]:
            if l1["length"] == l2["length"]:
                if l1["key"] > l2["key"]:
                    return True
                return False
            return False
        return False

    def chuqu(lzuikai, a):  # 将列表中已出的牌删除
        l1 = a.split("^")
        for x in l1:
            if x in lzuikai:
                lzuikai.remove(x)

    def qiangdizhu(name, dazong):  # 根据收到信息，判断应该调用那个叫分函数
        lq = dazong.split("^")
        n = int(lq[1])
        nxin = jiaofen(n)
        sockfd.send((qianzhui+'^抢地主^'+(str(nxin))+"^"+nameid).encode())

    while True:
        global tuichu
        if tuichu == 1:
            break
        d = 99
        global n,ncun
        n = 30
        ncun = n
        data = sockfd.recv(1024)
        if data == "":
            print(9999)
        dax = data.decode()
        daxf = dax.split("信息间隔")
        for x in daxf:
            dazong = x
            jiezong = dazong.split("^")
            if dazong == "":
                pass
            else:
                if dazong == "上家过":
                    lshangjia = ["过"]
                if dazong == "下家过":
                    lxiajia = ["过"]
                print(data.decode())
                if dazong == "随便出牌":
                    informal(name, lzuikai)
                    if len(lzuikai)==0:
                        return
                elif dazong == "位置二要大出牌":
                    weizhi = "^位置二出牌^"
                    greater_than(lzuikai, weizhi, c)
                    if len(lzuikai)==0:
                        return
                elif dazong == "位置三要大出牌":
                    weizhi = "^位置三出牌^"
                    greater_than(lzuikai, weizhi, c)
                    if len(lzuikai)==0:
                        return
                elif dazong[:4] == "请抢地主":
                    qiangdizhu(name, dazong)
                elif dazong[:3] == "地主名":
                    gaishuju(dazong)
                    print("已经显示地主了")

                elif dazong[:4] == "上家出牌":
                    s2 = dazong.split("^")
                    global  shangsheng
                    c = "^".join(s2[1:-1])
                    lshangjia = s2[1:-1]
                    shangsheng = s2[-1]
                elif dazong[:4] == "下家出牌":
                    s2 = dazong.split("^")
                    global xiasheng
                    c = "^".join(s2[1:-1])
                    lxiajia = s2[1:-1]
                    xiasheng = s2[-1]
                elif dazong=="上家胜利":
                    if  benrenshenfen==shangjiashenfen:
                        result = "win"
                    else:
                        result = "fail"
                    dizhushenglihui(result)
                    return
                elif dazong=="下家胜利":
                    if  benrenshenfen==xiajiashenfen:
                        result = "win"
                    else:
                        result = "fail"
                    dizhushenglihui(result)
                    return


                else:
                    b = dazong
                    if b[:2] in ["ht", "fk", "ho", "mh", "bj"]:
                        if len(b.split("^")) > 16:
                            sp = paixu(b)
                            lzuikai = b.split("^")
                refresh(lzuikai)

        # print(1)
        # refresh(lzuikai)


def jinrugongnengxuanze():
    print("1000")
    global image
    global image_file

    print("1001")

    youxixze = tk.Tk()  # 调用模块创建窗口
    youxixze.title("请选择游戏")  # 窗口题目
    youxixze.geometry("960x540")  # 窗口大小
    youxixze.resizable(False, False)
    youxixze.transient()

    def dikuaisuks():  # 地主快速开始
        sockfd.send(("地主^客户^快速开始").encode())
        data = sockfd.recv(1024)
        global dizhufangjianhao, qianzhui
        dizhufangjianhao = data.decode()
        qianzhui = "地主^客户^出牌^"+dizhufangjianhao
        print(dizhufangjianhao)
        youxixze.destroy()
        time.sleep(2)
        dizhumain(nameid)
        jinrugongnengxuanze()

    def dichuangjianfj():
        difang = entry_dichuang.get()
        sockfd.send(("地主^客户^开房间^"+difang).encode())
        data = sockfd.recv(1024)
        jieguo = data.decode()
        if jieguo[:4] == "已经创建":
            global dizhufangjianhao, qianzhui
            dizhufangjianhao = difang
            qianzhui = "地主^客户^出牌^"+dizhufangjianhao
            youxixze.destroy()
            dizhumain(nameid)
            jinrugongnengxuanze()
        else:
            tk.messagebox.showerror("error", "对不起已经有同名房间")

    def dijiarufj():
        difang = entry_dijia.get()
        sockfd.send(("地主^客户^进入房间^"+difang).encode())
        data = sockfd.recv(1024)
        jieguo = data.decode()
        print(jieguo)
        if jieguo == "已经加入":
            global dizhufangjianhao, qianzhui
            dizhufangjianhao = difang
            qianzhui = "地主^客户^出牌^"+dizhufangjianhao
            youxixze.destroy()
            dizhumain(nameid)
            jinrugongnengxuanze()
        elif jieguo == "已经满人":
            tk.messagebox.showerror("error", "对不起该房间满人")
        else:
            tk.messagebox.showerror("error", "对不起没找到")


    canvas = tk.Canvas(youxixze, width=960, height=540)
    image_file = tk.PhotoImage(file="./tt/xuanzeyouxi/xuanzeyouxi.png")
    youxixze.attributes("-alpha", 0.3)
    image = canvas.create_image(0, 0, anchor="nw", image=image_file)
    canvas.pack(side="top")


    # 斗地主输入房间号
    entry_dijia = tk.Entry(youxixze,width=11,font=("黑体",18,"bold"))
    entry_dijia.place(x=323, y=418)
    entry_dichuang = tk.Entry(youxixze,width=11,font=("黑体",18,"bold"))
    entry_dichuang.place(x=323, y=353)

    image_fileksksd = tk.PhotoImage(file="./tt/xuanzeyouxi/ksksd.png")
    dizhukuaikai = tk.Button(youxixze,image=image_fileksksd,command=dikuaisuks).place(x=154, y=276)

    image_filecjfjd = tk.PhotoImage(file="./tt/xuanzeyouxi/cjfjd.png")
    dizhuchuangj = tk.Button(youxixze,image=image_filecjfjd,command=dichuangjianfj).place(x=154, y=345)

    image_filejrfjd = tk.PhotoImage(file="./tt/xuanzeyouxi/jrfjd.png")
    dizhujiaru = tk.Button(youxixze,image=image_filejrfjd,command=dijiarufj).place(x=154, y=410)


    youxixze.mainloop()


def jiance():
    pass


def zhaohuimima():
    pass


def kaiqi():
    global image

    def denglu():
        user = entry_name.get()
        pwd = entry_pwd.get()
        print(user)
        print(pwd)
        sockfd.send(("登录^" + user + "^" + pwd).encode())
        data = sockfd.recv(1024)
        print(data.decode())
        if data.decode() == "True":
            global nameid
            nameid = user
            win.destroy()
            jinrugongnengxuanze()
        else:
            tk.messagebox.showerror("error", message="用户名密码不正确")

    def zhuce():
        def zhucetijiao():
            nn = entry_new_name.get()  # nn 注册的用户名
            np = entry_user_pwd.get()  # np 注册的密码
            npt = entry_user_pwd_two.get()  # npt 再次确认密码
            sjh = entry_user_sjh.get()  # shj 手机号
            nc = entry_user_nc.get()  # nc 昵称
            if len(nn) < 6 or len(nn) > 18 or " " in nn:
                tk.messagebox.showerror("error", "用户名以字母开头，6-18位字符，不能有空格")
            elif nn[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRASUVWXYZ":
                tk.messagebox.showerror("error", "用户名以字母开头，6-18位字符，不能有空格")
                
            elif len(np) <= 5 or len(np) > 18:
                tk.messagebox.showerror("error", "密码长度在6-18位字符") 
            elif np != npt:
                tk.messagebox.showerror("error", "两次密码不一致") 

            elif sjh[0] != "1" or len(sjh) != 11:
                tk.messagebox.showerror("error", "手机号输入格式不正确")

            elif len(nc) < 6 or len(nc) > 18 or " " in nc:
                tk.messagebox.showerror("error", "昵称6-18位字符，不能有空格")
            else:
                print("注册" + "^" + nn + "^" + np + "^" + sjh + "^" + nc)
                sockfd.send(("注册" + "^" + nn + "^" + np +
                             "^" + sjh + "^" + nc).encode())
                data = sockfd.recv(1024)
                print(data.decode())
                if data.decode() == "True":
                    tanchuang.destroy()
                    tk.messagebox.showinfo("Congratulations", "恭喜您注册成功")
                    win.destroy()
                    jinrugongnengxuanze()
                else:
                    tk.messagebox.showerror("error", message="用户名密码不正确")
# 注册窗口
        tanchuang = tk.Toplevel(win)
        tanchuang.title("欢迎注册乐游天下")
        tanchuang.geometry("630x400")
        tanchuang.resizable(False, False)
        tanchuang.transient(win)

# 注册窗口配置图片
        canvas = tk.Canvas(tanchuang, width=630, height=400)
        image_file = tk.PhotoImage(file="./tt/zhuce/beijing.png")
        image = canvas.create_image(0, 0, anchor="nw", image=image_file)
        canvas.pack(side="top")

        global new_name

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="用户名").place(x=100, y=10)
        entry_new_name = tk.Entry(tanchuang,width=21,font=("黑体",13))
        entry_new_name.place(x=254, y=6)

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="密　码").place(x=100, y=50)
        entry_user_pwd = tk.Entry(tanchuang,width=21,font=("黑体",13),show="*")
        entry_user_pwd.place(x=254, y=60)

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="确认密码").place(x=100, y=90)
        entry_user_pwd_two = tk.Entry(tanchuang,width=21,font=("黑体",13), show="*")
        entry_user_pwd_two.place(x=254, y=115)

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="手机号").place(x=100, y=130)
        entry_user_sjh = tk.Entry(tanchuang,width=21,font=("黑体",13))
        entry_user_sjh.place(x=254, y=170)

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="昵　称").place(x=100, y=170)
        entry_user_nc = tk.Entry(tanchuang,width=21,font=("黑体",13))
        entry_user_nc.place(x=254, y=226)

        # 用户名检测结果提示框
        # var_jiance = tk.StringVar()
        # var_jiance.set = ""
        # lb3 = tk.Label(tanchuang, textvariable=var_jiance,
                       # width=20, height=1).place(x=201, y=30)

        # btn_jiance = tk.Button(tanchuang, text="检测用户名是否可用", command=jiance)
        # btn_jiance.place(x=400, y=10)

        # 注册按钮
        image_filetjzc = tk.PhotoImage(file="./tt/zhuce/tijiaozhuce.png")
        
        btn_tijiao = tk.Button(tanchuang, text="提交注册",image=image_filetjzc, command=zhucetijiao)
        btn_tijiao.place(x=260, y=300)
        win.mainloop()


# 主窗口
    win = tk.Tk()  # 调用模块创建窗口
    win.title("欢迎来到　乐游天下")  # 窗口题目
    win.geometry("960x540")  # 窗口大小
    win.resizable(False, False)
    # 主窗口插入背景图
    canvas = tk.Canvas(win, width=960, height=540)
    image_file = tk.PhotoImage(file="./tt/denglu/denglu2.png")
    image = canvas.create_image(0, 0, anchor="nw", image=image_file)
    canvas.pack(side="top")
    # 主窗口用户名/密码的提示
    # user = tk.Label(win, text="用户名", bg="palegoldenrod").place(x=450, y=300)
    # pwd = tk.Label(win, text="密　码", bg="palegoldenrod").place(x=350, y=360)
    # 用户名输入框
    entry_name = tk.Entry(win,width=24,font=("黑体",18))
    entry_name.place(x=573, y=238)
    # 密码输入框
    entry_pwd = tk.Entry(win, width=24,font=("黑体",18),show="*")
    entry_pwd.place(x=573, y=317)
    image_filed = tk.PhotoImage(file="./tt/denglu/denglu11.png")
    btn_denglu = tk.Button(win, text="登　录",image=image_filed, command=denglu)
    btn_denglu.place(x=573, y=450)

    image_filez = tk.PhotoImage(file="./tt/denglu/zhuce11.png")
    btn_zhuce = tk.Button(win, text="注　册",image=image_filez, command=zhuce)
    btn_zhuce.place(x=783, y=450)

    # image_filezh = tk.PhotoImage(file="./tt/denglu/zhaohui11.png")
    # btn_sign_up = tk.Button(win, text="找回密码",image=image_filezh, command=zhaohuimima)
    # btn_sign_up.place(x=730, y=470)
    win.mainloop()


kaiqi()