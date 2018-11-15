# 快速排序算法


# 简单实现
# def quick(data):
#     if len(data) < 2:
#         return data
#     mark = data[0]
#     smaller = [x for x in data if x < mark]
#     equal = [x for x in data if x == mark]
#     bigger = [x for x in data if x > mark]
#     return quick(smaller) + equal + quick(bigger)


# # 自测代码
# if __name__ == '__main__':
#     values = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
#     print('原数据列表：', values)
#     after = quick(values)
#     print('快速排序后：', after)


def quick(arr):
    if len(arr) < 2:
        return arr
    mark = arr[0]
    smaller = [x for x in arr if x < mark]
    equal = [x for x in arr if x == mark]
    bigger = [x for x in arr if x > mark]
    return quick(smaller) + equal + quick(bigger)

if __name__ == '__main__':
    arr = [2,3,43,2,6,7,-4,-3,6,4]
    print(quick(arr))






















