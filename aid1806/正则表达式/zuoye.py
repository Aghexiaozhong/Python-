#zuoye.py

import re

# f = open('test.txt','r')
# while True:
#     data = f.read(1024)
#     if not data:
#         break

#     l = re.findall(r'\b[A-Z][\._a-zA-Z]+',data)
#     print(l)
#     s = re.findall(r'[-+]?\d+[./]?\d*%?',data)
#     print(s)

def getdanci():
    f = open('dict.txt','r')
    
    while True:
        data = f.readline()
        if not data:
            break
        
        pattern1 = r'[a-z]+\b'
        addr = re.search(pattern1,data).group()
        pattern2 = r'\s+.+'
        try:
            addr2 = re.search(pattern2,data).group()
            addr3 = addr2.strip()
        except AttributeError:
            continue
        print(addr)
        print(addr3)

getdanci()














