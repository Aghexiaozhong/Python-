#regex2.py

import re

pattern = r'(?P<dog>ab)cd(?P<cat>ef)'
regex = re.compile(pattern)

#获取match 对象
obj = regex.search('abcdefghijklmn',0,8)

#match对象
print(obj.pos) #目标字符串的起始位置
print(obj.endpos) #目标字符串的结束位置

print(obj.re)  #正则表达式
print(obj.string) #目标字符串

print(obj.lastgroup)   #最后一组的名称
print(obj.lastindex) #最后一组是第几组

print('=======================')

print(obj.span())  #匹配内容的起止位置
print(obj.start())  #匹配到内容开始位置
print(obj.end())   #匹配到内容的结束位置
print(obj.groupdict())
print(obj.group())
print(obj.group(2))
print(obj.groups())


















