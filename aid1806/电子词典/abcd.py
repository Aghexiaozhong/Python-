#abcd.py

from database import Mydatabase

sqlh = Mydatabase('ni')
sql = 'select name from abc;'
res = sqlh.chaxun(sql)
print(res)








