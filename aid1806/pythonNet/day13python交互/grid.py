#grid.py

from pymongo import MongoClient

#pymongo绑定的模块
import gridfs

conn = MongoClient('localhost',27017)
db = conn.grid

#获取gridfs对象  不代表任意集合  而是综合了
#fs.files  fs.chunks  两个集合的属性内容
fs = gridfs.GridFS(db)

#查找文档生成游标
files = fs.find()

#获取一个文件的对象
for file in files:
    print(file.filename)
    if file.filename == '56.jpeg':
        with open(file.filename,'wb') as f:
            #从数据库中读取出来
            while True:
                data = file.read(1024)
                if not data:
                    break
                f.write(data)


conn.close()












