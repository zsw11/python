# type()查看变量类型
name1 = "Li Ming"
print(type(name1))

name2 = "123456"
print(type(name2))

ame1 = 123456
print(type(name1))

name2 = 1.23456
print(type(name2))

print(type(5 > 4))
print(type(4 > 5))

print(type(1+4j))
print(type(complex(4, 5)))

#隐式类型装换
print(type(1+0.1))

#显示类型转换
print(int())
print(int(3.6))

print(float(-3.0))          # 小数
print(float("3"))           # 字符串

print(str(1))
print(str(3.6))

a = 60
b = 13
print(a & b)
print(bin(a&b)) # 0b1100  十六进制
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(a >> 2)

a = 10
b = 20
if a and b:   # and or not
    print("- 变量 a 和 b 都为 true")
else:
    print("- 变量 a 和 b 有一个不为 true")

# in not in
a = 1
b = 2
list = [2, 3, 4, 5]

if a in list:
    print("a在列表中")
else:
    print("a不在列表中")

#is not is 判断的两个对象的存储单元是否相同的一种运算符号
# is 与 == 的区别
# is 用于判断两个变量引用对象是否为同一个，== 用于判断引用变量的值是否相等。
a = 1
b = 2
c = a
print(a is b)
print(a is c)
print(a == c)
print(a is not b)
print(a is not c)

# 行与缩进
if  True:
    print("answer")
    print("true")
else:
    print("false")

score = 77
if 90 < score <= 100:
    print("本次考试等级为 A")
elif 80 < score <= 90:
    print("本次考试等级为 B")
elif 70 < score <= 80:
    print("本次考试等级为 C")
elif 60 < score <= 70:
    print("本次考试等级为 D")
else:                          # 这一行也可以写成：elif 0 <= score <= 60:
    print("本次考试等级为 E")

a = int(input("请输入考试分数："))
assert 0 <= a <= 100                           # 断言数学考试分数是否位于正常范围内
print("你的考试成绩为：", a)                   # 只有当考试成绩位于 [0,100]范围内，程序才会继续执行
assert a > b
