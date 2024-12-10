from pymysql import *

# 建立到数据库的连接
conn = connect(host='192.168.1.164', user='root', password='govnet')
# 获取游标
mycur = conn.cursor()
# 执行创建数据库的语句
rowNum = mycur.execute("create database pydb")

print("受影响的行数：", rowNum)

# 关闭游标
mycur.close()
# 关闭连接
conn.close()
