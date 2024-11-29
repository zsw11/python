class MySingleton:

    __instance = None

    def __init__(self, name, age):
        # 如果对象没有'name‘属性，就赋值，否则不赋值
        if not hasattr(self, 'name'):
            self.name = name
            self.age = age
        print("调用了__init方法__")

    def __new__(cls, *args, **kwargs):
        # 如果类属性__instance不为None，则直接返回它的值
        if cls.__instance:
            return cls.__instance

        # 如果类属性__instance是None
        # 创建对象，并返回
        cls.__instance = super(MySingleton, cls).__new__(cls)
        return cls.__instance


mysingleton1 = MySingleton(name='zhangsan', age=25)
mysingleton2 = MySingleton(name='lisi', age=35)
print(mysingleton1)
print(mysingleton2)
print(id(mysingleton1))
print(id(mysingleton2))
print(mysingleton1 == mysingleton2)
# mysingleton1的值被覆盖掉了，因为__init__方法调用了两次
print(mysingleton1.name, str(mysingleton1.age))
print(mysingleton2.name, str(mysingleton2.age))



