#msz


from pymysql import *

class msz():
    def __init__(self,database,host='localhost',
        user='root',password='123456',port=3306
        ,charset='utf8'):
        self.host=host
        self.user=user
        self.password=password
        self.port=port
        self.charset=charset
        self.database=database

    def open_file(self):
        self.db=connect(host=self.host,user=self.user
            ,port=self.port,password=self.password,
            charset=self.charset,database=self.database)
        self.cur=self.db.cursor()

    def close_file(self):
        self.cur.close()
        self.db.close()

    def zhixin_file(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            self.db.commit()
            print('ok')
        except Exception as e:
            self.db.rollback()
            print('Failer',e)
        self.close()

    def chaxun_file(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            result=self.cur.fetchall()
            return result
        except Exception as e:
            print('Failed',e)
        self.close()




















































