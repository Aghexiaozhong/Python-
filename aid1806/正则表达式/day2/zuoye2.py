#zuoye2.py

import re
import sys


# s = sys.argv[1]
# pattern = r'\d{1,3}\.\d{1,3}\.{1,3}\.\d{1,3}/{1}\d{2}'

# f = open('1.txt','r')

# while True:
#     while True:
#         t = []
#         data = f.readline()
#         t.append(data)
#         if not data:
#             if s in t:
#                 l = re.findall(pattern,t)
#                 print(l)
                
            
        
#     data = f.readline()
#     if not data:
#         break


def getAddrress(s):

    f = open('1.txt','r')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        if not data:
            break
        port = re.match(r'\S+',data).group()
        #判断是否为目标段
        if port == s:
            
            pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            addr = re.search(pattern,data).group(1)
            return addr

if __name__ == '__main__':
    s = sys.argv[1]
    print(getAddrress(s))





