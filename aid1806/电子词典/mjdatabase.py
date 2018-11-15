#! /usr/bin/python3
from pymysql import *

class Mydatabase:
    def __init__(self,host='localhost',port=3306,db='mysql',
                 user='root',passwd='123456',charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host,port=
               self.port,db=self.db,user=self.user,
               passwd=self.passwd,
               charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def check_usrexist(self,name): #注册时判断用户名存在性
        self.open()
        sql = "select * from user where username='%s'"
        self.cursor.execute(sql %name)
        r = len(self.cursor.fetchall())
        self.conn.commit()
        self.close()
        if r > 0:
            return 0
        else:
            return 1

    def check_login(self,name,passwd): #判断用户名密码的一致性

        if self.check_usrexist(name):
            return 0
        self.open()
        sql = "select password from user where username='%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        if r[0] == passwd:
            return 1
        else:
            return 0

    def insert_user(self,name,passwd,niname,telnum): #新用户注册
        self.open()
        sql = "insert into user(username,password,user_nicheng,telnum)\
               values('%s',%d,'%s','%s')"
        self.cursor.execute(sql %(name,int(passwd),niname,telnum))
        self.conn.commit()

        sql = "select userid from user where username = '%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()

        sql = "insert into game(uid) values(%d)"
        r = self.cursor.execute(sql %r[0])
        self.conn.commit()

        self.close()

    def user_login(self,name):  #用户每次登录 登录次数加一
        self.open()
        sql = "update user set login_count = login_count + 1\
               where username = '%s'"
        self.cursor.execute(sql %name)
        self.conn.commit()
        self.close()