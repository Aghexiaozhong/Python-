#regex2.py


import re

# obj = re.finditer(r'\d+','2018事情有点多，512,08奥运')

# #迭代出的内容是match对象
# for i in obj:
#     # print(dir(i))
#     print(i.group())

# try:
#     obj = re.fullmatch(r'\w+','abc#123')
#     print(obj.group())
# except AttributeError as e:
#     print(e)

# obj = re.match(r'h','hds,af,s')
# print(obj.group())


obj = re.search(r'hds','mtd,hds,af,s')
print(obj.group())


