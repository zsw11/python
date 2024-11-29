
class User:
    def __new__(cls, *args, **kwargs):
        return super(User, cls).__new__(cls)
        # 如果该方法没有返回对象，None，则init方法不会调用
        # 创建对象
        # return None

    def __init__(self):
        # 构造方法
        # 对对象进行初始化
        self.name = "zhangsan"
        self.age = 25
        self.address = "大兴"

    def say_hello(self):
        print("你好，我是" + self.name + ", 我今年" + str(self.age) + "岁了，我住" + self.address)

    def __del__(self):
        print("析构方法调用了")

user = User()
print(user)
print(id(user))
# user.say_hello()