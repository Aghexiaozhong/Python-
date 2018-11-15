import pymysql

db= pymysql.connect(host='localhost',
    user='root',password='123456'
    ,database='db4',charset='utf8')
#利用db方法创建游标对象
cur =db.cursor()
#利用游标对象的execute()方法执行sql命令
cur.execute('insert into sheng values(16,300000,"台湾省");')
# 提交到数据库执行
db.commit()
print('ok')
#关闭游标对象
cur.close()
#断开数据库连接
db.close()