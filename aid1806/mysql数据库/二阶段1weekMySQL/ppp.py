import pymysql
db=pymysql.connect(host='localhost',user='root',password='123456'
    ,database='db4',charset='utf8')
cur=db.cursor()

try:
    sql_select='select * from sheng;'
    cur.execute(sql_select)

    data1=cur.fetchone()
    print(data1)
    print("***************")

    data2=cur.fetchmany(3)
    for x in data2:
        print(x)
    print("***************")

    data3=cur.fetchall()
    for i in data3:
        print(i)
    print("***************")

    db.commit()
except Exception as e:
    print('e')
    cur.close()
    db.close()