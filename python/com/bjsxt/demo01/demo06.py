class User:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method(self):
        print("我是：" + self.name + "，我的年龄是：" + str(self.age))

    @staticmethod
    def say_my_hello():
        print("静态方法")
        print("我是：" + User.name + "，我的年龄是：" + str(User.age))

User.say_my_hello()
user = User('李四', 33)
user.method()

