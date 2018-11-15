#mongo.py

from pymongo import MongoClient

#创建连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu 

#创建集合对象
myset = db.class4

# print(dir(myset))

#插入操作
# myset.insert({'name':'张铁林','king':'乾隆'})

# myset.insert([{'name':'张国立','king':'康熙'},\
#     {'name':'陈道明','king':'康熙'}])

# myset.insert_many([{'name':'唐国强','king':'雍正'},\
#     {'name':'陈建斌','king':'雍正'}])

# myset.insert_one({'name':'郑少秋','king':'乾隆'})

# myset.save({'_id':1,'name':'吴奇隆','king':'四爷'})
# myset.save({'_id':1,'name':'聂远','king':'乾隆'})
#查找操作

# cursor = myset.find({},{'_id':0})
# for i in cursor:
#     print(i['name'],'---->',i['king'])

# myset = db.class1
# #操作符使用引号变为字符串
# cursor = myset.find({'age':{'$gt':12}},{'_id':0})
# # cursor.limit(2)
# cursor.sort([('age',-1),('name',1)])
# for i in cursor:
#     print(i)
# print(cursor.next())

# dic = {'$or':[{'age':{'$gt':37}},{'sex':'m'}]}
# data = myset.find_one(dic,{'_id':0})
# print(data)

#修改操作
# myset.update({'name':'张国立'},{'$set':\
#     {'king_name':'玄烨'}})


# myset.update({'name':'霍建华'},{'$set':{'king':'乾隆'}},\
#     upsert = True)

# myset.update({'king':'乾隆'},{'$set':{'king_name':'弘历'}},multi = True)

# myset.update_one({'king':'康熙'},{'$set':{'king_name':'爱新觉罗玄烨'}})

# myset.update_many({'king':'雍正'},{'$set':{'king_name':'胤禛'}})

#删除操作
# myset.remove({'king':'康熙'},multi = False)  #删除一条

# myset.remove({'king':'乾隆'},multi = False)

#查找并删除
# print(myset.find_one_and_delete({'king':'乾隆'}))

#关闭连接
conn.close()