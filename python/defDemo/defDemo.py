# def 函数名(参数列表):
#     函数体
#     [return [返回值]]
# 定义函数：返回 a 和 b 中的最大值
def max_ab(a, b):
    if type(a) == int and type(b) == int:
        return a if a >= b else b
    else:
        return '类型错误'

# 函数的调用
ab= max_ab(1, 2)
print(ab)
s = max_ab(5, "n")
print(s)

# 值传递 引用传递
# 值传递：适用于实参类型为不可变类型（字符串、数字、元组）；
# 引用传递：适用于实参类型为可变类型（列表，字典）。

# 值传递
def print_copy(a):
    a += a
    print("值传递，形参值为:", a)
b = "Hello"
print("b的值为:", b)
print_copy(b)
print("值传递，实参值为:", b)
# 引用传递
def print_copy(a):
    print("引用传递参值为:", a)
    a += a

b = [1, 2, 3, 4]
print("b的值为:", b)
print_copy(b)
print("引用传递为:", b)

# 参数的类别
# 位置参数 ： 实参和形参位置，数量必须一致
# 关键字参数 : 跟进形参名称来确定参数
def area_trapezoid(a, b, h):
    s = (a + b) * h / 2
    print(s)
area_trapezoid(a=1, h=2, b=6)

# 位置参数，可变参数，可变关键字参数
def func(normal_arg, *args, **kwargs):
    print(f"Normal arg: {normal_arg}")  # 0
    for arg in args:
        print(f"Another positional arg: {arg}") # 1 2 3
    for key, value in kwargs.items():
        print(f"Keyword argument {key} is {value}") # 4 5 6

func(0, 1, 2, 3, a=4, b=5, c=6)

def print_obj1(**kwargs):
    print(kwargs)
    print(kwargs.items())
print_obj1(**{"hello": "a", "world": "b"})

# 解包位置参数 (*)
# 你可以将一个可迭代对象（如列表或元组）解包并传递给函数的多个位置参数。
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # 解包列表
print(result)  # 输出: 6

# *args：接受可变数量的位置参数，传入后会成为元组。
# **kwargs：接受可变数量的关键字参数，传入后会成为字典。
# *：用于强制要求后面的参数必须是关键字参数。
# 解包操作：你可以使用 * 解包可迭代对象传递位置参数，使用 ** 解包字典传递关键字参数。


# globals 函数可以返回一个包含全局范围内所有变量的字典
print(globals())
# locals 函数可以返回一个包含当前作用域内所有变量的字典 用在方法体内

# 作业
# 写一个打印一条横线的函数； 写一个函数，可以通过输入的参数，打印出自定义行数的横线（提示：调用前面的函数）；
# 第一问
def print_xian():
    return "-" * 20
# 第二问
def print_number(number):
    i = 1
    while i <= number:
        print(print_xian())
        i += 1
print_number(3)

def sum(a,b,c):
    return a+b+c
print(sum(1,2,3))

def avg(a,b,c):
    return sum(a,b,c,)/3
print(avg(1,2,3))
