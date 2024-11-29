
class User:

    @classmethod
    def say_hello(cls):
        """
        注意参数中的cls和静态方法中的不需要cls这个区别
        :return:
        """
        # cls代表当前类
        print("类方法")
        # Class clazz = User.class
        print(cls.__class__)

    @staticmethod
    def say_my_hello():
        print("静态方法")


User.say_hello()
User.say_my_hello()

