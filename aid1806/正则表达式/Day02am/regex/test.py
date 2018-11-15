import re 

f = open('mongo.txt')

l = [] 

# pattern = r'\b[A-Z][\._0-9a-zA-Z]*'

# for line in f:
#     l += re.findall(pattern,line)

# print(l)

pattern = r'-?\d+\.?/?\d*%?'

for line in f:
    l += re.findall(pattern,line)

print(l)