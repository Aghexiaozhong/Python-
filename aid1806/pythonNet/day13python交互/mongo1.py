#mongo1.py

from pymongo import MongoClient

#创建连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu 

myset = db.class1

#删除所有索引
# myset.drop_indexes()

# index = myset.ensure_index('name')
# index = myset.ensure_index([('name',-1),('age',1)])
# print(index)

#删除一个索引
# myset.drop_index('name_1')

#创建特殊索引
# index = myset.ensure_index('name',name = 'myIndex',\
#     unique = True,sparse = True)


# #查看集合中索引
# for i in myset.list_indexes():
#     print(i)

myset = db.class4

l = [{'$group':{'_id':'$king','num':{'$sum':1}}},\
    {'$match':{'num':{'$gt':1}}

    }]
cursor = myset.aggregate(l)
for i in cursor:
    print(i)


conn.close()



