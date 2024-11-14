# 特性	    Java    Python
# 类型系统	静态类型	动态类型
# 函数定义	需要显式声明类型	不需要显式声明类型
# 类和继承	单继承，类成员需声明访问控制符	多继承，类成员默认公开
# 异常处理	try-catch，显式声明异常	try-except，无需显式声明异常
# 控制结构	使用大括号 {}，语句以分号结束	使用缩进来表示代码块
# 模块与包	使用 import，通常通过 JAR 文件	使用 import，通过模块和包管理
# 内存管理与GC	垃圾回收	垃圾回收（引用计数 + 循环GC）
# 性能	较高，编译型语言	较低，解释型语言
# 跨平台	通过 JVM 跨平台	通过解释器支持跨平台


print("你好，python")
a=10
print(a)
import keyword
print(keyword.kwlist)
print(4)
print(5+3)
print("My lucky number is", " 6 ")
a = 3
print("输出的数字为：", a)

# 格式化输出（%）
number= 6
print("my lucky number is %d" % number)
print("my name is %s" % "li ming")

name = 'jack'
print("her name is %s" % name)
print("My name is %s"" and my lucky colour is %s" % ("Li Ming", "blue"))

#格式化输出（format 函数）
str = "{} is a beautiful {}！".format("Beijing","city")
print(str)

str1 = "{0} is a beautiful {1}!".format("Beijing", "city")
print(str1)
str2 = "{1} is a beautiful {2}!".format("Tianjin","Beijing", "city")
print(str2)

str1 = "{name1} is a beautiful {name2}!".format(name1="Beijing", name2="City")
print(str1)

class Names:
    Name1 = "Beijing"
    Name2 = "city"
str1 = "{names.Name1} is a beautiful {names.Name2}!".format(names=Names)
print(str1)

str1 = "The first letter of '{word}' is '{word[0]}'.".format(word="hello")
print(str1)

str1 = "π is {:.2f}.".format(3.1415926)  #保留两位小数
print(str1)

str1 = "{:,}".format(100000000)
print(str1) #给数字加千位符

s1 = "{:b}".format(8)     # 将数字8转换为二进制
print(s1)
s2 = "{:o}".format(8)     # 将数字8转换为八进制
print(s2)
s3 = "{:x}".format(12)    # 将数字12转换为十六进制
print(s3)

s = "{:4}b".format('a')
print(s)
# 如果指定的长度小于参数的长度，按照原参数匹配
s1 = "{:2}World".format('Hello')
print(s1)

s = "{:*^10}".format('Hello')
print(s)
s = "{:-^20}".format('123456')
print(s)

list = ["Beijing", "city"]
str1 = "{} is a beautiful {}!".format(*list)
str2 = "{1} is a beautiful {0}!".format(*list)
print(str1)
print(str2)

dict = {"name1": "Beijing", "name2": "city"}
str1 = "{name1} is a beautiful {name2}!".format(**dict)
print(str1)

a = 1
b = 2
c = 3
print(f"b={b}, c={c}, a={a}")
# 上面的代码等效于：
print("b={}, c={}, a={}".format(2, 1, 3))

print("a")
print("b", end="") # 不换行输出
print("c")

print("123456789---------")
print("123456789\n---------") #转义字符\n, 换行

# for 循环实现换行输出
a = "hello"
for i in a:
    print(i)
# while 循环实现换行输出
j = 0
while j <= 4:
    print(a[j])
    j += 1

print("a", end="\t")
print(end="")
print("b")  #水平制表符输出，  a          b

print("123456789\t---------")  # 123456789	---------

#更换间隔字符输出
print("www", "baidu", "com") #wwwbaiducom
print("www", "baidu", "com", sep=".") #www.baidu.com
print("www", "baidu", "com", sep="/") #www/baidu/com

print(complex(1, 4))