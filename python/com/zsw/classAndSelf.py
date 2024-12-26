# 封装
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量sel
class Student(object):
    def __init__(self, name, score): #self就指向创建的实例本身。
        self.name = name  #可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去，每个实例都有这两个属性
        self.score = score

    #类的方法，提供外部访问内部的方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score>=90:
            return 'a'
        elif self.score >=60:
            return 'b'
        else:
            return 'c'
    pass


bart = Student("zsw",100)
print(bart)
# 可以自由地给一个实例变量绑定属性
bart.name = 'zsw'
print(bart.name)
bart.print_score()
print(bart.get_grade())

'''类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。'''
