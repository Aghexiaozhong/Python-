import re 

s = '''hello world
nihao Beijing
'''

# pattern = r"Hello"

# l = re.findall(pattern,s,re.I)
# print(l)

# obj = re.search(r'.+',s,re.S)
# print(obj.group())

# regex = re.compile(r'^nihao',re.M)
# l = regex.findall(s)
# print(l)

#(?P<dog>H\w+)\s+(world)
pattern = '''(?P<dog>H\w+)  #dog组
\s+ #任意多个空字符
(world)  #匹配world
'''

obj = re.match(pattern,'hello  world',re.X|re.I)
print(obj.group())