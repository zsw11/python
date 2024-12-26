class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


student = Student('zsw', 100)
# student.__name --不可以访问私有变量
# student._Student__name # 可以访问，但不建议这么做
student.__name = '1'  # 这是实例内部新定义的 变量__name,不是 类的私有变量__name
student.get_score()
student.get_name()
# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的

type(123)