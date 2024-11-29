from pymysql import *

# 获取连接
conn = connect(host='localhost', user='root', password='123456', database='pydb')
# 打开游标
mycur = conn.cursor()
try:
    # 开启事务
    conn.begin()

    rowNum = mycur.execute("""
    insert into tb_item values(1234567, "new2 - 阿尔卡特 (OT-927) 炭黑 联通3G手机 双卡双待", "清仓！仅北京，武汉仓有货！", 29900000, 99999, null, "http://image.taotao.com/jd/4ef8861cf6854de9889f3db9b24dc371.jpg", 560, 1, "2015-03-08 21:33:18","2015-04-11 20:38:38")
    """)

    # 提交事务
    conn.commit()

except Error as e:
    conn.rollback()
    print(e)
finally:
    # 关闭游标
    mycur.close()
    # 关闭连接
    conn.close()

