class MySingleton:
    __instance = None
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("调用了——init 方法")
    def __new__(cls, *args, **kwargs):
        # 如果类属性__instance 不为none ,则直接返回它的值
        if cls.__instance:
            return cls.__instance
        #如果雷属性__是none,
        cls.__instance = super(MySingleton,cls).__new__(cls)
        return cls.__instance

mysingleton1 = MySingleton(name='zhangsan', age=25)
mysingleton2 = MySingleton(name='lisi', age=35)
print(mysingleton1)
print(mysingleton2)
print(id(mysingleton1))
print(id(mysingleton2))
print(mysingleton1 == mysingleton2)
# mysingleton1 的值被覆盖掉了，因为__init__方法调用了两次
print(mysingleton1.name, str(mysingleton1.age))
print(mysingleton2.name, str(mysingleton2.age))


