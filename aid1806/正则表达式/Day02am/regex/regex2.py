import re 

regex = re.compile(r"(?P<dog>cd)ef(?P<pig>gh)")

match_obj = regex.search("abcdefghijklmn")

# pos 目标字符串开始位置
print(match_obj.pos)
# endpos 目标字符串结束位置
print(match_obj.endpos)

# re 正则表达式
print(match_obj.re)
# string 目标字符串
print(match_obj.string)

# lastgroup  最后一组名称
print(match_obj.lastgroup)
# lastindex  最后一组是第几组
print(match_obj.lastindex)
print("**************************************")

print(match_obj.start()) # 匹配到的起始位置
print(match_obj.end())  #匹配到的结束位置
print(match_obj.span()) #匹配到的起止位置

print(match_obj.group())  #正则表达式匹配内容
print(match_obj.group(1)) #第一组匹配到的内容


print(match_obj.groups())
print(match_obj.groupdict())