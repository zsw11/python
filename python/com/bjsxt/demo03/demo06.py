import threading


class MySingleton:

    __instance = None
    __instence_lock = threading.Lock()

    def __init__(self, name, age):
        # 如果对象没有'name‘属性，就赋值，否则不赋值
        if not hasattr(self, 'name'):
            self.name = name
            self.age = age
        print("调用了__init方法__")

    def __new__(cls, *args, **kwargs):
        # 如果类属性__instance为None
        if not cls.__instance:
            # 代码块加锁，线程排队后再次判断是否为None
            with MySingleton.__instence_lock:
                if not cls.__instance:
                    # 如果类属性__instance是None，创建对象
                    cls.__instance = object.__new__(cls)
        return cls.__instance

    def __str__(self):
        # 类似java的toString
        return str(id(self)) + " [name] = " + self.name + " [age] = " + str(self.age)


# 类似java的Thread中的run方法
def task(name, age):
    obj = MySingleton(name=name, age=age)
    print(obj)


for i in range(50):
    thread = threading.Thread(target=task, args=['name' + str(i), 30 + i])
    thread.start()

