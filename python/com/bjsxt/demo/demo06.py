import os

mydir = r'E:\Anaconda3'
print(os.path.isdir(mydir))
# 判断是否是一个目录
if os.path.isdir(mydir):
    print("目录：", mydir)

# 列出指定目录下的内容
files = os.listdir(mydir)

for myfile in files:
    if os.path.isdir(mydir + "\\" + myfile):
        print("目录：", myfile)
    else:
        print("文件：", myfile)
