pak = {
  "name":"sue",
  "age":22,
  "hobby":"frisbee"
}
a,b,c = pak
print(a, b, c)  # name age hobby
a,b,c = pak.items()
print(a, b, c)  # ('name', 'sue') ('age', 22) ('hobby', 'frisbee')
a,b,c = pak.values()
print(a, b, c)  # sue 22 frisbee

addDic1 = {
  "name":"jyc",
  "age":21,
  "gender":"famale",
  "job":"student"
}
addDic1["age"]=22;
addDic1["address"] = "上海市xxx"
print(
    addDic1
)  # {'name': 'jyc', 'age': 22, 'gender': 'famale', 'job': 'student', 'address': '上海市xxx'}
addDic2 = {
  "name":"zsw",
  "sex": "男"
}
# 使用update()添加将新字典中所有的键值对全部添加到旧字典对象上。如果key重复，则覆盖。
addDic1.update(addDic2)
print(addDic1)