class Person:

    def __del__(self):
        print("销毁对象：{0}".format(self))


p1 = Person()  # 5. 销毁对象：<__main__.Person object at 0x000001DFCD279FC8>
print(p1)  # 1. 2060731260872
p2 = Person()  # 3. 销毁对象：<__main__.Person object at 0x000001DFCD284088>
print(p2)  # 2. 2060731302024
del p2    #用del语句删除对象，确保调用系统自动提供的__del__方法，一般不需要自定义析构方法
print("over")  # 4. over
# print(id(p2))  # name 'p2' is not defined
doc__ = p1.__class__
print(doc__)
doc2__ = p2.__class__
print(doc2__)
