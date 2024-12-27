from enum import Enum, auto
from calendar import month_name


class Month(Enum):
    JANUARY = (1, 31)
    FEBRUARY = (2, 28)  # Note: Not handling leap years for simplicity
    MARCH = (3, 31)
    APRIL = (4, 30)
    MAY = (5, 31)
    JUNE = (6, 30)
    JULY = (7, 31)
    AUGUST = (8, 31)
    SEPTEMBER = (9, 30)
    OCTOBER = (10, 31)
    NOVEMBER = (11, 30)
    DECEMBER = (12, 31)

    def __init__(self, number, days):
        self.number = number
        self.days = days

    @classmethod
    def from_number(cls, number):
        for month in cls:
            if month.number == number:
                return month
        raise ValueError(f"No month with number {number}")
    @property
    def name(self):
        return month_name[self.number]


# 使用示例
print(Month.JANUARY.name)  # 输出: January
print(Month.JANUARY.days)  # 输出: 31
# 使用新方法从数字获取月份
march_month = Month.from_number(3)
print(march_month.name)        # 输出: March

for enum_name, enum_value in Month.__members__.items():
    print(f"Enum Member Name: {enum_name}, Month Name: {enum_value.name}, Days: {enum_value.days}")

