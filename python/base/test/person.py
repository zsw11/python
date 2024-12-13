class Person:

    # 类属性  Python 的类属性相当于 Java 的 static 属性
    school = "中加枫华国际学校"
    tuition = 100000
    count = 0

    # 实例属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count = Person.count+1

    # 静态实例
    @staticmethod
    def addNum(a,b):
      print("{0}+{1}={2}".format(a,b,a+b))
      return a+b

    # 实例方法
    def get_score(self):
        print("姓名：{0}；年龄：{1}".format(self.name,self.age))

stu1 = Person("sue", 22)
print(stu1.age)
stu1.get_score()
Person.addNum(1,2)