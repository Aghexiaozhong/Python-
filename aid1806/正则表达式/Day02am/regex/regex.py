import re 

#re调用findall

s = 'he   is   Tom'

# l = re.findall(r'(ab)cd(ef)',s)

# print(l)

#通过compile对象调用findall
# regex = re.compile(r'abcd')
# l = regex.findall(s,3,20)
# print(l)

#将目标字符串用正则匹配内容分割
# l = re.split(r'\s+',s)
# print(l)

#替换目标字符串
s = re.subn\
(r'\s+','##',"hello world  nihao  china")
print(s)



