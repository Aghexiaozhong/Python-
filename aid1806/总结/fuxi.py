#fuxi.py

# def quick_paixu(array,start,end):
#     i = start
#     j = end
#     if i >= j:
#         return
#     port = array[i]
#     while i < j:
#         if port <= array[j]:
#             j -= 1
#         array[i] = array[j]
#         if array[i] <= port:
#             i += 1
#         array[j] = array[i]
#     array[i] = port

#     quick_paixu(array,start,i-1)
#     quick_paixu(array,i+1,end)
#     return array
# array = [2,3,5,1,-3,-5,-2,6,78,48]
# print(quick_paixu(array,0,(len(array)-1)))


# import itertools  as it
# def luoxuan(m,n):
#     move = it.cycle(['r','d','l','u'])
#     pop = dict.fromkeys((x,y) for x in range(m)\
#         for y in range(n))
#     iters = {'r':(1,0),'d':(0,1),'l':(-1,0),'u':(0,-1)}
#     pos = (0,0)
#     next_it = next(move)
#     for i in range(1,m*n+1):
#         oldpos = pos
#         pos = tuple(map(sum,zip(pos,iters[next_it])))
#         if (pos not in pop) or pop[pos]:
#             next_it = next(move)
#             pos = tuple(map(sum,zip(oldpos,iters[next_it])))
#         pop[oldpos] = i
#     return pop

# def xianshi(m,n):
#     pop = luoxuan(m,n)
#     for i in range(n):
#         for j in range(m):
#             k = pop[(j,i)]
#             print('%2d' % k,end = ' ')
#         print()

# xianshi(5,4)

# id_list = [1,2,3,3,3,4,5,5,6,6,7,7,8,9]
# res = []
# for i in range(13):
#     try:
        
#         if id_list[i] == id_list[i+1] and\
#                 id_list[i] != id_list[res[-1]]:
#             res.append(i)
#     except IndexError:
#         res.append(i)
# print(res)






create table user(
     userid int primary key auto_increment,
     username varchar(20),
     password varchar(20),
     nicheng varchar(20),
     telnum char(11));






