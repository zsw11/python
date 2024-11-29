class Person:
    name = ''

    def __init__(self, name):
        self.name = name
        print(self)

    def work(self):
        print("我是：" + self.name + "，我的工作就是干活")


class Programmer(Person):

    def __init__(self):
        # 调用父类构造器
        Person.__init__(self, '张三')

    def work(self):
        print("我是：" + self.name + "，我的工作是写代码和bug")
        # 调用父类被覆盖的方法
        super(Programmer, self).work()


programmer = Programmer()
programmer.work()
