"""
以只读模式打开文件，以utf-8字符集解码
"""
file = open(r'E:\mydata.txt', 'r', encoding='utf-8')
# 定位到索引是5的字节
file.seek(5)
print(file.readline())

file.seek(100)
print(file.readline())
# 打印当前指向的位置
print(file.tell())
# 关闭文件流
file.close()
