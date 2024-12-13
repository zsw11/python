import re
# 基本的正则表达式符号
# .：匹配任何单个字符（除换行符 \n 外）。
# ^：匹配字符串的开头。
# $：匹配字符串的结尾。
# *：匹配前面的子表达式零次或多次。
# +：匹配前面的子表达式一次或多次。
# ?：匹配前面的子表达式零次或一次。
# {n}：匹配前面的子表达式恰好 n 次。
# {n,}：匹配前面的子表达式至少 n 次。
# {n,m}：匹配前面的子表达式至少 n 次，最多 m 次。
# []：定义字符集，匹配其中的任意一个字符。
# |：表示“或”操作，匹配左边或右边的表达式。
# ()：分组，表示子表达式，捕获匹配的文本。

# 匹配任意字符
pattern = r"abc.def"
match = re.match(pattern, "abcXdef")
print(match.group())

pattern = r"^abc"  # 匹配以 'abc' 开头的字符串
result = re.match(pattern, "abcdef")
if result:
    print("匹配成功:", result.group())
else:
    print("匹配失败")


pattern = r"abc"  # 匹配任意位置的 'abc'
result = re.search(pattern, "123abc456")
if result:
    print("找到匹配:", result.group())  # 输出 'abc'
else:
    print("未找到匹配")

pattern = r"\d+"  # 匹配一个或多个数字
result = re.findall(pattern, "There are 123 apples and 456 oranges")
print(result)  # 输出 ['123', '456']

pattern = r"\d+"  # 匹配数字
replaced_string = re.sub(pattern, "#", "There are 123 apples and 456 oranges")
print(replaced_string)  # 输出 'There are # apples and # oranges'

pattern = r"\s+"  # 匹配一个或多个空白字符
result = re.split(pattern, "This is a test string")
print(result)  # 输出 ['This', 'is', 'a', 'test', 'string']