
import pymysql
db=pymysql.connect(host='localhost',user='root',password='123456'
    ,database='db4',charset='utf8')
cur=db.cursor()
try:
    #cur.execute('insert into sheng values(60,200001,"云南省");')
    #cur.execute('update sheng set id=666 where id=60;')
    cur.execute('alter table sheng add primary key(id);')
    cur.execute('alter table sheng add modify id int auto_increment;')
    #cur.execute('alter table sheng modify id int(3) zerofill;')
    print('ok')
    db.commit()
except Exception as e:
    db.rollback()
    print('出现错误回滚',e) 
cur.close()
db.close()
