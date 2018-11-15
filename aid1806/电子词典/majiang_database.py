#!/usr/bin/python3

from pymysql import *

class Mydatabase():
    def __init__(self,database,host='localhost',port=3306,\
        user='root',passwd='123456',charset='utf8'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.passwd = passwd
        self.charset =charset

    def open(self):
        self.db = connect(host=self.host,port=self.port,\
            database=self.database,user=self.user,passwd=self.passwd,\
            charset=self.charset)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def zhixin(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            self.db.commit()
            # print('ok')

        except Exception as e:
            self.db.rollback()
            print('Field',e)
        self.close()

    def chaxun(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print('Filed',e)
        self.close()

































