# 名称重整（Name Mangling）
class MyClass:
    def __init__(self):   # __init__ 方法并不属于私有方法，而是 Python 类中的构造方法（或初始化方法）。
        self.__private = "I'm private"

    def __private_method(self):
        print("This is a private method.")

class SubClass(MyClass):
    def __init__(self):
        super().__init__()
        print(self.__private)  # 子类中访问父类的私有属性会报错
        # self.__private_method()  # 子类中访问父类的私有方法也会报错

# 外部访问私有属性或方法
obj = MyClass()
# print(obj.__private)  # 会抛出 AttributeError
# obj.__private_method()  # 会抛出 AttributeError

# 使用名称重整访问
print(obj._MyClass__private)  # 访问私有属性
obj._MyClass__private_method()  # 调用私有方法

'''共有属性/方法：没有任何前缀，直接在类中定义，可以被外部访问。
受保护的属性/方法：以单下划线 _ 开头。只是一个约定，表示该属性或方法是类内部实现的一部分，不推荐外部使用。
私有属性/方法：以双下划线 __ 开头。通过名称重整（name mangling）机制使得这些属性和方法不容易被外部访问。尽管如此，仍然可以通过特殊的方式访问它们，但这种做法不被推荐 '''

'''
单下划线 _：
约定：表示受保护的属性或方法，不建议外部访问。
特殊用途：在某些情况下作为临时变量使用，或作为忽略值的标记。

双下划线 __：
表示私有属性/方法：通过名称重整（name mangling）来避免子类与父类的命名冲突。
特殊方法：在 Python 中双下划线还用来定义“魔法方法”，例如 __init__, __str__ 等。'''
