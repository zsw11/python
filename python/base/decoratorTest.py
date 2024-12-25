# 装饰器 Python 中一种特殊的函数，用于动态地修改函数或方法的功能，而无需更改其源代码。
import functools
import time

def timing_decorator(func): # `func` 是被装饰的函数，作为入参
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行时间：{end - start:.2f} 秒")
        return result
    return wrapper   # 返回包装后的函数

@timing_decorator
def slow_function():
    time.sleep(2)
    print("函数执行完毕")

slow_function()

# 装饰器类
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("类装饰器：函数执行前")
        result = self.func(*args, **kwargs)
        print("类装饰器：函数执行后")
        return result

@MyDecorator
def say_hello():
    print("Hello, world!")

say_hello()

#偏函数 functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
max2 = functools.partial(max, 10)
max_ = max2(1, 2)
print(max_)