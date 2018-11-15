#fuxi.py

# def yanghui(n):
#     pop = []
#     l = [1]
    
#     for i in range(n):
#         pop.append(l)
#         next_l = [1]
#         for j in range(len(l)-1):
#             next_l.append(l[j]+l[j+1])
#         next_l.append(1)
#         l = next_l
        
#     return pop
# print(yanghui(6))

# def fu(t):
#     def fo(a,x):
#         print('fi又被调用')
#         t(a,x)
#         return a+x
#     return fo

# def fn(y):
#     def foo(a,x):
#         print('fi被调用')
#         y(a,x)
#         return a**x
#     return foo
# @fn
# @fu
# def fi(a,x):
#     pass
# #fi=fn(fi)
# print(fi(2,3))




create table user(
     userid int primary key auto_increment,
     username varchar(20) not null unique,
     password varchar(20) not null,
     nicheng varchar(20) not null,
     telnum char(11)
     );
























