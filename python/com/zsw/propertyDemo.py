'''@property 是一个用于将方法转化为属性访问方式的装饰器。它允许你在不改变调用方式的情况下，使用方法来计算或返回一个属性值。
通过使用 @property，你可以将一些需要计算的值以属性的形式暴露给外部，提供更加清晰、简洁的接口。'''
class Circle:
    def __init__(self, radius):
        self._radius = radius  # 私有变量

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

# 使用 @property
circle = Circle(5)
print(circle.radius)  # 访问 radius 属性，输出: 5   @property 装饰器将 radius 方法变成了一个属性，circle.radius 变成了对 circle._radius 的访问。
circle.radius = 10    # 修改 radius 属性           @radius.setter 装饰器允许你修改 radius 属性，并且可以添加一些额外的逻辑（例如限制半径的值不能为负数）。
print(circle.area)    # 访问 area 属性，输出: 314.0
