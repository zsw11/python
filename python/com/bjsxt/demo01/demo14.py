
myvar = '全局'


def myfunc():
    myvar1 = '局部'

    def myinnerfunc():
        myvar2 = '内嵌'


# print(myvar)
# 无法访问
# print(myvar1)