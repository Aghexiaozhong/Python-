#daoru.py

import re
from database import Mydatabase



def getdanci():
    f = open('dict.txt','r')
    
    # while True:
    #     data = f.readline()
    #     if not data:
    #         break

    #     sqlh = Mydatabase('cidian')
    #     pattern1 = r'[a-z]+\b'
    #     pattern2 = r'\s+.+'
    #     msg1 = re.search(pattern1,data).group()
    #     try:
    #         msg2 = re.search(pattern2,data).group()
    #         msg3 = msg2.strip()
    #     except AttributeError:
    #         continue

    #     sql = 'insert into words(word,interpret)\
    #      values (%s,%s) ' 
    #     sqlh.zhixin(sql,[msg1,msg3])
        
    for line in f:
        try:
            l = re.split('[ ]+',line)
        except:
            pass
        sqlh = Mydatabase('cidian')
        sql = 'insert into words(word,interpret)\
         values (%s,%s) '
        sqlh.zhixin(sql,[l[0],' '.join(l[1:])])
        


getdanci()


    








