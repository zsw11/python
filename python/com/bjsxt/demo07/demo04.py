from pymysql import *

conn = connect(host='localhost', user='root', password='123456', database='pydb')
mycur = conn.cursor()
try:
    conn.begin()
    mycur.execute("delete from tb_item where id=%s", (536563, ))
    conn.commit()
except Error as e:
    conn.rollback()
    print(e)
finally:
    mycur.close()
    conn.close()

