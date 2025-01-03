import threading
import time

# 创建一个锁
lock = threading.Lock()

# 共享的列表
a = 0


def safe_print_numbers():
    global a  # 声明a是全局变量
    # with lock: # 获取锁
    for i in range(10):
        time.sleep(1)
        print(i)
        a = a + 1


# 创建线程
thread1 = threading.Thread(target=safe_print_numbers)
thread2 = threading.Thread(target=safe_print_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(a)
