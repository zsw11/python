class Student(object):
    student = '学生'  # 类属性，属于类

    # 用tuple定义允许绑定的属性名称  __slots__用于限制实例化对象可以拥有的属性。主要作用是告诉 Python 不使用默认的 __dict__ 来存储实例属性，而是使用一个固定的、内存优化的数据结构。
    # __slots__ = ('__name', '__score')

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
# student.__name = '1'  # 这是实例内部新定义的 变量__name,不是 类的私有变量__name
student.get_score()
student.get_name()
# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的

# __dict__ 存储实例属性：__dict__ 存储对象的所有实例属性（包括动态添加的属性）。
print(student.__dict__)
print(type(123))
print(isinstance(student, Student))