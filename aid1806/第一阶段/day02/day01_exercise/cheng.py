# 1. 中国古代的秤是16两一斤,请问古代对216
#    两是古代的几斤几两，写程序打印出来?

liang = 216

jin = 216 // 16  # 得到斤
l = 216 % 16
print('是古代的', jin, '斤', l, '两')
