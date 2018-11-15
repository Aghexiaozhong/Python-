import random
from socket import *
from time import sleep
from multiprocessing import Pool
# 创建流式套接字
sockfd = socket(AF_INET, SOCK_STREAM, 0)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定ＩＰ端口
sockfd.bind(('127.0.0.1', 8867))

# 设置监听套接字，创建监听队列
sockfd.listen(5)
c, addr = sockfd.accept()
print("connect from", addr)

d = {}
# 发送规范   地主　服务器　出牌　房间号码　发到某人　内容
sf = "地主^服务器^出牌^"


class Fangjian():

    def __init__(self, s,):
        self.name = s
        self.wei1 = "0"
        self.wei2 = "1"
        self.wei3 = "2"
        self.wei4 = '3'
        self.dizhuming = ""
        self.gong = ""
        self.gangchupai = ""
        self.pai1 = ""
        self.pai2 = ""
        self.pai3 = ""
        self.pai4 = ""
        self.xifapai()
    def xifapai(self):  # 洗牌发牌，发请0位置抢地主，积分为0
        
        l=[]
        for i in range(1,10):
            for j in ['D','W','T']:
                l.append(str(i)+j)
        l = l*4
        lzong = l
        random.shuffle(lzong) 
        print(lzong)
        s1 = "^".join(lzong[:14])
        self.pai1 = s1
        s2 = "^".join(lzong[14:27])
        self.pai2 = s2
        s3 = "^".join(lzong[27:40])
        self.pai3 = s3
        s4 = "^".join(lzong[40:53])
        self.pai4 = s4
        self.gong = "^".join(lzong[53:])

        print(self.gong)
        c.send((sf + self.name + "^" + self.wei1 + "^" + s1 + "信息间隔").encode())
        c.send((sf + self.name + "^" + self.wei2 + "^" + s2 + "信息间隔").encode())
        c.send((sf + self.name + "^" + self.wei3 + "^" + s3 + "信息间隔").encode())
        c.send((sf + self.name + "^" + self.wei4 + "^" + s4 + "信息间隔").encode())

        self.qiangdizhu("0", 0)
        def qiangdizhu(self, s, n):  # 传入要几号位置抢地主，和现在的积分，方法将按照信息发送消息
        c.send((sf + self.name + "^" + s + "^请抢庄家" +
                "^" + str(n) + "信息间隔").encode())
    
    def fasuibchu(self):  # 发送随便出牌
        c.send((sf+self.name+"^"+self.wei1+"^出牌"+"信息间隔").encode())

    def weizhichu1(self, lx):  # 发送位置0出牌打牌，给其他人
        c.send((sf+self.name+"^"+self.wei2+"^上家出牌^"+"^".join(lx)+"信息间隔").encode())
        c.send((sf+self.name+"^"+self.wei3+"^下家出牌^"+"^".join(lx)+"信息间隔").encode())
        c.send((sf+self.name+"^"+self.wei4+"^下家出牌^"+"^".join(lx)+"信息间隔").encode())
        if lx[-1] != "0":
            # self.fayaodachu1()
            c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())
            return self

    def weizhichu2(self, lx):  # 发送位置１出牌打牌，给其他人
        if lx[0] == "过":
            c.send((sf+self.name+"^"+self.wei3+"^上家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei1+"^下家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei4+"^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.fayaodachu2()
            return self
        else:
            c.send((sf+self.name+"^"+self.wei3 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei1 +
                    "^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei4 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3,self.wei4 = self.wei2, self.wei3,self.wei4, self.wei1
            if lx[-1] != "0":
                c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())
                return self

    def weizhichu3(self, lx):  # 发送位置２出牌打牌，给其他人
        if lx[0] == "过":
            c.send((sf+self.name+"^"+self.wei1+"^上家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2+"^下家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei4+"^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.fasuibchu()
            return self
        else:
            c.send((sf+self.name+"^"+self.wei1 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2 +
                    "^下家出牌^"+"^".join(lx)+"信息间隔").encode())
             c.send((sf+self.name+"^"+self.wei4 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3 ,self.wei4 = self.wei3, self.wei4, self.wei1, self.wei2
            if lx[-1] != "0":
                c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())
                return self
    def weizhichu4(self, lx):  # 发送位置3出牌打牌，给其他人
        if lx[0] == "过":
            c.send((sf+self.name+"^"+self.wei1+"^上家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2+"^下家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei3+"^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            
            self.fasuibchu()
            return self
        else:
            c.send((sf+self.name+"^"+self.wei1 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2 +
                    "^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3,self.wei4 = self.wei4 ,self.wei3, self.wei1, self.wei2
            if lx[-1] != "0":
                c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())
                return self

































