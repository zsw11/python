# 定义一个类
class MyClass:
    class_var = "I am a class variable"  # 类

    def __init__(self, instance_var):
        self.instance_var = instance_var  # 实例属性

    # 实例方法
    def instance_method(self):
        print(f"Instance method called, instance_var={self.instance_var}")

    # 类方法
    @classmethod
    def class_method(cls):
        print(f"Class method called, class_var={cls.class_var}")

    # 静态方法
    @staticmethod
    def static_method():
        print("Static method called")

# 定义一个模块级别的函数
def module_level_function():
    print("Module level function called")

# 使用类和模块级别函数
if __name__ == "__main__":
    obj = MyClass("I am an instance variable")

    # 调用实例方法
    obj.instance_method()

    # 调用类方法
    MyClass.class_method()
    obj.class_method()  # 也可以通过实例调用

    # 调用静态方法
    MyClass.static_method()
    obj.static_method()  # 也可以通过实例调用

    # 调用模块级别函数
    module_level_function()