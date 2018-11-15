

import pymysql
db=pymysql.connect(host='localhost',user='root',password='123456'
    ,database='db4',charset='utf8')
cur=db.cursor()

s_id=input('请输入省标号：')
s_name=input('省名称：')

try:
    sql_insert='insert into sheng(s_id,s_name) \
    values(%s,%s);'
    cur.execute(sql_insert,[s_id,s_name])
    print('ok')
    db.commit()
except Exception as e:
    db.rollback()
    print('Failed',e)
cur.close()
db.close()


关于中期项目思路：
1 在mysql数据库中创建库 表（注册表，好友表，）
2 实现自动加密（sha1+insert+注册表），和验证账号密码（sha1+select+注册表+用户ID）
3 实现 python和MySQL的交互
4 生成一个游戏id加上自增长属性
5 添加好友到好友表（搜索注册表里的id或者用户名）
6 用户名不能重复，不能有特殊字符，若有提示错误
7 注册表表中信息 "游戏ID 用户名 密码 性别 电话 密保问题 居住城市"好友表"游戏id 用户名 性别" 
8 退出








