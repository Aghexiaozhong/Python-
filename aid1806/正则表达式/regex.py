#regex.py

import re

pattern = r'([A-Z])(\S+)'

#re 调用
# l = re.findall(pattern,'Hello World')
# print(l)

#compile 调用
# regex = re.compile(pattern)

# l = regex.findall('Hello World',3,20)
# print(l)

l = re.split(r'\W+','Hello$$W!@orld')
print(l)

s = re.subn(r'\S+','**','this is a boy')
print(s)








