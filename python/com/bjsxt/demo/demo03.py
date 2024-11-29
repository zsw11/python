"""
文件以写模式打开，以utf-8编码来处理
"""
file = open(r'E:\mydata.txt', 'w', encoding='utf-8')

for i in range(10):
    # file的write方法调用，向打开的文件写内容
    file.write('1234567890\n')
# 关闭文件流
file.close()
