from pymysql import *

# 获取JDBC连接
conn = connect(host='localhost', user='root', password='123456')
# 获取游标
mycur = conn.cursor()
# 让游标执行操作
mycur.execute("create database pydb")
# 关闭游标
mycur.close()
# 关闭连接
conn.close()

