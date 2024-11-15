import random  # 引入随机数

x = random.randint(0, 2)  # 随机生成 0、1、2 中的一个数字，赋值给变量 x
print(x)

x = random.randint(0, 2)
y = int(input("请输入剪刀石头布相对应的数字，其中剪刀0石头1布2"))
if y not in [0, 2]:
    print("请输入0，1，2之间的数字")
if y == 0:
    print("你输入的是剪刀")

import python.hanshu
python.hanshu.add(1,2)  #引入python包下 hanshu.py里的add方法
