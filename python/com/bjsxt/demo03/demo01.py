class MySingleton:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        pass


mysingleton1 = MySingleton()
mysingleton2 = MySingleton()
print(mysingleton1)
print(mysingleton2)
print(id(mysingleton1))
print(id(mysingleton2))
print(mysingleton1 == mysingleton2)

