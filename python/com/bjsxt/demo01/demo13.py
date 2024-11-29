class Vector:

    xpos = 0
    ypos = 0

    def __init__(self, xpos, ypos):
        # 构造方法，对对象进行初始化
        self.xpos = xpos
        self.ypos = ypos

    def __add__(self, other):
        # 重写__add__方法
        # 运算符重载   vector1 + vector2 = vector3(1x+2x, 1y+2y)
        return Vector(self.xpos + other.xpos, self.ypos + other.ypos)

    def __str__(self):
        # 类似于java中的toString方法
        return "横坐标：" + str(self.xpos) + "；纵坐标：" + str(self.ypos)

    def __sub__(self, other):
        # # 运算符重载   vector1- vector2 = vector3(1x-2x, 1y-2y)
        return Vector(self.xpos - other.xpos, self.ypos - other.ypos)

    def __mul__(self, other):
        # 运算符重载   vector1 * vector2 = vector3(1x*2x, 1y*2y)
        return Vector(self.xpos * other.xpos, self.ypos * other.ypos)

    def __truediv__(self, other):
        # 不是整除
        # 运算符重载   vector1 / vector2 = vector3(1x/2x, 1y/2y)
        return Vector(self.xpos / other.xpos, self.ypos / other.ypos)

    def __mod__(self, other):
        # 运算符重载   vector1 % vector2 = vector3(1x%2x, 1y%2y)
        return Vector(self.xpos % other.xpos, self.ypos % other.ypos)

    def __pow__(self, power, modulo=None):
        # 运算符重载   vector1 ** 2 = vector2(1x**2, 1y**2)
        return Vector(self.xpos ** power, self.ypos ** power)


v1 = Vector(1, 3)
v2 = Vector(4, 5)

# 此处的+号操作对应类中的__add__方法
v = v1 + v2
print(v)

v = v1 - v2
print(v)

v = v1 * v2
print(v)

v = v1 / v2
print(v)

v = v1 % v2
print(v)

v = v1 ** 2
print(v)

