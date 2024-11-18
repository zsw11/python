a = 5
b = 0
try:
    c = a / b
except:
    print("It is wrong.")

# 捕获所有可能出现的异常
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    print(e)

# 捕获指定类型的异常
a = 5
b = 0
try:
    c = a / b
except ZeroDivisionError:
    print("It is ZeroDivisionError.")

# 同时捕获多个异常
a = 5
b = 0
try:
    assert a < b
    c = a / b
except (ZeroDivisionError, AssertionError):
    print("It is ZeroDivisionError or AssertionError.")