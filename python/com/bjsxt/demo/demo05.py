file = open(r'F:\大数据数据搜集的网站.txt', 'r', encoding='utf-8')
file1 = open(r'E:\mydata.txt', 'w', encoding='utf-8')
# 次数使用的是readlines，注意s，复数形式
# 还有一个方法是readline，读取一行。
for line in file.readlines():
    file1.write(line)
    # file1.write("\n")

file.close()
file1.flush()
file1.close()