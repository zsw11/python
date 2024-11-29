class MySingleton:

    __myobj = None

    def __init__(self, name, age):

        if not hasattr(self, 'name'):
            self.name = name
            self.age = age
        print("调用了构造方法")

    def __new__(cls, *args, **kwargs):
        if not cls.__myobj:
            cls.__myobj = super(MySingleton, cls).__new__(cls)
        return cls.__myobj


mysingleton1 = MySingleton('zhangsan', 25)
mysingleton2 = MySingleton('lisi', 30)

print(mysingleton1)
print(mysingleton2)
print(id(mysingleton1))
print(id(mysingleton2))
print(mysingleton1 == mysingleton2)
print(mysingleton1.name, str(mysingleton1.age))
print(mysingleton2.name, str(mysingleton2.age))
