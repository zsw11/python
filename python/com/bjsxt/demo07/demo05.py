from pymysql import *

conn = connect(host='localhost', user='root', password='123456', database='pydb')
mycur = conn.cursor()

# rowNum = mycur.execute("select * from tb_item where id=%s and price=%s", (536563, 29900000))
rowNum = mycur.execute("select * from tb_item where title=%s", ('阿尔卡特 (OT-979) 冰川白 联通3G手机',))

print("受影响的行数：", str(rowNum))

results = mycur.fetchall()

for result in results:
    print(result)
    print("id:", result[0])
    print("title:", result[1])
    print("sell_point:", result[2])
    print("price:", result[3])
    print("num:", result[4])
    print("barcode:", result[5])
    print("image:", result[6])
    print("cid:", result[7])
    print("status:", result[8])
    print("created:", result[9])
    print("updated:", result[10])

mycur.close()
conn.close()


