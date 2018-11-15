#abc.py

# from database import Mydatabase

# sqlh = Mydatabase('ni')
# nm = 'nihao'
# mn = 23
# sql = 'insert into abc(id,name)\
#  values (%s %s)'
# sqlh.zhixin(sql,[mn,nm])

# 5,用递归求n的阶乘
# ４，打印出斐波那契额的前２０个数
# ３，计算１＋４＋９＋．＋１００００的和

# def fn(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fn(n-1)
# print(fn(7))

# def fn(n):
    
#     i = 0
#     a = 0 
#     b = 1

#     while i < n:
#         v = b
#         a,b = b,a+b
#         print(v)
#         i += 1
# fn(20)

# def fn(n):
#     count = 0
#     for i in range(1,n+1):
#         count += i**2
#     return count
# print(fn(100))

#闭包
# def fn(y):
#     def foo(a,b):
#         return (a+b)**y

#     return foo
# k = fn(2)
# print(k(4,6))

# 7,写一个简单的线程计时器，每隔一秒在屏幕上打印当前时间，
# 时间格式为HH:MM:SS

# 6,编写

# ５，
# ４，
# ３，
# ２，
# １，alist = ['hello','world']

# alist = ['hello','world']
# for index,value in enumerate(alist):
#     print('index',index,value)


# from majiang_database import Mydatabase
# sqlh = Mydatabase('mysql')
# sql = "select * from user"
# res = sqlh.chaxun(sql)
# print(res)

# l = [2,3,45,6,6,6,7,8,2,7,9]
# def fn(l):
#     l2 = []
#     for i in l:
#         if i not in l2:
#             l2.append(i)

#     return l2

# print(fn(l))


# class Student:
#     def __init__(self,name,age,score):
#         self.name,self.age,self.score = name,age,score

#     def __repr__(self):
#         return 'Hello World'

#     def infos(self):
#         m = 'Hello China'
#         return m
#     def __str__(self):
#         return self.infos()

# s1 = Student('Bob',30,88)
# print(s1)


def yanghui(n):
    R = []
    l = [1]
    for i in range(n):

        R.append(l)

        next_l = [1]
        for i in range(len(l)-1):
            next_l.append((l[i]+l[i+1]))
        next_l.append(1)
        l = next_l
    return R
# print(yanghui(6))

def xianshi(l):
    for p in l:
        str_list = [str(x) for x in p]
        
    
        for i in str_list:

            print(i,end='\t')
        print()   

xianshi(yanghui(6))















# 总结：运算符重载　　多进程　多线程　　map filter 迭代器　生层器　
# 消息队列　　管道　　共享内存　　进程池　　httpserver  电子词典　携程　
# git  css  js  mongodb  mysql 