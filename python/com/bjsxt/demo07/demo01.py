from pymysql import *

# 建立到数据库的连接
conn = connect(host='localhost', user='root', password='123456')
# 获取游标
mycur = conn.cursor()
# 执行创建数据库的语句
rowNum = mycur.execute("create database pydb")

print("受影响的行数：", rowNum)

# 关闭游标
mycur.close()
# 关闭连接
conn.close()
