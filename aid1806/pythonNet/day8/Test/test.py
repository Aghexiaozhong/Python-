#计算密集
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

#io密集
def write():
    f = open("test.txt",'w')
    for x in range(2000000):
        f.write("hello world\n")
    f.close()

def read():
    f = open("test.txt")
    lines = f.readlines()
    f.close()