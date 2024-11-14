print("hello")
print('hello')
print('''hello''')

# \ 转义
print('What\'s your name ?')
print("Do you know \"Python\" ?")

str = "abcdefghijklmn"
print(str.find("abc"))
print(str.find("lmn"))
print(str.find("n", 5, 13)) # 查找字符串
print(str.index("abc"))  # 字符串下标
print(str.index('m', 5, 13))

str = "abcabcabcabc"
print(str.count("abc", 0, 3)) # 统计字符串出现次数
print(str.count("a"))

str1 = "Welcome to Beijing ! Beijing is a beautiful city ."
print(str1.replace("Beijing", "Wuhan"))
str2 = "Welcome to Beijing ! Beijing is a beautiful city . I love Beijing . Do you love Beijing ?"
print(str2.replace("Beijing", "Wuhan", 2))  #字符串替换，替换前2个

str1 = "    123123123\n\t\r"
print(str1.strip())
str2 = "******123******"
print(str2.strip("*"))   #删除字符串前面或者后面的字符

str3 = "123123123***123***123123123"
print(str3.lstrip("123456"))  # 删除字符串左侧的字符序列  ***123***123123123

str3 = "123123123***123***123123123"
print(str3.rstrip("123456")) # 删除字符串右侧的字符序列  123123123***123***

str1 = "Beijing!"
str2 = "北京欢迎你!"
print(len(str1))
print(len(str2))
print(len("Beijing!"))
print(len("北京欢迎你!")) # 字符串长度

str1 = "人生苦短，我用Python"
print(len(str1.encode()))
print(len(str1.encode("gbk"))) # 不同字符编码 所占的字节数

str1 = "https://github.com/"
str2 = "https://www.bilibili.com/"
print(str1.ljust(30))
print(str2.ljust(30))
print(str1.ljust(10))
print(str2.ljust(10))
print(str1.ljust(30, "*"))
print(str2.ljust(30, "*")) #字符串左对齐

str1 = "https://github.com/"
str2 = "https://www.bilibili.com/"
print(str1.rjust(30))
print(str2.rjust(30))
print(str1.rjust(10))
print(str2.rjust(10))
print(str1.rjust(30, "*"))
print(str2.rjust(30, "*")) #字符串右对齐

str1 = "https://github.com/"
str2 = "https://www.bilibili.com/"
print(str1.center(30))
print(str2.center(30))
print(str1.center(10))
print(str2.center(10))
print(str1.center(30, "*"))
print(str2.center(30, "*")) # 原字符串居中对齐

a = "shijiazhuang"
print(a[0])
print(a[-1])
print(a[0:10])
print(a[0:10:2]) #从0 开始，截取到 第10位，步长为2（每2位取一个字符）

print("h" "a" "p" "p" "y") #空格自动拼接
print("h" + "a" + "p" + "p" + "y") # 字符串 加号“+”拼接
print("happy"*5) # 乘号“*”重复拼接

str = "www.nihao.com.cn"  # 字符串分割
print(str.split("."))
print(str.split("c"))
print(str.split(".", 2))
print(str.split(".", 2)[2])
a, b, c, d = str.split(".")
print(a)
print(b)
print(c)
print(d)

sequence = "H", "a", "p", "p", "y"
print("".join(sequence)) # 字符串的合并
print(" ".join(sequence))
print("-".join(sequence))

str = '我要成为python大佬'
encode = str.encode("UTF-8")  # UTF-8 是一种字符编码方式，它将每个字符映射到一个二进制数字序列。
print("utf-8编码：",encode)
decode = encode.decode("UTF-8")
print("utf-8解码：", decode)

# 列表 同一个列表中元素的类型也可以不同
list1 = [1, 2, 3, 4]
list2 = ["1", "2", "3", "4"]
list3 = ["a", "b", 1, 2]
list4 = ["www.baidu.com", 6, [1, 2, 3], 6.0]
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))

# 将其他类型转换成list类型
list1 = list("Beijjing")
print(type(list1))
print(list1)

tuple1 = ("a", "b", "c", "d")
list1 = list(tuple1)
print(type(list1))
print(list1)

# 将字典转换成列表
dict1 = {"a": 1, "b": 2, "c": 3}
list1 = list(dict1)
print(type(list1))
print(list1)

a = ["h", "a", "p", "p", "y"]
b = ["n", "e", "w"]
c = ["y", "e", "a", "r"]
d = a + b + c
print(d)

list1 = [4, 5, 3, 1, 2]
print(max(list1))
print(min(list1))
print(list1*2)
print(len(list1))

# 列表的遍历
listname = ["zsw","zsere",1,3.2]
for item in listname:
    print(item)
for i in range(len(listname)):
    print(listname[i])
for i_value in enumerate(listname):  # i为索引 value为索引对应的值
    print(i_value)
for i, value in enumerate(listname):
    print(i, value)

list1 = ["a", "b", "c"]
del list1[0]
print(list1)
list1.append("z")
list1.insert(2,"2")    #插入元素
print(list1)
del list1[0:1]
list1.remove("c")

list1.clear()  # 清空列表

list1 = [2, 36, 2, 7, "aa", "bb"]
list1[2] = 66    # 修改挪个元素
print(list1)
list1[5] = "ee"
print(list1)

list1 = ["a", 1, "b", 2, "c", 3]
list1[1:4] = [4, "d", 5]   #修改一些元素，顾头不顾尾（包含下标1，不含下标4）
print(list1)

l = sorted(list2, reverse=True)
print(l)
list2.sort(reverse=True)

def print_info(name, **kwargs):   # *args 和 **kwargs 是用来处理可变数量的参数的特殊语法
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 调用函数时传入多个关键字参数
print_info("Alice", age=25, city="New York")

