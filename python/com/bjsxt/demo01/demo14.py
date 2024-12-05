
myvar = '全局'


def myfunc():
    myvar1 = '局部'
    def myinnerfunc():
        myvar2 = '内嵌'


print(myvar)
# rint(myvar1)

# 的代码来查看到底预定义了哪些变量:
import builtins
dir(builtins)