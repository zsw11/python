import threading
import time


def print_numbers():
    for i in range(5):
        print(i)
        # time.sleep(1)


def print_letters():
    for letter in 'abcde':
        print(letter)
        # time.sleep(1)


# 创建线程
thread1 = threading.Thread(target=print_numbers())
thread2 = threading.Thread(target=print_letters())

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread2.join()
thread1.join()
print("所有的线程完成")
