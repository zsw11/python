class User:

    def say_hello(self):
        print("你好，我似乎" + self.__my_name())

    # 私有方法
    def __my_name(self):
        return "狗剩子"

user = User();
# user.say_hello()
user.__my_name()