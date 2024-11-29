
try:
    print("这是上方的语句")
    num1 = 1 / 0
    num1 = 100 / 10

    # say_hello()

    print("这是下方的语句")
except (ZeroDivisionError, NameError) as e:
    print("你又拿0做除数了吧")
    #  打印异常信息
    print(e)
finally:
    print("好，该结束了")

