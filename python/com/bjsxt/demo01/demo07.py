class Person:
    name = ''
    age = 0
    # 私有属性，外部无法访问，只能在类内部访问
    __weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def say_hello(self):
        print("我叫：" + self.name + "，我的年龄是：" + str(self.age) + "，我的体重是：" + str(self.__weight))


class Programmer(Person):
    language = ''

    def __init__(self, name, age, weight, language):
        self.language = language
        # 调用父类的构造器
        Person.__init__(self, name, age, weight)

    # 重写父类方法
    def say_hello(self):
        Person.say_hello(self)
        print("我的编程语言是：" + self.language)


programmer = Programmer('高司令', 60, 120, 'java')
programmer.say_hello()

