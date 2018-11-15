#save_file.py

from pymongo import MongoClient

#pymongo绑定的模块
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.images

myset = db.img

#存储
# f = open('56.jpeg','rb')

#将读取到的内容转换为mongodb的二进制存储形式
# content = bson.binary.Binary(f.read()) 

#插入到数据库
# myset.insert({'filename':'56.jpeg','data':content})

#提取
data = myset.find_one({'filename':'56.jpeg'})

with open(data['filename'],'wb') as f:
    f.write(data['data'])


conn.close()





