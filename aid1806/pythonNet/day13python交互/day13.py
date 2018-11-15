#day13.py

day13.txt

聚合操作：
    对文档的信息进行整理统计的操作
    返回：统计后的文档集合

db.collection.aggregate()
功能：聚合函数，完成聚合操作
参数：聚合条件，配合聚合操作符使用
返回：返回聚合后的结果

集合操作符
    $group  分组聚合  配合具体的统计操作符获取结果
        $sum   求和     

db.class0.aggregate({$group:{_id:'$gender',     
                               分组  按照gender值统计     
                    num:{$sum:1}}})
                    统计结果，求和，每有一个加1

db.class5.aggregate({$group:{_id:'$sex',num:{$sum:'$age'}}})
                                    统计结果，求和，每有一个加age


        $avg 平均值  统计男女生的年龄的平均值
        db.class5.aggregate({$group:{_id:'$sex',num:{$avg:'$age'}}})

        $max
        db.class5.aggregate({$group:{_id:'$sex',num:{$max:'$age'}}})


$project
用于修改文档的显示效果
    project的值用法同find()中filed参数差不多
    db.class5.aggregate({$project:{_id:0,name:1,age:1}})

    db.class5.aggregate({$project:{_id:0,Name:'$name',Age:'$age'}})
         显示结果 比如：       { "Name" : "xiaohong", "Age" : 10 }

$match
过滤想要的数据
        得到年龄大于13岁的文档  值的用法同find()中的query参数一致
  db.class5.aggregate({$match:{age:{$gt:13}}})  

$limit
显示前几个文档
        db.class5.aggregate({$limit:3})

$skip
跳过前几个文档
    db.class5.aggregate({$skip:3})

$sort
排序
    db.class5.aggregate({$sort:{age:1}})


聚合管道
将前一个聚合产生的结果交给后一个聚合操作继续使用
db.collection.aggregate([{聚合1},{聚合2},{聚合3},..])

$match---> $sort --- >$project
db.class2.aggregate
([{$match:{sex:'m'}},{$sort:{age:1}},{$project:{_id:0}}])


统计改班同学有哪几个重名
db.class5.aggregate
([{$group:{_id:'$name',num:{$sum:1}}},{$match:{num:{$gt:1}}}])

文件存储
    1，存储路径
        将文件放在本地路径（网络路径）下，然后数据库中存储
        该文件的查找路径
        优点：节省数据库空间
        缺点：当数据库或者文件位置发生变化时，文件即丢失
    2，将文件转换成二进制，存储文件本身
        数据库支持二进制格式，将文本文件转换为二进制格式，
        然后存入到数据库中
        优点：数据库和文件绑定，数据库在即文件在
        缺点：占用数据库空间大，存取效率低

mongodb存储文件本身
    1，如果是小文件，建议转换二进制直接插入
    2，如果是大文件，就建议使用GridFS方案存储  
    >16M的认为是大文件

GridFS方案解释
    1，在mongodb的一个数据库中，使用两个集合配合存储文件
    2，fs.files 用来存储文件的相关信息，为每一个文件创建
    一个文档 ，存储文件名，文件大小 ，存入时间。。。
    3，fs.chunks 用来分块存储文件的实际内容
                Binary data  类型数据

存储方法：
mongofiles -d   dbname   put  file
数据库不存在会自动创建数据库
数据库中会自动创建fs.files  fs.chunks两个集合

fs.files 文件结构
{ "_id" : ObjectId("5b7cdd09b29be8673f852031"), "filename" : "56.jpeg", "chunkSize" : 261120, "uploadDate" : ISODate("2018-08-22T03:48:25.922Z"), "md5" : "71851494239f38122d5bb161729d1ca3", "length" : 103559 }

fs.chunks
{ "_id" : ObjectId("5b7cdd096ea17883e5b22d8f"), "files_id" : ObjectId("5b7cdd09b29be8673f852031"), "n" : 0, "data" : BinData(0,"/9j/4AAQSkZJRgA ...  

同一个文件fs.files中的_id值等于fs.chunks中的files_id域的值

提取方法：
mongofiles -d dbname get file

GridFS   
优点：存储方便，提提供较好的命令支持和编程接口
缺点：存取效率低

mongo shell 中获取游标
    mongo shell 下支持JS代码，可以通过JS
    获取游标，进而获取数据操作结果
    比如：
    var cursor = db.class1.find()
    cursor.next()      获取下一条结果
    cursor.hasNext()   查看是否有下一个对象

通过python操作 MongoDB
pymongo 模块    第三方模块

安装：
sudo pip3 install pymongo

操作步骤：
    1，连接数据库，生成数据库连接对象
    conn = pymongo.MongoClient('localhost',27017)
    
    2,选择要操作的数据库，生成数据库对象
    db = conn.stu(stu：选择的数据库)  <====> db = conn['stu']

    3,获取集合对象
    myset = db.class0

    4,通过集合对象调用mongodb数据库操作函数
     增删改查，聚合，索引。。。。。

     5，关闭数据库连接
     conn.close()

插入文档