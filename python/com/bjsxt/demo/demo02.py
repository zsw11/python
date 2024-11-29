"""
第一个参数表示读取的文件路径，第二个参数表示只读模式，第三个参数表示编码字符集
"""
file = open(r'F:\大数据数据搜集的网站.txt', 'r', encoding='utf-8')

for line in file.readlines():
    print(line, end='')
# 关闭文件流
file.close()
