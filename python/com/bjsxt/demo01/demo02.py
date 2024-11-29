class User:
    name = 'zhangsan'
    age = 25

    def method(self):
        return "hello world"


# 创建user对象
user = User()
print("User类属性：name = " + user.name)
print("User类方法：method()输出：" + user.method())
