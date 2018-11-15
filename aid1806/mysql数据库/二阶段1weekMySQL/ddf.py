



from msz import msz
# sqlh=msz('db4')
# # sql_update='update sheng set s_name="日本省" where s_name="云南省";'
# # sqlh.zx(sql_update)
# sql_select="select * from sheng where id=%s;"
# date=sqlh.cx(sql_select,[1])
# print(date)
from hashlib import sha1

u_name=input('用户名:')
pwd=input('密码：')
# 用sha1给pwd加密
s1=sha1() #创建sha1加密对象
s1.update(pwd.encode('utf8'))#指定编码
pwd2=s1.hexdigest()#返回十六进制加密结果
sqlh=msz('db4')
select='select password from user2 where u_name=%s;'
result=sqlh.chaxun(select,[u_name])

if len(result)==0:
    print('用户名不存在')
elif result[0][0]==pwd2:
    print('登录成功')
else:
    print('密码错误')


