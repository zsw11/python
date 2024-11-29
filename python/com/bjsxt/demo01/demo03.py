class User:
    name = 'zhangsan'
    age = 25

# 构造方法
    def __init__(self):
        self.name = "lisi"
        self.age = 29

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method(self):
        return "hello world"


# 创建user对象
# user = User()
user = User('wangwu', 28)
print("User类属性：name = " + user.name)
print("User类方法：method()输出：" + user.method())
