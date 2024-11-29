class User:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method(self):
        print("我是：" + self.name + "，我的年龄是：" + str(self.age))


user = User('李四', 33)
user.method()

