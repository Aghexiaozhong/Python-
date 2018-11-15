#debuger.py

import sys
import pdb

def add(a=0,b=0):
    return int(a) + int(b)

def sub(a=0,b=0):
    return int(a) - int(b)

def main():
    print(sys.argv)
    #设置初始断点
    pdb.set_trace()
    addition = add(sys.argv[1],sys.argv[2])
    print(addition)
    subtraction = sub(sys.argv[1],sys.argv[2])
    print(subtraction)

if __name__ == '__main__':
    main()












