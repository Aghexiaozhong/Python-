# 3. 用while语句实现打印三角形，输入一个整数，表示三角形
#     的宽度和高度,打印出相应的直角三角形:
#   如:
#     请输入三角形的宽度: 4
#     1) 打印如下:
#       *
#       **
#       ***
#       ****
#     2) 打印如下:
#          *
#         **
#        ***
#       ****
#     3) 打印如下:
#       ****
#        ***
#         **
#          *
#     4) 打印如下:
#       ****
#       ***
#       **
#       *


# 请输入三角形的宽度: 4
n = int(input("请输入三解形的宽度: "))

line = 1  # line 代表行数
while line <= n:
    # 打印一行星
    print('*' * line)
    line += 1  # 行数变大
# 1) 打印如下:
#   *
#   **
#   ***
#   ****

print('-------------------')
line = 1
fmt = "%%%ds" % n
while line <= n:
    print(fmt % ('*' * line))
    line += 1
# 2) 打印如下:
#      *
#     **
#    ***
#   ****

print('-------------------')
stars = n  # 第一行星号的个数
while stars > 0:
    # 先计算空格的个数
    blank = n - stars
    print(' ' * blank + '*' * stars)
    stars -= 1  # 下一行星号个数变少一个
# 3) 打印如下:
#   ****
#    ***
#     **
#      *

print('-------------------')
stars = n  # 第一行星号的个数
while stars > 0:
    # 先计算空格的个数
    print('*' * stars)
    stars -= 1  # 下一行星号个数变少一个
# 4) 打印如下:
#   ****
#   ***
#   **
#   *








