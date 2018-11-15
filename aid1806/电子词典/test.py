#test.py

from database import Mydatabase
sqlh = Mydatabase('cidian')
sql= 'select interpret from words \
 where word=%s'
res = sqlh.chaxun(sql,['abattoir'])

print(res)







