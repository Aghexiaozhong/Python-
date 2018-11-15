# 冒泡排序算法


# 简单实现
# def bubble(data):
#     for n in range(len(data)-1):
#         for i in range(len(data)-1-n):
#             if data[i] > data[i+1]:
#                 data[i], data[i+1] = data[i+1], data[i]


# # 自测代码
# if __name__ == '__main__':
#     values = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
#     print('原数据列表：', values)
#     bubble(values)
#     print('冒泡排序后：', values)


# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(i, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#     return array
# array = [1,4,8,2]
# print(bubble_sort(array))

# def bun(arr):
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i] >= arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#     return arr
# arr = [2,3,42,5,1,3,2,8]
# print(bun(arr))



# 1**9+2**8+3**7+...+9**1

# for i in map(lambda x,y:x**y,range(10),range(9,0,-1)):
#     print(i)

# fib = lambda n:1 if n<=2 else fib(n-1) + fib(n-2)
# L = [fib(i) for i in range(1,21)]
# print(L)


# L = [2,3,-3,4-59,78,-89,34]

# L=sorted(L)
# if L[-1]*L[-2] >= L[0]*L[1]:
#     print(L[-1],L[-2])
# else:
#     print(L[0],L[1])


# def ins(arr):
#     for n in range(1,len(arr)):
#         tmp = arr[n]
#         for i in range(n,-1,-1):
#             if arr[i-1] < tmp or i==0:
#                 break
#             else:
#                 arr[i] = arr[i-1]
#         arr[i] = tmp
#     return arr
# arr = [3,4,5,6,3,42,1,4,38,9,-2]
# print(ins(arr))


# fib = lambda n:1 if n <= 2 else fib(n-1)+fib(n-2)
# for i in range(20):
#     print(fib(i))

class Singleton(object):
    def __new__(cls,**args,**kw):
        _instance = None
        if not hasattr(cls,'_instance'):
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls,**args,**kw)
        return cls._instance
class Myclass(object):
    a = 1

one = Myclass.a






















