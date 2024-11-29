
class Person:
    # 私有属性
    __name = 'lisi'
    age = ''

    def __init__(self):
        self.__name = '张三'
        self.age = 25

    def say_hello(self):
        print("你好，我是" + self.__name + "，我今年" + str(self.age) + "岁了")

# person = Person()
# # 不能访问
# # print(person.__name)
# person.say_hello()


class Programmer(Person):

    def __init__(self):
        pass

    def say_hello(self):
        print("你好，我后if的撒范德萨分")
        super(Programmer, self).say_hello()

programmer = Programmer()
programmer.say_hello()

