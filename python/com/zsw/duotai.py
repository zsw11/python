class Animal(object):
    def run(self):
        print('animal is running...')

    def run_twice(self, animal):
        animal.run()


class Dog(Animal):

    def run(self):
        print('dog is running ...')


class Cat(Animal):
    def run(self):
        print('cat is running ...')


def run_twice(animal): # animal这里只是形参，可以取任何名字
    animal.run()   # 如果animal没有run()方法就会报错
run_twice(Dog()) # 这里是实参

animal = Animal()
animal.run_twice(Cat())


    # 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
    # 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')
animal.run_twice(Timer()) # 输出Start...     动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的

