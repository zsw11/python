import os

print("当前目录：", os.getcwd())
# os.chdir("..")
# print("当前目录：", os.getcwd())
exists = os.path.exists("path") # 相对于当前路径
print(exists)

# t = open("hello.txt", "w") # 打开文件，如果文件不存在则创建，文件存在会覆盖源文件的内容
# name = t.name
# t.write("Welcome to Wuhan!")
# t.close()

# read() readline() readLines()
# hello.txt 中包含的内容为：Welcome to Wuhan!
# 读取所有内容
file_obj = open("hello.txt", "r", encoding="utf-8")
print(file_obj.read())
file_obj.close()
# 读取文件开头的前10个字符
file_obj = open("hello.txt", "r", encoding="utf-8")
print(file_obj.read(10))
file_obj.close()
# 读取文件开头的前20个字符
file_obj = open("hello.txt", "r", encoding="utf-8")
print(file_obj.read(20))
file_obj.close()

# 读取所有的内容
text_io = open("hello.txt", "r", encoding="utf-8")
print(text_io.read())
text_io.close()
open1 = open("hello.txt", "r", encoding="utf-8")
print(open1.readline())
open1.close()

open2 = open("hello.txt", "r", encoding="utf-8")
print(open2.readline(10)) # 读取10个字节
open2.close()

# 读取文件所有行的字符,返回是一个字符串列表
file_obj = open("hello.txt", "r", encoding="utf-8")
print(file_obj.readlines())
file_obj.close()

#
t = open("hello.txt", "r+", encoding="utf-8")
t.write("替换,写入文本")
print(t.read()) # 这里读取不到里面替换写入的内容，需要再次读取文件，才能看到最新写入的内容
t.close()

# tell函数用于判断文件指针当前所处的位置
b = open("hello.txt", "r+", encoding="utf-8")
print(b.tell())
print(b.read(3))   # 替换,
print(b.tell())


a = open("hello.txt", "rb")
print(a.tell())
print(a.read(3))   # b'\xe6\x9b\xbf'   二进制读取
print(a.tell())

# seek 函数用于将文件指针移动至指定位置,这里是指针移动到2位置，不是从某个位置移动2个
seek = b.seek(2)
print(seek)
print(b.tell())

# with 打开文件字段关闭， 相当于java try（）
# with expression [as variable]:
    # statement

with open("hello.txt", "r", encoding="UTF-8") as file_obj:
    read = file_obj.read(5)
    print(read)

# a 追加写入，
with open("hello.txt", "a+", encoding="utf-8") as file_obj:
    print(file_obj.tell())    # a 追加模式，文件指针会移到文件末尾
    # print(file_obj.read())  # 指针在文件莫问，读取数据失败
    file_obj.seek(0)   # 移动文件到头
    print(file_obj.read()) # 读取文件
    file_obj.write("**")

# os 模块函数

# 如果给出的路径包含目录和文件名，则返回目录和文件名；如果给出的路径只含目录名，则返回目录和空文件名。
a = os.path.split("C:\\Users\\****\\Desktop\\books\\book.txt")
print(a)
b = os.path.split("C:\\Users\\****\\Desktop\\books\\")
print(b)
