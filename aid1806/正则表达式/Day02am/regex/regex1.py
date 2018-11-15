import re 

#匹配内容返回迭代对象
# s = "2008年是个多事之秋,512地震,08奥运等"
# it = re.finditer(r'\d+',s)

# for i in it:
#     print(i.group())

# try:
#     obj = re.fullmatch(r'\w+','abcde#f123')
#     print(obj.group())
# except AttributeError as e:
#     print(e)

#匹配字符串开始位置
# obj = re.match('foo','foo,food on the table')
# print(obj.group())

#匹配第一处内容
obj = re.search('foo','Foo,food on the table')
print(obj.group())
