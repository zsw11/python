# 元组 使用 () 直接创建元组 是一个有序且不可更改的集合，允许重复，元素的类型可以不同
a1 = (1, 1.1, "a", [1, "b", 3], ("h", "a", 2))
a1 = {1, 1.1, "a", (1, "b", 3), ("h", "a", 2)} # 集合
print(type(a1))

# tuple tuple() 函数可以将其他可迭代对象（如列表、字符串、集合等）转换为元组
tuple1 = tuple("hello")  # 字符串
tuple2 = tuple(["h", "e", "l", "l", "o"])  # 列表 == java list
tuple3 = tuple({1: "h", 2: "e", 3: "l", 4: "l", 5: "o"})  # 字典
tuple4 = (1, 2, 3)  # 元组
# tuple4 = tuple("hello",["h", "e", "l", "l", "o"])  不可以，tuple() 函数只接受 一个 可迭代对象作为参数，而你传入了 两个 参数（"hello" 和 ["h", "e", "l", "l", "o"]）
print(tuple4)

tuple1 = ("a", "b", "c", 1, "d")
print(tuple1[0])
print(tuple1[-5])
print(tuple1[0:4])
print(tuple1[0:5])
print(tuple1[0:5:2])  # 步长 2

# 元组不可修改，只能创建新的元祖去替换
f_ = ("b", "a")
f_ = ("1", "2.5", "f")
zsw_ = ("zsw", 1)
tuple5 = f_ + zsw_
print(tuple5)
print("b" in f_)
del tuple5

# 元组的遍历
f___ = ("a", "f", 2, 2.5)
for i in f___:
    print(i, end="\t")
# print(max(f___))

# 字典
# 无序的、可变的序列，它的元素以“键值对（key-value）
name_zsw_ = {"年龄": 18, "name": "zsw"}
print(type(name_zsw_))

# 通过 fromkeys 函数创建字典, 第一个参数字段所有的key, value 默认为空
list1 = ["语文", "数学", "英语"]
dict1 = dict.fromkeys(list1)
print(dict1)
dict2 = dict.fromkeys(list1, 90)
print(dict2)

# 通过dict函数创建
three_ = [('two', 2), ("one", 1), ('three', 3)]
print(dict(three_))

# 通过应用 dict 函数和 zip 函数，可将两个列表、元组、集合、字符串，甚至还可以将 range 区间转换为对应的字典，语法格式为：dictname = dict(zip(keys, values) )
keys1 = ["two", "one", "three"]
values1 = (2, 1, 3)
values2 = range(0, 3)
dict1 = dict(zip(keys1, values1))
dict2 = dict(zip(keys1, values2))
print(dict1)
print("11--", dict2)

dict1 = {'语文': 85, '数学': 96, '英语': 92}
dict1["物理"] = 86
print(dict1)
print(dict2.keys())

dict__get = dict2.get("英语")
if dict__get is None:
    print("键 '英语'不存在")
dict2.setdefault("英语")
print(dict2.get("英语"))
del dict1["数学"]

# copy 深浅拷贝 copy.deepcopy(dict1)
# 浅拷贝：使用 dict.copy()，仅拷贝字典的外部结构，内部的嵌套对象仍然共享。
# 深拷贝：使用 copy.deepcopy()，递归地拷贝所有嵌套对象，确保所有对象都被独立复制。
a = {'one': 100, 'two': 200, 'three': [100, 200, 300]}
b = a.copy()
a['four'] = 100
print(a)
print(b)
a['three'].remove(100)
print(a)
print(b)

# 字典的更新 update
dict1 = {'one': 100, 'two': 200, 'three': [100, 200, 300]}
dict2 = {'one': 100, 'two': 300, 'four': 400}
dict1.update(dict2)
print(dict1)

# 字典的函数 len() str() max() min()

# 集合{} 等于 java set
set1 = {4, 5, 6}
set2 = {6, 7, 8}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 5]

a = range(0, 101)
# 使用 break 跳出当前循环体之后，该循环后的 else 代码块也不会被执行
sum_i = 0
for i in a:
    if i == 5:
        break
        sum_i += i
        i += 1
    else:
        print(sum_i)

# pass 空语句，pass 不做任何事情，表示一个占位符，一般用作占位语句
age = int( input("请输入你的年龄：") )
if age < 12 :
    print("婴幼儿")
elif 12 <= age < 18:
    print("青少年")
elif 18 <= age < 30:
    print("成年人")
elif 30 <= age < 50:
    pass
else:
    print("老年人")
